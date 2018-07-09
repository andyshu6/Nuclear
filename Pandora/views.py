# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import ToolInfo

# Create your views here.
def index(request):
    return render(request,'index.html')

def tools_test(request):
    toollist = ToolInfo.objects.all()
    grouplist = {}
    for i in toollist:
        type = i.tool_group.all()[0].group_name
        grouplist.append(type)

    return render(request,'tools_test.html', {'toollist':toollist, 'grouplist':grouplist})