from django.contrib import admin
from .models import ToolGroupInfo, ToolInfo
# Register your models here.



class ToolGroupInfoAdmin(admin.ModelAdmin):
    list_display = ("group_code", "group_parent", "group_name")
    list_filter = ("group_parent", "group_name")
    search_fields = ("group_parent", "group_name")

class ToolInfoAdmin(admin.ModelAdmin):
    list_display = ("tool_name", "tool_url", "tool_heat")
    list_filter = ("tool_name", "tool_group")
    search_fields = ("tool_name", "tool_group")

admin.site.register(ToolGroupInfo,ToolGroupInfoAdmin)
admin.site.register(ToolInfo, ToolInfoAdmin)