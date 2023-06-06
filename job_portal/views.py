from django.shortcuts import render,redirect
from job_portal.models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from mongoengine import Q 
import os
jemail=None



# Create your views here.
def Homepage(request):
    return render(request,"Home_page.html")
def login(request):
    return render(request,"Login_form.html")

def signup(request):
    return render(request,"Signup_form.html")

def loginSeeker(request):
    uemail=request.POST['email']
    upassword=request.POST['password']
    try:
        user_email=userDetails.objects.get(email=uemail)
    except userDetails.DoesNotExist:
        return HttpResponse ("username does not exist")
    try:
        user_password=userDetails.objects.get(password=upassword)
    except userDetails.DoesNotExist:
        return HttpResponse ("password does not exist")
    
    if(user_email == None or user_password == None):
        return render(request,'Login_form.html')
    else:
        global jemail 
        jemail = user_email
        return render(request,'JobSeekar_mainpage.html')
    
def loginManager(request):
    email=request.POST['email']
    password=request.POST['password']
    user_email=ManagerDetails.objects.get(email=email)
    user_password=ManagerDetails.objects.get(password=password)
    if(user_email == None or user_password == None):
        return render(request,'Login_form.html')
    else:
        return render(request,'Manager_mainpage.html',{'role':user_email.role,'company_name':user_email.company_name})

def SignupSeekar(request):
    _username=request.POST['username']
    _email=request.POST['email']
    _password=request.POST['password']
    user_email= userDetails.objects.filter(email=_email)
    if(user_email != None):
        new_user=userDetails(    
        username=_username,
        email=_email,
        password=_password,
        user_fullName=" ",
        user_location=" ",
        user_role=" ",
        user_experience=" ",
        user_education=" ",
        user_jobInterest=" ",
        user_resume=" ",
        )
        new_user.save()
        return render(request,'Acc_creation.html',{'email':_email})
    else:
        return render(request,'Signup_form.html')

def SignupManager(request):
    _email=request.POST['email']
    _password=request.POST['password']
    _role=request.POST['role']
    _company_name=request.POST['company_name']
    M_email=ManagerDetails.objects.filter(email=_email)
    M_cname=ManagerDetails.objects.filter(company_name=_company_name)
    if( M_email != None and M_cname != None):
        new_user=ManagerDetails(  
            email=_email,
            password=_password,
            role=_role,
            company_name=_company_name,
        )
        new_user.save()
        return render(request,'Manager_mainpage.html',{'role':new_user.role,'company_name':new_user.company_name})
    else:
        return render(request,'Signup_form.html')


def accCreate(request):
    _email=request.POST.get('email')
    user=userDetails.objects.filter(email=_email)
    my_model_instance = user.first()
    _user_fullName=request.POST.get('fullname','')
    _user_location=request.POST.get('location','')
    _user_role=request.POST.get('Role','')
    _user_experience=request.POST.get('experience','')
    _user_jobInterest=request.POST.get('Jobtype','')
    _user_education=request.POST.get('education','')
    _user_resume = request.FILES.get('myfile')
    print(_user_resume.name)
    my_model_instance.user_fullName=_user_fullName
    my_model_instance.user_location=_user_location
    my_model_instance.user_experience=_user_experience
    my_model_instance.user_role=_user_role
    my_model_instance.user_education=_user_education
    my_model_instance.user_jobInterest=_user_jobInterest
    filename = os.path.join(settings.MEDIA_ROOT, 'pics', _user_resume.name)
    with open(filename, 'wb') as f:
        f.write(_user_resume.read())
    my_model_instance.user_resume=_user_resume.name
    my_model_instance.save()
    return render(request,'JobSeekar_mainpage.html')

def Job_Available(request):
    job=Jobs.objects.all()
    return render(request,'Job_available.html',{'jobs':job})

def apply(request,cname,crole):
    return render(request,'apply.html',{'cname':cname,'crole':crole})

def Jobsapp(request,cname,crole):
    c_name=request.POST.get("name")
    role = request.POST.get("role")
    user_des=request.POST.get("cover-letter")

    jobapp=Jobapply(
        apply_email=jemail,
        apply_company=c_name,
        apply_role=role,
        apply_des=user_des,
    )
    jobapp.save()
    return redirect('/Job_Available')


def User_dashboard_url(request):
    return HttpResponse(jemail)

def User_edit_profile_url(request):
    prof = userDetails.objects.get(email=jemail)
    return render(request,'Profile.html',{'prof':prof})

def create_job(request,company_name):
    return render(request,'create_job.html',{'cname':company_name})

def Manager_dashboard(request,company_name):
    dis = Jobapply.objects.filter(apply_company=company_name)
    # if dis.count() > 0:
    #     job_apply = dis.first() # get the first Jobapply object in the queryset
    #     user_det = userDetails.objects.get(email=job_apply.apply_email)
    #     return render(request, 'Manager_dashboard.html', {'dis': dis, 'user': user_det})
    # else:
    # handle the case where no Jobapply objects were found
    return render(request, 'Manager_dashboard.html', {'dis': dis})



def Manager_job_status(request):
    return render(request,'create_job.html')

def Manager_edit_job(request):
    return render(request,'create_job.html')

def createJob(request):
    if request.method == "POST":
        cname=request.POST.get("cname")
        role = request.POST.get("role")
        description = request.POST.get("description")
        experience = request.POST.get("experience")
        new_job=Jobs(  
        experience=experience,
        job_description=description,
        recruit_role=role,
        recruit_company=cname,
        )
        new_job.save()
        return HttpResponse("success")
    else:
        return HttpResponse("fail")
