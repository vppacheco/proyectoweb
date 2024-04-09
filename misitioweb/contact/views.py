from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import FormularioContactos
from django.core.mail import EmailMessage
from misitioweb.settings import EMAIL_HOST_USER

def contact(request):  
     if request.method == 'POST':         
        form = FormularioContactos(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #AQUÍ INTRODUCIMOS LOS DATOS DEL ENVÍO DEL MAIL
            email = EmailMessage (
                'Nuevo mensaje de MISITIOWEB', # Asunto
                'De {} <{}>\n\nMensaje:\n\n{}'.format(cd['name'], cd['email'], cd['message']), #Cuerpo
                EMAIL_HOST_USER,# Origen
                ['victorvillagarcia03@gmail.com'],#Destinno
                reply_to=[cd['email']],#email de respuesta
              )
#AQUÍ INTRODUCIMOS EL ENVÍO DEL MAIL
            try:
                email.send()
                #si todo va ok, redireccionamos a ?ok
                return redirect(reverse('contact')+'?ok')
            except:
                #si algo falla, redireccionamos a ?fail
                return redirect(reverse('contact')+'?fail')
     else:
        form = FormularioContactos()
     return render(request, 'contact/contact.html', {'form': form})