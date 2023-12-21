from django.shortcuts import render

#定义跳转--上传--界面
def upload_view(request):
    return render(request, 'IEAS_WEB/upload.html')