from django.shortcuts import render

# Create your views here.
def index(request):
    info={}
    return render(request,'governanceandcontrol/dashboard1.html',info)