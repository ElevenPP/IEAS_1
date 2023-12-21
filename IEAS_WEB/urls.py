from django.contrib import admin
from django.urls import path,include
from IEAS_WEB.view import adress,community,index,summary,translate,upload,login

urlpatterns = [
    path("",login.user_login,name="user_login" ),
    # 定义登录操作路由
    path("login/",login.user_dologin,name="user_dologin" ),
    # 定义退出操作路由
    path("user_logout/",login.user_logout,name="user_logout" ),

    # 定义跳转路径
    path("index/",login.index,name="index"),

    # 定义跳转至主界面
    # path("index_view",views.index_view,name="index_view"),
    path("index_view/",index.index_view,name="index_view"),

    # 定义跳转至码址界面
    # path("adress_view",views.adress_view,name="adress_view"),
    path("adress_view/",adress.adress_view,name="adress_view"),

    # 定义跳转至通联界面
    # path("community_view",views.community_view,name="community_view"),
    path("community_view/",community.community_view,name="community_view"),

    # 定义跳转至概括界面
    # path("summary_view",views.summary_view,name="summary_view"),
    path("summary_view/",summary.summary_view,name="summary_view"),
    path("summary_print/<str:op>",summary.summary_print,name="summary_print"),

    # 定义跳转至上传界面
    # path("upload_view",views.upload_view,name="upload_view"),
    path("upload_view/",upload.upload_view,name="upload_view"),

    # 定义跳转至翻译界面
    # path("translate_view",views.translate_view,name="translate_view"),
    path("translate_view/",translate.translate_view,name="translate_view"),



    

]