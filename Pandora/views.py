from django.shortcuts import render
from .models import ToolInfo

# Create your views here.
def index(request):
    return render(request,'index.html')

def tools_test(request):
    toollist = ToolInfo.objects.all()
    return render(request,'tools_test.html')