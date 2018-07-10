# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import ToolInfo

# Create your views here.
def index(request):
    return render(request,'index.html')

def tools_test(request):
    toollist = ToolInfo.objects.all()
    # for i in toollist:
    #     name = i.tool_name
    #     print(name)
    #     # type = i.tool_group.all()[0].group_name
    #     for j in i.ToolInfo_set.all():
    #         print(j)

    return render(request,'tools_test.html', {'toollist':toollist})