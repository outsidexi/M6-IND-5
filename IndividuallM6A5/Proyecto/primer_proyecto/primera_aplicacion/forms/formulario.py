from django import forms

class FormularioSupplierForm(forms.Form):
    direccion = forms.CharField(max_length=50, label="Direccion", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su direccion'}))
    area = forms.CharField(label="Area", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su area'}))
    producto = forms.CharField(max_length=50, label="Producto", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su producto'}))
    
class FormularioUsuarioForm(forms.Form):
    direccion = forms.CharField(max_length=50, label="Direccion", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su direccion'}))
    edad = forms.IntegerField(label="Edad", required=True, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Ingrese su edad'}))
    profesion = forms.CharField(max_length=50, label="Profesion", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su profesion'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Usuario", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su usuario'}),
                               error_messages={'required': 'El Usuario es requerida'})
    password = forms.CharField(max_length=20, label="Contraseña", required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingrese su contraseña'}),
                               error_messages={'required': 'La contraseña es requerida'})