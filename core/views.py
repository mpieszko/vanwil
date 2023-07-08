from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request, 'core/index.html')
# def home(request):
#     return render(request, "core/home.html")

def about(request):
    return render(request, "core/quienessomos.html")


def contact(request):
    return render(request, "core/contactos.html")


def industria4(request):
    return render(request, "core/industria4.0.html")
