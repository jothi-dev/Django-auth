from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from main.models import Post


def on_login(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        content_type = ContentType.objects.get_for_model(Post)
        post_permissions = Permission.objects.filter(content_type=content_type)

        # add user permissions on login
        if request.path == "/home":
            print("add user perms --", request.path)
            for perm in post_permissions:
                request.user.user_permissions.add(perm)

        # remove user permissions on logout
        if request.path == "/logout/":
            for perm in post_permissions:
                request.user.user_permissions.remove(perm)

        response = get_response(request)

        return response

    return middleware
