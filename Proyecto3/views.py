from django.http import HttpResponse

# a cada función creada en este archivo views en django se le llama vista
def saludo(request):

    return HttpResponse("Hola Gabriel Rezqallah Django")