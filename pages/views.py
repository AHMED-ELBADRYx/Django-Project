from django.shortcuts import render
from .models import Login
from .forms import LoginForm, LoginModelForm
# Create your views here.

def home(request):
    return render(request, 'pages/home.html',{
        'content': "Welcome to the home page!",
        'logs_names': '<br>'.join([log.name for log in Login.objects.all()]),
    })

def about(request):
    return render(request, 'pages/about.html', {
        'content': f'Welcome to the About Page! We are a team of passionate developers building awesome projects.',
    })

def contact(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     message = request.POST.get('message')
    #     data = Login(name=name, email=email, password=password, message=message)
    #     data.save()
    #     return render(request, 'pages/contact.html', {
    #         'l': LoginForm(),
    #         'lf': LoginModelForm(),
    #         'success_message': 'Thank you for your message! We will get back to you soon.',
    #     })
    if request.method == 'POST':
        
        form = LoginModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/contact.html', {
                'l': LoginForm(),
                'lf': LoginModelForm(),
                'success_message': 'Thank you for your message! We will get back to you soon.',
            })
    else:
        form = LoginModelForm()
    return render(request, 'pages/contact.html', {
        'l': LoginForm(),
        'lf': LoginModelForm(),
    })
