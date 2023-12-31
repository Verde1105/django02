from django.contrib.auth import authenticate, login
from django.shortcuts import render,  redirect
from common.forms import UserForm


def signup(request):
    """
    회원가입
    """

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            print("username",username)
            print("password1",password1)
            print("password2",password2)

            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form})

