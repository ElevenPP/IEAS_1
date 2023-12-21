import re
from django.urls import reverse
from django.shortcuts import redirect


class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # 定义后台直接访问的地址
        urlslist = ['/login/','/admin/',""]
        if not request.path.startswith('/admin'):
            if request.path not in urlslist: 
                if 'session_username' not in request.session:
                    return redirect(reverse('user_dologin'))
     
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response