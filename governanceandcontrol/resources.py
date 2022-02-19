from import_export import resources
from . import models

# Create your forms here.
from .models import Governance_And_Control

class RiskManagemenResource(resources.ModelResource):

    class Meta:
        model = Governance_And_Control
        fields = "__all__"
