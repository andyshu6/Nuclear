from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def tools_test(request):
    return render(request,'tools_test.html')