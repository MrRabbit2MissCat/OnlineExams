from django.db import models


# Create your models here.
class Questions(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=50)
    question_type = models.CharField(max_length=50)
    question = models.CharField(max_length=2500)
    analyze = models.CharField(max_length=2500, blank=True, null=True)
    retail_credit_department = models.CharField(max_length=100, blank=True, null=True)
    corporate_credit_department = models.CharField(max_length=100, blank=True, null=True)
    customer_service = models.CharField(max_length=100, blank=True, null=True)
    marketing_department = models.CharField(max_length=100, blank=True, null=True)
    brand_public_relations_department = models.CharField(max_length=100, blank=True, null=True)
    the_brand_sales_department = models.CharField(max_length=100, blank=True, null=True)
    multi_brand_sales_department = models.CharField(db_column='multi-brand_sales_department', max_length=100,
                                                    blank=True,
                                                    null=True)  # Field renamed to remove unsuitable characters.
    used_car_business_department = models.CharField(max_length=100, blank=True, null=True)
    technology_business_department = models.CharField(max_length=100, blank=True, null=True)
    big_data_platform_department = models.CharField(max_length=100, blank=True, null=True)
    ministry_of_science_and_technology = models.CharField(max_length=100, blank=True, null=True)
    risk_management_department = models.CharField(max_length=100, blank=True, null=True)
    financial_accounting_department = models.CharField(max_length=100, blank=True, null=True)
    integrated_management_department = models.CharField(max_length=100, blank=True, null=True)
    operation_management_department = models.CharField(max_length=100, blank=True, null=True)
    internal_audit_section = models.CharField(max_length=100, blank=True, null=True)
    legal_compliance_department = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'questions'
