from django.urls import path
from . import views

urlpatterns=[
    path('',views.Homepage,name='Homepage'),
    path('login',views.login,name='login_form'),
    path('signup',views.signup,name='signup_form'),
    path('loginSeeker',views.loginSeeker,name='login'),
    path('loginManager',views.loginManager,name='loginManager'),
    path('accCreate',views.accCreate,name='accCreate'),
    path('SignupSeeker',views.SignupSeekar,name='signup'),
    path('SigupManager',views.SignupManager,name='SignupManager'),
    path('Job_Available',views.Job_Available,name='Job_Available'),
    path('apply/<str:cname>/<str:crole>/Jobsapp',views.Jobsapp,name='Jobsapp'),
    path('apply/<str:cname>/<str:crole>/',views.apply,name='apply'),
    path('User_dashboard_url',views.User_dashboard_url,name='User_dashboard_url'),
    path('User_edit_profile_url',views.User_edit_profile_url,name='User_edit_profile_url'),
    path('create_job/<str:company_name>/)', views.create_job, name='create_job_url'),
    path('Manager_dashboard_url/<str:company_name>/', views.Manager_dashboard, name='Manager_dashboard_url'),
    path('Manager_job_status_url', views.Manager_job_status, name='Manager_job_status_url'),
    path('Manager_edit_job_url', views.Manager_edit_job, name='Manager_edit_job_url'),
    path('createJob',views.createJob,name='createJob')
    ]