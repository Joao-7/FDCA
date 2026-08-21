from django.shortcuts import render

# Create your views here.
def pagina_login(request):
    return render(request, 'login.html')
