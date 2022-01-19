from django.shortcuts import  render
from django.shortcuts import  redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import NewConnection, BookGas
import datetime

def index(request):
  return render(request,'index.html')

def about(request):
  with open('home//static//About.txt') as f:
    f = f.read()
    f = f.split("|")
  about={'h1':f[0],'p1':f[1],'h2':f[2],'p2':f[3],'h3':f[4],'p3':f[5],'extra':None}
  return render(request,'about.html',about)

def tnc(request):
  with open('home//static//tnc.txt') as m:
    m = m.read()
    m = m.split('|')
    tnc={}
    for i in range(14):
      tnc["l{0}".format(i+1)] = m[i]
  return render(request,'tnc.html',tnc)

def register(request):
  if request.method=='POST':
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        psw1 = request.POST['psw1']
        psw2 = request.POST['psw2']        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('register')        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('register')        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('register')       
        if psw1 != psw2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('register')       
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('register')
        myuser = User.objects.create_user(username, email, psw1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
    return redirect('login')   
  return render(request,'register.html')


def log_in(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['psw']
    user = authenticate(username=username,password=password)
    if user is not None:
      login(request, user)
      fname = user.first_name
      messages.success(request, "Logged In Sucessfully!!")
      return render(request, "home.html",{"fname":fname})
    else:
      messages.error(request, "Bad Credentials!!")
      return redirect('login')
  return render(request, "login.html")
  

def log_out(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('index')
  else:
    return redirect('login')

def newc(request):
  if request.user.is_authenticated:
    if request.method=="POST":
      uname = request.user
      fname = request.POST['fname']
      lname = request.POST['lname']
      phoneno = request.POST['phoneno']
      email = request.POST['email']
      gender = request.POST['gender']
      aadhaar = request.POST['aadhaar']
      address = request.POST['address']
      zipcode = request.POST['zip']
      payopt = request.POST['payoption']
      newc = NewConnection(user=uname,fname=fname,lname=lname,phoneno=phoneno,email=email,gender=gender,aadhaar=aadhaar,address=address,zipcode=zipcode,paymentOption=payopt)
      newc.save()
      return redirect('bookgas')
    uname = request.user.username
    fname = request.user.first_name
    lname = request.user.last_name
    email = request.user.email
    return render(request,'NewConnection.html',{"uname":uname,'fname':fname,'lname':lname,'email':email})
  else:
    return redirect('login')
  
def bookgas(request):
  if request.user.is_authenticated:
    user = request.user
    try:
      data = NewConnection.objects.get(user=user)
      #data2 = BookGas.objects.get(user=user)
      fname = data.fname
      lname = data.lname
      address = data.address
      phoneno = data.phoneno
      name = fname +" "+ lname
     # billnum = data2.id
      dt = datetime.datetime.now()
      tdate = str(dt.day)+'-'+str(dt.month)+'-'+str(dt.year)
      expdate = str(dt.day+2)+'-'+str(dt.month)+'-'+str(dt.year)
      dict1 = {'name':name,'address':address,'date':tdate,'phoneno':phoneno,'alert':' '}
      if request.method =="POST":
        if request.POST.get('cylinder') is not None:
          gctype = request.POST.get('cylinder')
        else:
          gctype = '7.8kg'
      if request.POST.get('book'):
        bookgas = BookGas(user=user,gctype=gctype,accname = name,billdate=tdate,expctdate=expdate,amount='900')
        bookgas.save()
        return redirect('pay')
    except:
      dict1 = {'name':" ",'address':" ",'date':" ",'phoneno':" ",'alert':'You do not have any gas connection.'}
    return render(request,'BookGas.html',dict1)
  else:
    return redirect('login')

def pay(request):
  if request.user.is_authenticated:
    if request.method=='GET':
      return render(request,'success.html')
    return render(request,'pay.html')
  else:
    return redirect('login')


def delivery(request):
  if request.user.is_authenticated:
    context = {'query':BookGas.objects.filter(user=request.user).exclude(status = 'delivered')}
    return render(request,'delivery.html',context)
  else:
    return redirect('login')  

def billhistory(request):
  if request.user.is_authenticated:
    query = BookGas.objects.filter(user=request.user).filter(status = 'delivered')
    
    context={"data":query}
    return render(request, 'billhistory.html', context)
  else:
    return redirect('login')