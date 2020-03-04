from django.shortcuts import render, redirect
from .models import Posting
from django.utils import timezone

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def hospital(request):
    return render(request, 'hospital.html')

def patient(request):

    testdata = {
        "name" : "1번 환자",
        "paths" : ['37.25400, 126.59302', '37.23374, 126.55239', '37.012345, 127.259493'],
        "mapid" : 1
    }
    data = [
        testdata
    ]

    return render(request, 'patient.html', {
        'data' : data,
    })

def virus(request):
    
    return render(request, 'virusinfo.html')

def community(request):
    Posts = Posting.objects.all()
    return render(request, 'community.html',{
        'Posts' : Posts,
    })

def detail(request, id):
    Post = Posting.objects.get(id=id)
    return render(request, 'detail.html',{
        'Post' : Post,
    })

def create_posting(request):

    if(request.method == "GET"):
        return render(request, 'posting.html')

    elif(request.method == 'POST'):
        _useremail = request.POST.get('email')
        _title = request.POST.get('title')
        _content = request.POST.get('content')
        _updated_at = timezone.datetime.now()

        new_posting = Posting.objects.create(
            useremail = _useremail,
            title = _title,
            content = _content,
            updated_at = _updated_at
        )

        return redirect('/community')