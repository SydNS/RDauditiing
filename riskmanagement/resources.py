from import_export import resources
from . import models

# Create your forms here.
from .models import RiskManagement

class RiskManagemenResource(resources.ModelResource):

    class Meta:
        model = RiskManagement
        fields = "__all__"
