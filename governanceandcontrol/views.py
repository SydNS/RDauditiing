from django.shortcuts import render
from . import models


# Create your views here.
def dashboard(request):
    gncobj = models.GncTable.objects.all()
    # info =
    return render(request, 'governanceandcontrol/index.html', {
        "gncojbects": gncobj
    })


def loginuser(request):
    info = {
        "apple": "green",
        "banana": "yellow",
        "cherry": "red"
    }
    return render(request, 'governanceandcontrol/login.html', info)
