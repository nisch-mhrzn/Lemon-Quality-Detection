from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is our home page")
    return render(request,"index.html")
    
def about(request):
    return HttpResponse("This is our about page")

def contact(request):
    return HttpResponse("This is our contact page")
