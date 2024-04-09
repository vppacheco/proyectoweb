from django import forms
class FormularioContactos(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label = "Email", required=True)
    message = forms.CharField(label = "Contenido", required=True, widget=forms.Textarea())