from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.-----------------------------------
class Homepage(TemplateView):
    template_name = "homepage.html"

class Homefilmes(LoginRequiredMixin, ListView):#vai exibir lista de filmes do banco dados
    template_name = "homefilmes.html"
    model = Filme
    # object_list ->lista de itens do modelo

#classe que vai mostrar os detalhes dos filmes
class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # objec -> 1 item do nosso modelo

#funcao que faz a contagem de acessos
    def get(self,request, *args, **kwargs):
        #descobrir qual filme ele esta acessando
        filme = self.get_object()
        #somar +1 nas visualizacoes daquele filme
        filme.visualizacoes += 1
        #salvar
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super(Detalhesfilme, self).get(request, *args, **kwargs)#redireciona o usuario para a URL final


    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        #filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a do filme da página(object)
        # self.get_object()
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return  context

#pagina construida dentro de filme/templates
class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    #função que vai filtrar o curso pelo nome
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None


#def homepage(request):     #template
#  return render(request, "homepage.html")


# url - view - html
#def homefilmes(request): #funcao homefilmes---------------------
#    context = {}
#    lista_filmes = Filme.objects.all()
#    context['lista_filmes'] = lista_filmes
#    return render(request, "homefilmes.html", context)
