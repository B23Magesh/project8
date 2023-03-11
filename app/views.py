from django.shortcuts import render

# Create your views here.
def Sample(request):
    return render(request,'index.html')
def Super(request):
    return render(request,'Super.html')