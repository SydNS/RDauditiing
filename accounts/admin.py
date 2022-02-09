from django.contrib import admin

# Register your models here.
from .models import Department,Person,RatingUser

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
class DeptAdmin(admin.ModelAdmin):
    list_display = ('deptname', 'deptrole', 'numberofmembers', 'criticality',)
    list_filter = ('deptname', 'deptrole',  'numberofmembers', 'criticality',)
    search_fields = ('deptname', 'deptrole', 'numberofmembers', 'criticality',)


# class Person(models.Model):
#     last_name = models.TextField()
#     first_name = models.TextField()
#     personemail = models.EmailField()
#     personsdept = models.ForeignKey(Dept, on_delete=models.CASCADE)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'personemail', 'personsdept',)
    list_filter = ('last_name', 'first_name', 'personemail', 'personsdept',)
    search_fields = ('last_name', 'first_name', 'personemail', 'personsdept',)


#
# class GradingUser(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     grade = models.PositiveSmallIntegerField()
#     deptnem = models.ForeignKey(Dept, on_delete=models.CASCADE)
#
@admin.register(RatingUser)
class RatingUserAdmin(admin.ModelAdmin):
    list_display = ('person', 'grade', 'deptnem',)
    list_filter = ('person', 'grade', 'deptnem',)
    search_fields = ('person', 'grade', 'deptnem',)
