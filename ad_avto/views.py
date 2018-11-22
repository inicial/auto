from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from ad_avto.models import Ad, Comments


def detail(request, ad_id):
    ad = Ad.objects.filter(id=ad_id)
    comments = Comments.objects.filter(adId=ad_id, status=True)
    return render(request, 'ad/detail.html', {"ad": ad, "comment": comments})
