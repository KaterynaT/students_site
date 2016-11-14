from django.conf import settings

def processor(request):
    return dict(settings=settings)