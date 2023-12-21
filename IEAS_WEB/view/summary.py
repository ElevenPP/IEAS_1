from django.http import HttpResponse
from django.shortcuts import render

#定义跳转--概括--界面
def summary_view(request):
    return render(request, 'IEAS_WEB/summary.html')


def summary_print(request,op="0"):
    return HttpResponse(op)