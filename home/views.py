# _*_ coding:utf-8 _*_

from __future__ import unicode_literals

from django.shortcuts import render


def home(request):
    return render(request, "home.html")
