from django.shortcuts import render

def index(request):
     return render(request, 'index.html')

def usuarios(request):
     lista_de_usuarios = [
          {"nome": "Amanda",
           "matrícula": "200118",
           "idade": 30,
           "cidade": "Bom Jesus"},

            {"nome": "Gabriely",
           "matrícula": "204144",
           "idade": 18,
           "cidade": "Bom Jesus"},

            {"nome": "Almira",
           "matrícula": "201112",
           "idade": 22,
           "cidade": "Natal"},

            {"nome": "Jorge",
           "matrícula": "201667",
           "idade": 19,
           "cidade": "Bom Jesus"},

            {"nome": "João Victor",
           "matricula": "206121",
           "idade": 20,
           "cidade": "Bom Jesus"},
     ]
     return render(request, 'usuarios.html',{'usuarios': lista_de_usuarios})