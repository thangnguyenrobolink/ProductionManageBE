import json
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser


class JWTUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        jwt_authenticator = JWTAuthentication()
        try:
            user, _ = jwt_authenticator.authenticate(request)
            request.user = user
        except Exception:
            request.user = AnonymousUser()

        if request.method in ['POST', 'PUT', 'PATCH']:
            if request.content_type == 'application/json':
                try:
                    data = json.loads(request.body)
                    if request.user and request.user.is_authenticated:
                        if request.method == 'POST':
                            data['created_by'] = request.user.id
                        else:
                            data['updated_by'] = request.user.id
                    request._body = json.dumps(data).encode('utf-8')
                except json.JSONDecodeError:
                    pass
            elif request.content_type == 'application/x-www-form-urlencoded':
                data = request.POST.copy()
                if request.user and request.user.is_authenticated:
                    if request.method == 'POST':
                        data['created_by'] = request.user.id
                    else:
                        data['updated_by'] = request.user.id
                request.POST = data