from django.shortcuts import render
from StoreApp.models import Departamento, Produto
from StoreApp.forms import CadrastroForm
from StoreApp.forms import ContatoForm

# Create your views here.
def index(request): 
    produto_destaque = Produto.objects.filter(destaque = True)

    context = {
        'produtos' : produto_destaque
    }
    
    return render(request, 'index.html', context)

def produto_lista(request):
    produtos_lista = Produto.objects.all()

    context = {
        'produtos' : produtos_lista,
        'titulo' : 'Cantores Para Venda:'
    }
    return render(request, 'produtos.html', context)

def produto_detalhe(request, id):
    produto = Produto.objects.get(id = id)
    produtos_relacionados = Produto.objects.filter(departamento_id = produto.departamento).exclude(id = id)[:4]

    context = {
        'produto' : produto,
        'produtos_relacionados' : produtos_relacionados
    }
    return render(request, 'produto_detalhes.html', context)

def produto_lista_por_departamento(request, id):
    produtos_lista = Produto.objects.filter(departamento_id = id)
    departamento = Departamento.objects.get(id = id)
    context = {
        'produtos' : produtos_lista,
        'titulo' : departamento.nome
    }
    return render(request, 'produtos.html', context)

def sobre_empresa(request):
    return render (request, 'sobre_empresa.html')

def cadastro(request):

    mensagem = "" # armazenar mensagem de sucesso ou erro

    # se o formulario foi submetido
    if request.method == 'POST':
        formulario = CadrastroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario = CadrastroForm()
            mensagem = "Cliente cadastrado com sucesso :)"
        else:
            mensagem = "Verifique erros abaixo: "
 

    
    
    
    #  se o formulario nãao foi submetido. Entrei na pag. pelo menu
        # o form deve vir vazio
        
    else:
        formulario = CadrastroForm()

    formulario = CadrastroForm()

    context = {
        'formulario_cadastro' : formulario,
        'mensagem' : mensagem
        
    }
    return render (request, 'cadastro.html', context)

def contato(request): 

    mensagem = ''
    formulario = ContatoForm()

    context = {
        'mensagem' : mensagem,
        'formulario_contato' : formulario
    }
    return render(request, 'contato.html', context)
