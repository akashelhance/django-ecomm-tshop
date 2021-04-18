from django.urls import path

from store.views import home, cart, login,signup,orders

urlpatterns = [
   path('' , home , name='homepage'),
   path('cart/' , cart , name='cart'),
   path('login/' , login , name='login'), 
   path('signup/' , signup , name='signup'),
   path('orders/' , orders , name='orders'),  

   
      

]