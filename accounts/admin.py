from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from .models import Department, Person, RatingUser


# class Dept(models.Model):
#     CRITICALITY_LEVELS = (
#         ('low', 'low'),
#         ('medium', 'medium'),
#         ('high', 'high'),
#     )
#     deptname = models.TextField()
#     deptrole = models.TextField()
#     deptcriticality = models.TextField()
#     numberofmembers = models.IntegerField()
#     criticality = models.CharField(db_column='Criticality', max_length=20, blank=False, null=True,
#                                    choices=CRITICALITY_LEVELS, default='draft')  # Field name made lowercase.

@admin.register(Department)
class DeptAdmin(ImportExportModelAdmin):
    list_display = ('departmentname', 'departmentrole', 'numberofmembers', 'criticality',)
    list_filter = ('departmentname', 'departmentrole', 'numberofmembers', 'criticality',)
    search_fields = ('departmentname', 'departmentrole', 'numberofmembers', 'criticality',)


# class Person(models.Model):
#     last_name = models.TextField()
#     first_name = models.TextField()
#     personemail = models.EmailField()
#     personsdept = models.ForeignKey(Dept, on_delete=models.CASCADE)

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('last_name', 'first_name', 'personsdept',)
    list_filter = ('last_name', 'first_name', 'personsdept',)
    search_fields = ('last_name', 'first_name', 'personsdept',)


#
# class GradingUser(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     grade = models.PositiveSmallIntegerField()
#     deptnem = models.ForeignKey(Dept, on_delete=models.CASCADE)
#
@admin.register(RatingUser)
class RatingUserAdmin(ImportExportModelAdmin):
    list_display = ('person', 'rate_level', 'department',)
    list_filter = ('person', 'rate_level', 'department',)
    search_fields = ('person', 'rate_level', 'department',)
