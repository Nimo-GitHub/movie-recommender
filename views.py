from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "test/home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "test/login.html", {})

def register_view(request, *args, **kwargs):
    return render(request, "test/register.html", {})

# def movie_view(request, *args, **kwargs):
# 	movie = Movie.objects.get(id=1)	
# 	context = {
# 		'movie' : movie
# 	}
# 	return render(request, "details.html", context)

# # def movie_form_view(request, *args, **kwargs):
# # 	form = MovieForm()
# # 	if request.method == 'POST':
# # 		form = MovieForm(request.POST)
# # 		if form.is_valid():
# # 			Movie.objects.create(**form.cleaned_data)

# # 	context = {'form' : form }
# # 	return render(request, "movie_form.html", context)

# def login_form(request, *args, **kwargs):
# 	return render(request, "log_in_form.html")

# def signup_form(request, *args, **kwargs):
# 	form=UserCreationForm()
# 	context={'form':form}
# 	return render(request, "sign_up_form.html",context)


# def signup(request,*args,**kwargs):
# 	if request.method=="POST":
		
# 		name=request.POST['usrnm'],
# 		email=request.POST['email'],
# 		password=request.POST['psw']
# 		print(password)
# 		user=User(username=name,email=email,password=password)
# 		user.save()
# 		return render(request, "sign_up_form.html")

# def login(request,*args,**kwargs):
# 	if request.method=="POST":
		
# 		email=request.POST['email'],
# 		password=request.POST['psw']
# 		user=User(username=name,email=email,password=password)
# 		return render(request, "log_in_form.html")
