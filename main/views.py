from django.shortcuts import render
#render:mainpage.html을 전송하는 함수
# Create your views here.
def showmain(request):
    return render(request,'main/mainpage.html')
#Request: main폴더 안의 mainpage.html 요청

def showmain2(request):
    return render(request, 'main/show.html')

def first(request):
    return render(request, 'main/first.html')

def second(request):
    return render(request, 'main/second.html')

def third(request):
    return render(request, 'main/third.html')

def fourth(request):
    return render(request, 'main/fourth.html')