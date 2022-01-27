
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.base import TemplateView
from User.models import Usuario
from django.contrib.auth import *
from django.shortcuts import redirect, render
from Login.form import resetPasswordForm
from django.contrib.auth.views import * 
from django.contrib.auth.mixins import *
from django.contrib.auth.forms import *
from django.views.generic.edit import FormView
from django.template.loader import render_to_string
from academia21.settings import *
import uuid
from academia21.settings import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Create your views here.
class Login(LoginView):
    template_name = 'login.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)
class resetPassword(FormView):
    form_class = resetPasswordForm
    template_name = 'reset.html'
    success_url = '/login/'
    def SendMail(self, id, email):
        try:
            To = email
            Subject = 'Reestablecer contraseña'
            Body = "Restaurar contraseña"
            password = uuid.uuid4()
            mailServer = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
            print(mailServer.ehlo())
            mailServer.starttls()
            print(mailServer.ehlo())
            mailServer.login(EMAIL_HOST_USER,EMAIL_HOST_PASSWORD)
            mensaje = MIMEMultipart()
            mensaje['From'] = EMAIL_HOST_USER
            mensaje['To'] = To
            mensaje['Subject'] = Subject
            content = render_to_string('email.html', {'user' :  Usuario.objects.get(pk = id), 'password' : password})
            mensaje.attach(MIMEText(content, 'html'))
            mailServer.sendmail(EMAIL_HOST_USER, To ,mensaje.as_string())
            update = Usuario.objects.get(pk = id)
            update.token = password
            update.save()
        except Exception as e:
            print('Error al enviar email : ', e)


    def post(self, request, *args, **kwargs):
        try:
            usuario = ''
            username = ''
            email = ''
            try:
                username = request.POST['username']
                email = request.POST['email']
            except Exception as e:
                print('Sin datos ln-61: ', e)
    
            if username and email:
                usuario = Usuario.objects.filter(username = username).exists()
            if usuario:
                usuario = Usuario.objects.get(username = username)
                if email == usuario.email:
                    self.SendMail(usuario.pk, usuario.email)
                    print('Se cae aquí')
                    return render(request, 'login.html', {'success': 'Email enviado correctamente, porfavor, revise su bandeja de entrada'})
                    # return render(self.success_url)
                else:
                    print('Email incorrecto')
                    return render(request= request, template_name='reset.html',context= {'form': self.form_class, 'errorf': 'Email incorrecto'})
            else:
                print('Usuario no existe')
                return render(request, self.template_name, {'form': self.form_class, 'errorf': 'Usuario no registrado'})
        except Exception as e:
            print('Error ln-73: ', e)
            # return super().post(request, *args, **kwargs)

class updatePassword(TemplateView):
    template_name = 'update.html'
    def get(self, request, *args, **kwargs):
        try:
            token = self.kwargs['token']
            user = Usuario.objects.filter(token = token).exists()
            if user:
                return super().get(request, *args, **kwargs)
            else:
                return redirect('/login/')
        except Exception as e:
            print('Error ln-80: ', e)
            return redirect('/login/')
    def post(self, request, *args, **kwargs):
        try:
            token = self.kwargs['token']
            user = Usuario.objects.get(token = token)
            psw = request.POST['password']
            psw1 = request.POST['password1']
            if psw == psw1:
                user.password = psw
                user.token = ''
                user.save()
                return redirect('/login/')
                
            else:
                return render(request, self.template_name, {'errorp': 'Las contraseñas no coinciden'})
        except Exception as e:
            print('Error ln-97: ', e)
        return redirect('/login/')


class changePassword( LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    success_url = '/login/'
    template_name = 'password.html'
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)
