from django.db import models
import mongoengine as me
from mongoengine import ObjectIdField
from bson import ObjectId

# Create your models here.
class userDetails(me.Document):
    username=me.StringField(required=True)
    email=me.StringField(required=True)
    password=me.StringField(required=True)
    user_fullName=me.StringField(required=True)
    user_location=me.StringField(required=True)
    user_role=me.StringField(required=True)
    user_experience=me.StringField(required=True)
    user_education=me.StringField(required=True)
    user_jobInterest=me.StringField(required=True)
    user_resume=me.StringField(required=True)

class ManagerDetails(me.Document):
    email=me.StringField(required=True)
    password=me.StringField(required=True)
    role=me.StringField(required=True)
    company_name=me.StringField(required=True)

class Jobs(me.Document):
    recruit_company=me.StringField(required=True)
    recruit_role=me.StringField(required=True)
    job_description =me.StringField(required=True)
    experience=me.StringField(required=True)

class Jobapply(me.Document):
    apply_email=me.StringField(required=True)
    apply_company=me.StringField(required=True)
    apply_role=me.StringField(required=True)
    apply_des=me.StringField(required=True)



