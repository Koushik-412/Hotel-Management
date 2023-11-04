from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contactus.html')

def about(request):
    return render(request,'aboutus.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Create a new User instance and save it to the database
        new_user = User(username=username, email=email, password=password)
        new_user.save()

        # Redirect to a success page or any other page after successful signup
        return HttpResponse('Registered Succesfully')  # Change 'success_page' to the name of your success page URL pattern

    return render(request, 'signup.html')




def user_login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']

        flag=User.objects.filter(Q(username=username) & Q(password=password))

        print(flag)

        if flag:
            user=User.objects.get(username=username)
            print(user)
            request.session["uname"]=user.username
            products = Product.objects.all()  # Fetch all products from the database
            return render(request, 'displayproducts.html', {"uname":user.username,"products":products})
        elif username=="admin" and password=="admin":
            return render(request,"adminhome.html")
        else:
            return HttpResponse('Login Failed')
    return render(request, 'login.html')


def display(request):
    users=User.objects.all()

    context={
        'users':users
    }

    return render(request,"display.html",context)

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('display'))

def update(request,id):
    user=User.objects.get(id=id)

    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        return redirect('display')

    return render(request,"update.html",{'user':user})

def admin(request):
    return render(request,"adminhome.html")

def dashboard(request):
    return render(request,"dashboard.html")

def products(request):
    return render(request,"products.html")




from django.shortcuts import render, redirect
from .models import Product
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES['image']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT + '/productimages/')
        filename = fs.save(image.name, image)
        image_url = fs.url(filename)
        new_product = Product(name=name, description=description, price=price, image=image_url)
        new_product.save()
        return HttpResponse("Added Succesfully")
    return render(request, 'addproduct.html')



def display_products(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'displayproducts.html', {'products': products})


def payments(request):
    return render(request,"payments.html")






