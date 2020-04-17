from django.shortcuts import render
from .models import Category, Product, Portfolio
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from .forms import NameForm
from django.http import HttpResponseRedirect

def home(request):
    #tak tworzysz zapytania bazy danych Product.objects.filte ( w filter podajesz jak chchesz odflitrowac)
    #poczytaj sobie o queryset na konczu elemet '[:8]' powoduje pokazanie sie na stronie tylko 8 obiektow z bazy danych
    query_product_first = Product.objects.filter(category_id=1)[:8]
    query_product_second = Product.objects.filter(category_id=2)[:4]

    #UWAGA! tak wlasnie ponizej przekazujesz parametry do szablonu
    context = {'query_product_first': query_product_first,
               'query_product_second': query_product_second,
               'parametr': 'To jest moj parametr z serwera'}
    return render(request, 'app/home.html', context)


def single_product(request, id):
    #tak odbierasz pojedynczy produkt
    #ponizszy linia kodu zabierze produkt o przekazanym id albo zwroci blad 404 jezeli nie istnieje

    single_product = get_object_or_404(Product, pk=id)

    #i tak ponizsza linia kodu przekarzesz produkt do szablonu
    #tam za pomoca template tags obrabiasz go i wyswietlasz sobie dowoli
    context = {'object': single_product,}
    return render(request, 'app/shop-product.html', context)


def services(request):
    return render(request, 'app/services.html', {})

def portfolio(request):
    port = Portfolio.objects.all()
    context = {'obj': port,}
    return render(request, 'app/portfolio.html', context)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'app/contact.html', {'form': form})