from django.shortcuts import render, redirect,get_object_or_404
from .models import User,Ticket
from django.http import HttpResponse 

# Create your views here.
def index(request):
    if request.method== 'POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(name=name,password=password)

        if user:
            return redirect ('home')  

    return render(request,'ticket/index.html')

def home(request):
    if request.method== 'POST':
        from_city=request.POST.get('from_city')
        to_city=request.POST.get('to_city')
        name=request.POST.get('username')
        moblie=request.POST.get('moblie')
        gender=request.POST.get('gender')
        blood_group=request.POST.get('blood_group')
        birth=request.POST.get('birth')
        ticket=Ticket.objects.create(from_city=from_city,to_city=to_city,name=name,moblie=moblie,gender=gender,blood_group=blood_group,birth=birth)

        if ticket:
            return redirect('view_ticket')
    
    return render(request,'ticket/home.html')

def signup(request):
    if request.method=='POST':
        name=request.POST.get('username')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.objects.create(name=name,mobile=mobile,email=email,password=password)
        if user:
            return render(request,'ticket/index.html')
        
    return render(request,'ticket/signup.html')

def view_ticket(request):
    tickets= Ticket.objects.all()
    return render(request,'ticket/view_ticket.html',{'tickets':tickets})

def edit_ticket(request, id):
    ticket=get_object_or_404(Ticket,id=id)
    if request.method== 'POST':
        ticket.from_city=request.POST.get('from_city')
        ticket.to_city=request.POST.get('to_city')
        ticket.name=request.POST.get('username')
        ticket.moblie=request.POST.get('moblie')
        ticket.gender=request.POST.get('gender')
        ticket.blood_group=request.POST.get('blood_group')
        ticket.birth=request.POST.get('birth')
        ticket.save()
        return redirect('view_ticket')
    return render(request,'ticket/edit_ticket.html',{'ticket':ticket})

def delete_ticket(request, id):
    ticket=Ticket.objects.filter(id=id)
    if ticket:
        ticket.delete()
        return redirect('view_ticket')
