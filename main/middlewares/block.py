from django.shortcuts import redirect
from django.contrib import messages

emails_to_block = ["kangethejosphat01@gmail.com"]


def block_user(get_response):
    def middleware(request):
        # block user of certain emails
        if request.path == "/home" and request.user.email in emails_to_block:
            messages.add_message(
                request,
                messages.INFO,
                "Sorry. You've been blocked from this site. Kindly contact support.",
            )
            return redirect("/logout")

        response = get_response(request)

        return response

    return middleware
