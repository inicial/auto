from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from ad_avto.models import Ad


def index_view(request):
    ad = Ad.objects.filter(status=True)[:3]
    ad_hot = Ad.objects.filter(status=True, isHot=True)
    ad_recently = Ad.objects.order_by('date').filter(status=True)
    return render(request, 'mainpage/index.html', {"ad": ad, "ad_hot": ad_hot, "ad_recently": ad_recently})
