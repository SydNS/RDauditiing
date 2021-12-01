from django.shortcuts import render


# Create your views here.
def dashboard(request):
    info = {
        "apple": "green",
        "banana": "yellow",
        "cherry": "red"
    }
    return render(request, 'governanceandcontrol/index.html', info)


def loginuser(request):
    info = {
        "apple": "green",
        "banana": "yellow",
        "cherry": "red"
    }
    return render(request, 'governanceandcontrol/login.html', info)
