#sempre que for criar uma pagina precisa de:
#url - view - template


from django.urls import path, include
from .views import homepage

urlpatterns = [
   path('', homepage),
]
