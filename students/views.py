from django.http import HttpResponse

# Create your views here.

def students(request):
    return HttpResponse("Hello, world. You're at the students page.")