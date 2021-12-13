from django.contrib import admin


# Register your models here.

@admin.register(RiskManagement)
class RiskManagementAdmin(admin.ModelAdmin):
    list_display = ('xy_strategic_pillar', 'xy_strategic_objectives', 'risk_category', 'risk_description',
                    'likelihood', 'impact', 'risk_rating', 'control_exists_yesno',
                    'control_description', 'control_is_adequate_yesno', 'recommended_control'
                    , 'action',
                    'kri', 'target', 'dept',
                    )
    list_filter = ('xy_strategic_pillar',
                   'control_description', 'xy_strategic_objectives', 'risk_category',
                   )
    search_fields = ('xy_strategic_pillar', 'xy_strategic_objectives', 'dept',
                     'impact', 'target',
                     )
