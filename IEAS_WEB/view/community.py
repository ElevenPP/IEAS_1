from django.shortcuts import render

#定义跳转--通联--界面
def community_view(request):
    return render(request, 'IEAS_WEB/community.html')


