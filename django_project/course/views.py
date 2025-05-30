from django.shortcuts import render

# Create your views here.

def learn_django(req):
    course_name={'cname':'django'}
    #return render(req, 'course/django.html',context=course_name)
    #return render(req, 'course/django.html',{'cname':'Python'})
    return render(req, 'course/django.html',course_name)


def learn_fastAPI(req):
    return render(req, 'course/fastapi.html')
