from django.urls import path
from django.conf.urls.static import static
from .views import *
from django.conf import settings

urlpatterns = [
        path('',home,name='home'),
        path('aboutus/',about,name='aboutus'),
        path('contactus/',contact,name='contactus'),
        path('signup/',signup,name='signup'),
        path('login/',user_login,name='login'),
        path('display/',display,name='display'),
        path('delete/<int:id>/', delete, name='delete'),
        path('update/<int:id>/',update,name='update'),
        path('adminhome/',admin,name='adminhome'),
        path('dashboard/',dashboard,name='dashboard'),
        # path('products',products,name='products'),
        path('addproduct/',add_product,name='addproduct'),
        path('displayproducts/',display_products,name='displayproducts'),
        # path('demo1',demo1,name='demo1'),
        path('payments/',payments,name='payments'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)