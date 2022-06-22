from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register_request,name='register'),
    path("login", views.login_request, name="login"),
    path('logout', views.logout_request, name='logout'),
    path("projects",views.project_list,name='projects'),
    path('search/',views.project_search,name='searchResults'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path("all_users",views.all_users,name='allUsers'),
    path("sub", views.submit_request, name='submit'),
    path("detail/<id>", views.project_detail,name="details"),
    path('ratings/<project_id>', views.rate_project,name='rate_project'),
    
]