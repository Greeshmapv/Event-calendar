from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_event')  # Redirect to the index page after successful form submission
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_event(request):
    authenticationform=AuthenticationForm()
    if request.method=="POST":
        authenticationform=AuthenticationForm(request,data=request.POST or None)
        if authenticationform.is_valid():
            username=authenticationform.cleaned_data["username"]
            password=authenticationform.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user=user)
                return redirect("index")
        else:
            print(authenticationform.errors)
    return render (request,template_name="login.html",context={"authenticationform":authenticationform})
def logout_user(request):
    logout(request)
    return redirect('/')
