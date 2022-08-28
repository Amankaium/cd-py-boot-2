# from django.shortcuts import HttpResponse


def superuseronly(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            fn()
        else:
            raise Exception("no permission")
            # return HttpResponse("No permission", status=403)
    return wrapper
