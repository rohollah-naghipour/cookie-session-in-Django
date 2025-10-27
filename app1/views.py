from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


def set_cookie_view(request):
    response = HttpResponse("Cookie set successfully!")
    response.set_cookie('user_name', 'Ali', max_age=3600)  
    return response

def get_cookie_view(request):
    name = request.COOKIES.get('user_name', 'Guest')
    return HttpResponse(f"Welcome back, {name}!")



def set_session_view(request):
    request.session['user_name'] = 'Ali'
    return HttpResponse("Session set successfully!")

def get_session_view(request):
    name = request.session.get('user_name', 'Guest')
    return HttpResponse(f"Welcome back, {name}!")


#def login_view(request):
    #if request.method == "POST":
        #username = request.POST.get("username")
        #password = request.POST.get("password")

        #if username == "admin" and password == "1234":
            #request.session["user"] = username 
            #return redirect('index')
        #else:
            #return HttpResponse("Invalid credentials. Try again.")
    
    #return render(request, "login.html")


#def home_view(request):
    #user = request.session.get("user")
    #if not user:
        #return redirect("login")  
    #return HttpResponse(f"Welcome {user}! You are logged in using session.")


#def logout_view(request):
    #try:
        #del request.session["user"] 
    #except KeyError:
        #pass
    #return HttpResponse("You have been logged out successfully!")

# BEFORE FORM


# AFTER FORM
def login_view1(request):
    if request.method == "POST":
        print("request.POST =", request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

        try:    
            user = User.objects.get(username=username)
            print('request.user =', request.user)
            print('user =', user)
            print('username send by the user =', username)

            if check_password(password, user.password):
                print('The password sent by the user =', password)
                print('Hashed password in the database =', user.password)
                request.session["user"] = username  
                return redirect("index")
            else:
                print("The password is incorrect")
                return HttpResponse("The username or password is incorrect.",
                 {'user': request.user})
        
        except User.DoesNotExist:
            return HttpResponse("The username or password is incorrect.")

    form = LoginForm()
    return render(request, "login.html", {"form": form})


def home_view1(request):
    user = request.session.get("user")
    print('user =', user)
    if not user:
        return redirect("login")
    return render(request,"index.html",{'user': request.user})
    print(request.user)


def logout_view1(request):
    request.session.flush()  
    return HttpResponse("You have successfully logged out 🧹")
