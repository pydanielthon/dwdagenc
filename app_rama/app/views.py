from django.shortcuts import render
from .models import Portfolio
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactForm
def home(request):
    portf = Portfolio.objects.all()[:3]


    return render(request, 'app/home.html', {'portf': portf})

def services(request):
    return render(request, 'app/services.html', {})

def portfolio(request):
    port = Portfolio.objects.all()
    context = {'obj': port,}
    return render(request, 'app/portfolio.html', context)
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['czerepak183@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('/')

    return render(request, 'app/contact.html', {
        'form': form_class,
    })