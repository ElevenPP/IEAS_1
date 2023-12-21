from django.shortcuts import render
#定义跳转--码址--页面

def adress_view(request):
    return render(request, 'IEAS_WEB/adress.html')