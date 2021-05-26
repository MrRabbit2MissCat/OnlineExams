import json
import re
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from index.models import Questions
from user.models import User


# Create your views here.
def get_answer(title):
    answer = re.findall(r'（(.*?)）', title)
    return answer


def question_list(questions):
    questions_list = []
    for question in questions:
        question_id = question.id
        question_type = question.question_type
        content = question.question
        content_list = content.split("\n")
        # 去除题目内的答案
        # title = re.sub(r"[A-F]", "", content_list[0])
        title = content_list[0]
        items = "|".join([re.sub(r'[A-F][.，,、]?', '', item) for item in content_list[1:]])
        answer = get_answer(title)
        questions_list.append(
            {
                "questionId": f"{question_id}",
                "questionType": f"{question_type}",
                "questionTitle": f"{title}",
                "questionItems": f"{items}",
                "questionAnswer": answer
            }
        )
    return json.dumps(questions_list)


def login_vaild(fun):
    def inner(request, *args, **kwargs):
        username = request.get_signed_cookie("username", None, salt="~!@#")
        username_session = request.session.get("name")
        if username_session and username:
            return fun(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/")

    return inner


def login(request):
    if request.method == "GET":
        return render(
            request,
            'login.html'
        )
    elif request.method == "POST":
        name = request.POST["username"]
        department = request.POST["department"]
        questions_type = request.POST["questions_type"].split(":")[:-1]
        try:
            User.objects.create(username=name, department=department).save()
        except Exception as e:
            print(e)
        response = HttpResponse()
        response.set_signed_cookie("username", name.encode("utf-8"), salt="~!@#")
        request.session["name"] = name
        request.session["department"] = department
        request.session["question_type"] = questions_type
        request.session.set_expiry(0)
        return response


@login_vaild
def index(request):
    if request.method == "GET":
        department = request.session.get("department", None)
        question_type = request.session.get("question_type", None)
        qt = ','.join(question_type)
        if department:
            SQL = f"select * from questions where {department} != '' and question_type in ({qt});"
            questions = Questions.objects.raw(SQL)
            result = question_list(questions)
            return render(
                request,
                "index.html",
                {"data": result}
            )


@login_vaild
def exit_login(request):
    if request.method == "GET":
        response = HttpResponse()
        response.delete_cookie('username')
        response.delete_cookie('sessionid')
        request.session.flush()
        return response
