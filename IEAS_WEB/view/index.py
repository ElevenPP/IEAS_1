from django.shortcuts import render

#定义跳转--首页--页面
def index_view(request):
    return render(request, 'IEAS_WEB/index.html')