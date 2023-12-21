from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,logout
from django.urls import reverse

# Create your views here.

#定义跳转页面
def index(request):
    return render(request, 'IEAS_WEB/base.html')

def user_login(request):
    return render(request, 'IEAS_WEB/login.html')
    

# 执行登录操作
def user_dologin(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            # 将用户名存入session
            request.session['session_username'] = username
            # 跳转到主界面
            # return render(request, 'IEAS_WEB/base.html')
            return redirect(reverse('index_view'))
        else:
            context ={"info":"密码错误或者账号不存在"}
            return render(request,'IEAS_WEB/login.html',context)
    except Exception as err:
        return render(request,'IEAS_WEB/login.html')
    


# 用户退出登录
def user_logout(request):
    try:
        del request.session['session_username']
    except KeyError:
        pass
    return redirect(reverse('user_login'))



    





















    