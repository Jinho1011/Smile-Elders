import requests
import json
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta


class k1r(View):
    def get(self, request):
        response = redirect("https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=419%3A8&node-id=419%3A4187&viewport=515%2C3139%2C0.253072589635849&scaling=scale-down")
        response.set_cookie(key="k1", value=1)
        return response


class k1w(View):
    def get(self, request):
        response = redirect("https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=419%3A8&node-id=419%3A4039&viewport=515%2C3139%2C0.253072589635849&scaling=scale-down")
        response.set_cookie(key="k1", value=0)
        return response
