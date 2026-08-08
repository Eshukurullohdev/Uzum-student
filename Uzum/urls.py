from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("detail/<int:id>/", detail, name="detail"),
    path("topshirish_punkiti/", topshirish_punkiti, name="topshirish_punkiti"),
    path("navigation/", navigation, name="navigation"),
    path("footer/", footer, name="footer"),
    path("sotuvchi_bolish/", sotuvchi_bolish, name="sotuvchi_bolish"),
    path("sotuv/", sotuv, name="sotuv"),
    path("savol/", savol, name="savol"),
    path("sotuvchilik/", sotuvchilik, name="sotuvchilik")
]
