from django.shortcuts import render

from .models import Uzum

# Create your views here.
def navigation(request):
    return render(request, "navigation.html")


def footer(request):
    return render(request, "footer.html")

def home(request):
    mahsulotlar = Uzum.objects.all()
    
    context = {
        "mahsulotlar": mahsulotlar
    }
    return render(request, "home.html", context) 

def detail(request, id):
    mahsulotlar = Uzum.objects.get(id=id)
    context = {
        "mahsulotlar": mahsulotlar
    }
    return render(request, "detail.html", context)

def topshirish_punkiti(request):
    return render(request, "topshirish_punkiti.html")


def sotuvchi_bolish(request):
    return render(request, "sotuvchi_bolish.html")

def sotuv(request):
    return render(request, "sotuv.html")
def savol(request):
    return render(request, "savol.html")
def sotuvchilik(request):
    return render(request, "sotuvchilik.html")