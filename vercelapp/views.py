from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def output(request):
    num1=request.GET['num1']
    num2=request.GET['num2']
    num3=int(num1)+int(num2)
    return render(request,'index.html',{'num3':num3})
