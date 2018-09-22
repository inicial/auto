from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from ad_avto.models import Ad


def indexView(request):
    ad = Ad.objects.all()[:3]
    return render(request, 'mainpage/index.html', {"ad": ad})
