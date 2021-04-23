from django.urls import path

from store.views import home, cart, login,signup,orders,signout, showproduct

urlpatterns = [
   path('' , home , name='homepage'),
   path('cart/' , cart , name='cart'),
   path('login/' , login , name='login'), 
   path('signup/' , signup , name='signup'),
   path('orders/' , orders , name='orders'),
   path('logout/' , signout , name='logout'),
   path('product/<int:id>' , showproduct,name="showproduct"),  

]