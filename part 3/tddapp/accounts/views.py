from django.http import HttpResponse
from django.shortcuts import render
from accounts.models import Account

def login(request):
    
    valid = True

    if request.method == "POST":
        if _is_valid_login(request.POST['username'], request.POST['password']):        
            return HttpResponse("Login Succesful")
        else:
            valid = False

    return render(request, 'login.html', {'valid' : valid,
                                    'referrer' : 'RealPython'})

def _is_valid_login(username, password):
    user_list = Account.objects.filter(username=username, password=password)
    return len(user_list) > 0
