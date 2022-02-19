from import_export import resources
from . import models

# Create your forms here.
from .models import Person, RatingUser, Department


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
        fields = "__all__"


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
        fields = "__all__"


class RatingUserResource(resources.ModelResource):
    class Meta:
        model = RatingUser
        fields = "__all__"
