from django.shortcuts import render

def login(request):
    #return HttpResponse("this is a login")
    return render(request, 'login.html') 