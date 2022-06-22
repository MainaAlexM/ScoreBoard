from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import Registration, LoginForm, SubmitForm, ProfileEditForm
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Project, Profile, Ratings
from .serializers import ProjectSerializer, ProfileSerializer
from rest_framework.decorators import api_view

# Views.


def register_request(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are Successfully Registered. Proceed to Login")
            return redirect("login")
        messages.error(
            request, "Registration Failed. Use a Strong Password and Fill all the Fields")
    form = Registration()
    return render(request, template_name="auth/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "You Entered Wrong Username or Password")
            return redirect('login')
    form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, 'auth/login.html', context=context)


def home(request):
    projects=Project.objects.all()
    user_view = request.user

    return render(request,'home.html',context={"projects":projects,"user_view":user_view})


@login_required
def submit_request(request):
    user_view = request.user

    if request.method == "POST":
        form = SubmitForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description =form.cleaned_data["description"]
            site_url = form.cleaned_data["site_url"]
            landing_page = form.cleaned_data["landing_page"]
            new_project = Project(title=title, description=description,site_url=site_url)
            new_project.landing_page = landing_page
            new_project.owner = request.user
            new_project.save()
            messages.success(request,"Upload Successful!") 
            return redirect('home')
    
    form = SubmitForm()
    context = {
        "form": form,
        "user_view":user_view
    }
    return render(request, 'submit.html',context=context)


@login_required
def project_detail(request,id):
    projects=Project.objects.get(id=id)
    user_view = request.user

    reviews = Ratings.objects.filter(project=projects)
    print(projects.title)
    return render(request, 'details.html',context={"projects":projects,'ratings':reviews,'user_view':user_view} )


def project_search(request):
    projects=Project.objects.all()
    if 'name' in request.GET and request.GET['name']:
        searched_term = request.GET['name']
        user_view = request.user

        searched = Project.search_project(searched_term)
        message = f"Results For {searched_term}"
    
        return render(request, 'search_results.html', {"message": message, 'searched': searched, 'user_view':user_view})
    else:
        message = "Enter a Search Term to Proceed"
        return render(request, 'search_results.html', {"message": message})


@api_view(['GET','POST'])
def project_list(request):
    if request.method=='GET':
        projects=Project.objects.all()
        serializer=ProjectSerializer(projects,many=True)
        return Response(serializer.data)


@api_view(['GET','POST'])
def all_users(request):
    if request.method =='GET':
        users=User.objects.all()
        serializer=ProfileSerializer(users, many=True)
        return Response(serializer.data)


@login_required
def rate_project(request, id):
    if request.method == "POST":

        project = Project.objects.get(id=id)
        current_user = request.user

        design_rate=request.POST["design"]
        usability_rate=request.POST["usability"]
        content_rate=request.POST["content"]

        Ratings.objects.create(
            project=project,
            user=current_user,
            design_rate=design_rate,
            usability_rate=usability_rate,
            content_rate=content_rate,
            avg_rate=round((float(design_rate)+float(usability_rate)+float(content_rate))/3,2),
        )
        avg_rating= (int(design_rate)+int(usability_rate)+int(content_rate))/3

        project.rate=avg_rating
        project.update_project()

        return render(request, "details.html", {"success": "Project Rated Successfully", "project": project, "rating": Ratings.objects.filter(project=project)})
    else:
        project = Project.objects.get(id=id)
        return render(request, "details.html", {"danger": "Error. Please Reload Your Page and Try again", "project": project})


