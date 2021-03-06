import requests
import json
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta


class KakaotalkMessageView(View):
    def get(self, request, step, result):
        if step == 1 and result == 1:
            URL = "https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=636%3A8&node-id=636%3A6795&viewport=431%2C1773%2C0.2996300160884857&scaling=min-zoom"
            response = redirect(URL)
            try:
                res = request.COOKIES.get('k'+str(step))
                response.set_cookie(key='k'+str(step), value=str(int(res)+1))
                return response
            except:
                response.set_cookie(key='k'+str(step), value=1)
                return response
        elif step == 1 and result == 0:
            URL = "https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=636%3A8&node-id=636%3A6066&viewport=431%2C1773%2C0.2996300160884857&scaling=min-zoom"
            response = redirect(URL)
            try:
                res = request.COOKIES.get('k'+str(step))
                print(int(res)-1)
                response.set_cookie(key='k'+str(step), value=str(int(res)-1))
                return response
            except:
                response.set_cookie(key='k'+str(step), value=-1)
                return response
        elif step == 2 and result == 1:
            URL = "https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=636%3A8&node-id=636%3A6855&viewport=431%2C1773%2C0.2996300160884857&scaling=min-zoom"
            response = redirect(URL)
            try:
                res = request.COOKIES.get('k'+str(step))
                response.set_cookie(key='k'+str(step), value=str(int(res)+1))
                return response
            except:
                response.set_cookie(key='k'+str(step), value=11)
                return response
        elif step == 2 and result == 0:
            URL = "https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=636%3A8&node-id=636%3A6795&viewport=431%2C1773%2C0.2996300160884857&scaling=min-zoom"
            response = redirect(URL)
            try:
                res = request.COOKIES.get('k'+str(step))
                response.set_cookie(key='k'+str(step), value=str(int(res)-1))
                return response
            except:
                response.set_cookie(key='k'+str(step), value=-1)
                return response
        elif step == 3 and result == 1:
            URL = "https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=636%3A8&node-id=636%3A6906&viewport=431%2C1773%2C0.2996300160884857&scaling=min-zoom"
            response = redirect(URL)
            try:
                res = request.COOKIES.get('k'+str(step))
                response.set_cookie(key='k'+str(step), value=str(int(res)+1))
                return response
            except:
                response.set_cookie(key='k'+str(step), value=11)
                return response
        elif step == 3 and result == 0:
            URL = "https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=636%3A8&node-id=636%3A6855&viewport=431%2C1773%2C0.2996300160884857&scaling=min-zoom"
            response = redirect(URL)
            try:
                res = request.COOKIES.get('k'+str(step))
                response.set_cookie(key='k'+str(step), value=str(int(res)-1))
                return response
            except:
                response.set_cookie(key='k'+str(step), value=-1)
                return response
        elif step == 4 and result == 1:
            URL = "https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=636%3A8&node-id=636%3A7090&viewport=431%2C1773%2C0.2996300160884857&scaling=min-zoom"
            response = redirect(URL)
            try:
                res = request.COOKIES.get('k'+str(step))
                response.set_cookie(key='k'+str(step), value=str(int(res)+1))
                return response
            except:
                response.set_cookie(key='k'+str(step), value=11)
                return response
        elif step == 4 and result == 0:
            URL = "https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=636%3A8&node-id=636%3A6906&viewport=431%2C1773%2C0.2996300160884857&scaling=min-zoom"
            response = redirect(URL)
            try:
                res = request.COOKIES.get('k'+str(step))
                response.set_cookie(key='k'+str(step), value=str(int(res)-1))
                return response
            except:
                response.set_cookie(key='k'+str(step), value=-1)
                return response
        elif step == 5 and result == 1:
            URL = "https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=636%3A8&node-id=636%3A7258&viewport=431%2C1773%2C0.2996300160884857&scaling=min-zoom"
            response = redirect(URL)
            try:
                res = request.COOKIES.get('k'+str(step))
                response.set_cookie(key='k'+str(step), value=str(int(res)+1))
                return response
            except:
                response.set_cookie(key='k'+str(step), value=11)
                return response
        elif step == 5 and result == 0:
            URL = "https://www.figma.com/proto/ZV42t1vudbKH1nxSPCPy3p/%EC%82%B0%ED%98%91%ED%94%84-%EA%B3%B5%EC%9C%A0%EA%B3%B5%EA%B0%84_%EC%95%88%EB%93%9C%EB%9D%BC%EA%B3%A0%EC%A7%80?page-id=636%3A8&node-id=636%3A7090&viewport=431%2C1773%2C0.2996300160884857&scaling=min-zoom"
            response = redirect(URL)
            try:
                res = request.COOKIES.get('k'+str(step))
                response.set_cookie(key='k'+str(step), value=str(int(res)-1))
                return response
            except:
                response.set_cookie(key='k'+str(step), value=-1)
                return response
        else:
            return HttpResponse("????????? ???????????????.")


class KakaotalkMessageResultView(View):
    def get(self, request):
        k1 = request.COOKIES.get('k1')
        k2 = request.COOKIES.get('k2')
        k3 = request.COOKIES.get('k3')
        k4 = request.COOKIES.get('k4')
        k5 = request.COOKIES.get('k5')
        response = render(request, 'result.html', {
            'k1': k1,
            'k2': k2,
            'k3': k3,
            'k4': k4,
            'k5': k5,
        })
        for i in range(1, 6):
            response.set_cookie(key='k'+str(i), value=0)
        return response
