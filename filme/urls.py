#sempre que for criar uma pagina precisa de:
#url - view - template


from django.urls import path, include
from .views import Homefilmes, Homepage, Detalhesfilme, Pesquisafilme

app_name='filme'


#criando url das paginas
urlpatterns = [
   path('', Homepage.as_view(), name='homepage'),
   path('filmes/', Homefilmes.as_view(), name='homefilmes'),
   path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),
   path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme')
]
