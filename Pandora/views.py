from django.shortcuts import render
from .models import ToolInfo

# Create your views here.
def index(request):
    return render(request,'index.html')

def tools_test(request):
    toollist = ToolInfo.objects.all().select_related('group_code')
    for i in toollist:
        name = i.name
        type = i.tool_group.group_name
    return render(request,'tools_test.html', {'toollist':toollist})