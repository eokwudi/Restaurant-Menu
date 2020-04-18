from .models import RegularPizza, SicilianPizza, Subs, Pasta, Salads, Parm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
import stripe
import os

STRIPE_API = os.getenv("STRIPE_API")
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "orders/choose.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, "orders/choose.html")
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

# Access options for the different types of pizza
def to_pizza(request):
    return render(request, "orders/pizza_options.html")

# All the direct_ functions were needed as a redirect to the
# desired page due to javascript automatically trying to load any
# webpage regardless of whether there is a forom to full or not
def direct_cheese(request):
    return render(request, "orders/cheese.html")

def cheese(request):
    type = request.POST.get("type")
    length = request.POST.get("size")
    if type == "Regular" and length == "Small":
        regularpizza = RegularPizza (
        user = request.user,
        firstTop = "Cheese",
        secondTop = "None",
        thirdTop = "None",
        size = length,
        price = 12.70
        )
        regularpizza.save()
    if type == "Regular" and length == "Large":
        regularpizza = RegularPizza (
        user = request.user,
        firstTop = "Cheese",
        secondTop = "None",
        thirdTop = "None",
        size = length,
        price = 17.95
        )
        regularpizza.save()
    if type == "Sicilian" and length == "small":
        sicilianpizza = SicilianPizza (
        user = request.user,
        firstTop = "Cheese",
        secondTop = "None",
        thirdTop = "None",
        size = length,
        price = 24.45
        )
        sicilianpizza.save()
    if type == "Sicilian" and length == "large":
        sicilianpizza = SicilianPizza (
        user = request.user,
        firstTop = "Cheese",
        secondTop = "None",
        thirdTop = "None",
        size = length,
        price = 38.70
        )
        sicilianpizza.save()

    '''
    Add to shopping cart
    '''
    return render(request, "orders/choose.html", {"message": "Order Added!"})

# Takes you to ingredients list for special pizza
def direct_special(request):
    return render(request, "orders/special.html")

def special(request):
    type = request.POST.get("type")
    length = request.POST.get("size")
    if type == "Regular" and length == "Small":
        regularpizza = RegularPizza (
        user = request.user,
        firstTop = "Special",
        secondTop = "None",
        thirdTop = "None",
        size = length,
        price = 12.70
        )
        regularpizza.save()
    if type == "Regular" and length == "Large":
        regularpizza = RegularPizza (
        user = request.user,
        firstTop = "Special",
        secondTop = "None",
        thirdTop = "None",
        size = length,
        price = 17.95
        )
        regularpizza.save()
    if type == "Sicilian" and length == "Small":
        sicilianpizza = SicilianPizza (
        user = request.user,
        firstTop = "Special",
        secondTop = "None",
        thirdTop = "None",
        size = length,
        price = 24.45
        )
        sicilianpizza.save()
    if type == "Sicilian" and length == "Large":
        sicilianpizza = SicilianPizza (
        user = request.user,
        firstTop = "Special",
        secondTop = "None",
        thirdTop = "None",
        size = length,
        price = 38.70
        )
        sicilianpizza.save()
    '''
    Add to shopping cart
    '''
    return render(request, "orders/choose.html", {"message": "Order Added!"})

def direct_pizza(request):
    return render(request, "orders/custom.html")

def create_pizza(request):
    type = request.POST.get("type")
    length = request.POST.get("size")
    first = request.POST.get("first")
    second = request.POST.get("second")
    third = request.POST.get("third")

    if first == "None":
        return render(request, "orders/custom.html")
    if type == "Regular" and second == "None" and third == "None" and length == "Small":
        regularpizza = RegularPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 13.70
        )
        regularpizza.save()
    elif type == "Regular" and second == "None" and third == "None" and length == "Large":
        regularpizza = RegularPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 19.95
        )
        regularpizza.save()
    if type == "Regular" and second != "None" and third == "None" and length == "Small":
        regularpizza = RegularPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 15.20
        )
        regularpizza.save()
    elif type == "Regular" and second != "None" and third == "None" and length == "Large":
        regularpizza = RegularPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 21.95
        )
        regularpizza.save()
    if type == "Regular" and second != "None" and third != "None" and length == "Small":
        regularpizza = RegularPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 16.20
        )
        regularpizza.save()
    elif type == "Regular" and second != "None" and third != "None" and length == "Large":
        regularpizza = RegularPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 23.95
        )
        regularpizza.save()
    if type == "Sicilian" and second == "None" and third == "None" and length == "Small":
        sicilianpizza = SicilianPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 26.45
        )
        sicilianpizza.save()
    elif type == "Sicilian" and second == "None" and third == "None" and length == "Large":
        sicilianpizza = SicilianPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 40.70
        )
        sicilianpizza.save()
    if type == "Sicilain" and second != "None" and third == "None" and length == "Small":
        sicilianpizza = SicilianPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 28.45
        )
        sicilianpizza.save()
    elif type == "Sicilian" and second != "None" and third == "None" and length == "Large":
        sicilianpizza = SicilianPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 42.70
        )
        sicilianpizza.save()
    if type == "Sicilian" and second != "None" and third != "None" and length == "Small":
        sicilianpizza = SicilianPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 29.45
        )
        sicilianpizza.save()
    elif type == "Sicilian" and second != "None" and third != "None" and length == "Large":
        sicilianpizza = SicilianPizza (
        user = request.user,
        firstTop = first,
        secondTop = second,
        thirdTop = third,
        size = length,
        price = 44.70
        )
        sicilianpizza.save()
    return render(request, "orders/choose.html", {"message": "Order Added!"})

def direct_sub(request):
    return render(request, "orders/sandwich.html")

def create_sub(request):
    type = request.POST.get("type")
    length = request.POST.get("size")
    mush = request.POST.get("mushroom")
    clove = request.POST.get("onion")
    pepp = request.POST.get("peppers")
    dairy = request.POST.get("cheese")

    #Need to convert incoming numbers to allow for decimals
    mush = float(mush)
    clove = float(clove)
    pepp = float(pepp)
    dairy = float(dairy)

    if type == "Chicken Parmigiana":
        if length == "Small":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 7.50 + dairy
            )
            sub.save()
        if length == "Large":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 8.50 + dairy
            )
            sub.save()
    elif type == "Steak":
        if length == "Small":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = mush,
            onion = clove,
            pepper = pepp,
            cheese = dairy,
            price = 6.50 + mush + clove + dairy + pepp
            )
            sub.save()
        if length == "Large":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = mush,
            onion = clove,
            pepper = pepp,
            cheese = dairy,
            price = 7.95 + mush + clove + dairy + pepp
            )
            sub.save()
    elif type == "Cheese":
         if length == "Small":
             sub = Subs (
             user = request.user,
             flavor = type,
             size = length,
             mushroom = 0,
             onion = 0,
             pepper = 0,
             cheese = dairy,
             price = 7.50 + dairy
             )
             sub.save()
         if length == "Large":
             sub = Subs (
             user = request.user,
             flavor = type,
             size = length,
             mushroom = mush,
             onion = clove,
             pepper = pepp,
             cheese = dairy,
             price = 8.50 + dairy
             )
             sub.save()
    elif type == "Steak + Cheese":
        if length == "Small":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = mush,
            onion = clove,
            pepper = pepp,
            cheese = dairy,
            price = 6.95 + mush + clove + dairy + pepp
            )
            sub.save()
        if length == "Large":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = mush,
            onion = clove,
            pepper = pepp,
            cheese = dairy,
            price = 8.50 + mush + clove + dairy + pepp
            )
            sub.save()
    elif type == "Sausage, Peppers, Onions":
        if length == "large":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 8.50 + dairy
            )
            sub.save()
    elif type == "Hamburger":
        if length == "Small":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 4.60 + dairy
            )
            sub.save()
        if length == "Large":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 6.95 + dairy
            )
            sub.save()
    elif type == "Cheeseburger":
        if length == "Small":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 9,
            cheese = dairy,
            price = 5.10 + dairy
            )
            sub.save()
        if length == "Large":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 7.45 + dairy
            )
            sub.save()
    elif type == "Fried Chicken":
        if length == "Small":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 6.95
            )
            sub.save()
        if length == "Large":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 8.50 + dairy
            )
            sub.save()
    elif type == "Veggie":
        if length == "Small":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 6.95 + dairy
            )
            sub.save()
        if length == "Large":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 8.50 + dairy
            )
            sub.save()
    else:
        if length == "Small":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 6.50 + dairy
            )
            sub.save()
        if length == "Large":
            sub = Subs (
            user = request.user,
            flavor = type,
            size = length,
            mushroom = 0,
            onion = 0,
            pepper = 0,
            cheese = dairy,
            price = 7.95 + dairy
            )
            sub.save()
    return render(request, "orders/choose.html", {"message": "Order Added!"})

def direct_pasta(request):
    return render(request, "orders/pasta_create.html")

def create_pasta(request):
    type = request.POST.get("type")
    if type == "Mozarella":
        pasta = Pasta (
        user = request.user,
        flavor = type,
        price = 6.50
        )
        pasta.save()
    if type == "Meatballs":
        pasta = Pasta (
        user = request.user,
        flavor = type,
        price = 8.75
        )
        pasta.save()
    if type == "Chicken":
        pasta = Pasta (
        user = request.user,
        flavor = type,
        price = 9.75
        )
        pasta.save()
    return render(request, "orders/choose.html", {"message": "Order Added!"})

def direct_salad(request):
    return render(request, "orders/salad_create.html")

def create_salads(request):
    type = request.POST.get("type")
    if type == "Garden":
        salads = Salads(
        user = request.user,
        flavor = "Garden",
        price = 6.25
        )
        salads.save()
    else:
        salads = Salads (
        user = request.user,
        flavor = type,
        price = 8.25
        )
        salads.save()
    return render(request, "orders/choose.html", {"message": "Order Added!"})

def direct_platter(request):
    return render(request, "orders/create_platter.html")

def create_platter(request):
    type = request.POST.get('type')
    length = request.POST.get('size')
    if type == "Garden" and length == "Small":
        salads = Salads (
        user = request.user,
        flavor = type,
        price = 40.00,
        size = length,
        )
        salads.save()
    if type == "Garden" and length == "Large":
        salads = Salads (
        user = request.user,
        flavor = type,
        price = 65.00,
        size = length,
        )
        salads.save()
    if type == "Greek" and length == "Small":
        salads = Salads (
        user = request.user,
        flavor = type,
        price = 50.00,
        size = length,
        )
        salads.save()
    if type == "Greek" and length == "Large":
        salads = Salads (
        user = request.user,
        flavor = type,
        price = 75.00,
        size = length,
        )
        salads.save()
    if type == "Antipasto" and length == "Small":
        salads = Salads (
        user = request.user,
        flavor = type,
        price = 50.00,
        size = length,
        )
        salads.save()
    if type == "Antipasto" and length == "large":
        salads = Salads (
        user = request.user,
        flavor = type,
        price = 75.00,
        size = length,
        )
        salads.save()
    if type == "Baked" and length == "Small":
        pasta = Pasta (
        user = request.user,
        flavor = type,
        price = 40.00,
        size = length,
        )
        pasta.save()
    if type == "Baked" and length == "Large":
        pasta = Pasta (
        user = request.user,
        flavor = type,
        price = 65.00,
        size = length,
        )
        pasta.save()
    if type == "Meatball" and length == "Small":
        parm = Parm (
        user = request.user,
        flavor = type,
        price = 50.00,
        size = length,
        )
        parm.save()
    if type == "Meatball" and length == "Large":
        parm = Parm (
        flavor = type,
        price = 75.00,
        size = length,
        )
        parm.save()
    if type == "Chicken" and length == "Small":
        parm = Parm (
        user = request.user,
        flavor = type,
        price = 55.00,
        size = length,
        )
        parm.save()
    if type == "Chicken" and length == "Large":
        parm = Parm (
        user = request.user,
        flavor = type,
        price = 85.00,
        size = length,
        )
        parm.save()
    return render(request, "orders/choose.html", {"message": "Order Added!"})

def cart(request):
    context = {
    "classics": RegularPizza.objects.filter(user=request.user),
    "varieties": SicilianPizza.objects.filter(user=request.user),
    "sandwiches": Subs.objects.filter(user=request.user),
    "pastas": Pasta.objects.filter(user=request.user),
    "veggies": Salads.objects.filter(user=request.user),
    "parmigiana": Parm.objects.filter(user=request.user),
    }
    return render(request, "orders/list.html", context)

# See items with total price calculation
def items(request):
    classics = RegularPizza.objects.filter(user=request.user)
    varieties = SicilianPizza.objects.filter(user=request.user)
    sandwiches = Subs.objects.filter(user=request.user)
    pastas = Pasta.objects.filter(user=request.user)
    veggies = Salads.objects.filter(user=request.user)
    parmigiana = Parm.objects.filter(user=request.user)
    total = 0
    for classic in classics:
        total = total + classic.price
    for variety in varieties:
        total = total + variety.price
    for sandwich in sandwiches:
        total = total + sandwich.price
    for pasta in pastas:
        total = total + pasta.price
    for veggie in veggies:
        total = total + veggie.price
    for parm in parmigiana:
        total = total + parm.price
    if total == 0:
        return render(request, "orders/items.html", {"message": "Cart is Empty"})

    context = {
    "classics": RegularPizza.objects.filter(user=request.user),
    "varieties": SicilianPizza.objects.filter(user=request.user),
    "sandwiches": Subs.objects.filter(user=request.user),
    "pastas": Pasta.objects.filter(user=request.user),
    "veggies": Salads.objects.filter(user=request.user),
    "parmigiana": Parm.objects.filter(user=request.user),
    "total": total
     }
    return render(request, "orders/items.html", context)

def direct_checkout(request):
    classics = RegularPizza.objects.filter(user=request.user)
    varieties = SicilianPizza.objects.filter(user=request.user)
    sandwiches = Subs.objects.filter(user=request.user)
    pastas = Pasta.objects.filter(user=request.user)
    veggies = Salads.objects.filter(user=request.user)
    parmigiana = Parm.objects.filter(user=request.user)
    total = 0
    for classic in classics:
        total = total + classic.price
    for variety in varieties:
        total = total + variety.price
    for sandwich in sandwiches:
        total = total + sandwich.price
    for pasta in pastas:
        total = total + pasta.price
    for veggie in veggies:
        total = total + veggie.price
    for parm in parmigiana:
        total = total + parm.price
    tot_cents = int(total*100)


    stripe.api_key = STRIPE_API

    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
        'name': 'Food',
        'description': "Italy's Best!",
        'amount': tot_cents,
        'currency': 'usd',
        'quantity': 1,
        }],
    success_url='http://127.0.0.1:8000/success?session_id={CHECKOUT_SESSION_ID}',
    cancel_url='http://127.0.0.1:8000/cancel',
    customer_email = request.user.email
    )

    context = {
    "sessid": session['id']
    }
    return render(request, "orders/checkout.html", context)

def success(request):
    return render(request, "orders/success.html")

def cancel(request):
    return render(request, "orders/cancel.html")

def home(request):
    return render(request, "orders/choose.html")
