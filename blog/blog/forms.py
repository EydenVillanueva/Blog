from django import forms

#Formulario de contacto
class ContactoForm(forms.Form):

    asunto = forms.CharField()
    nombre = forms.CharField(required=True)
    email = forms.EmailField()
    #Por parámetro le estamos especificando a forms.CharField que la casilla que se presentará será mas grande
    mensaje = forms.CharField(widget=forms.Textarea)


    #Dato que necesitamos enviar un email con estos datos debemos de separar las cadenas de los campos email
    def formato_email(self):
        try:
            #Me devuelve el campo email
            email = self.cleaned_data.get('email')
            #Separamos las partes del email
            email_base, proveedor = email.split('@')
            #Separamos el dominio del email de la extensión de este
            dominio, extension = proveedor.split('.')

        except ValueError:
            print('Hubo un error en el email')

        return email
