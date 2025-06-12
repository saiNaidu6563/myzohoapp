from django.contrib import admin

from crm.models import Lead
class LeadAdmin(admin.ModelAdmin):
    list_display = ['id','lname','lemail','phone','created_at']
admin.site.register(Lead,LeadAdmin)
