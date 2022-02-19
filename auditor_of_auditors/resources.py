from import_export import resources
from . import models

# Create your forms here.
from .models import Auditor_of_auditors

class RiskManagemenResource(resources.ModelResource):

    class Meta:
        model = Auditor_of_auditors
        fields = "__all__"
