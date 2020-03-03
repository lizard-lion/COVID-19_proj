from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def hospital(request):
    return render(request, 'hospital.html')

def map(request):

    testdata = {
        "name" : "1번 환자",
        "paths" : ['37.25400, 126.59302', '37.23374, 126.55239', '37.012345, 127.259493'],
        "mapid" : 1
    }
    data = [
        testdata
    ]

    return render(request, 'map.html', {
        'data' : data,
    })

def virus(request):
    return render(request, 'virus.html')