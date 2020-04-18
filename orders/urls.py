from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("to_pizza", views.to_pizza, name = "to_pizza"),
    path("direct_cheese", views.direct_cheese, name = "direct_cheese"),
    path("cheese", views.cheese, name = "cheese"),
    path("direct_special", views.direct_special, name = "direct_special"),
    path("special", views.special, name = "special"),
    path("direct_pizza", views.direct_pizza, name = "direct_pizza"),
    path("custom", views.create_pizza, name = "create_pizza"),
    path("direct_salad", views.direct_salad, name = "direct_salad"),
    path("direct_sub",views.direct_sub,name="direct_sub"),
    path("create_sub", views.create_sub, name = "create_sub"),
    path("direct_pasta", views.direct_pasta, name = "direct_pasta"),
    path("create_pasta", views.create_pasta, name = "create_pasta"),
    path("create_salads", views.create_salads, name = "create_salads"),
    path("direct_platter", views.direct_platter, name = "direct_platter"),
    path("create_platter", views.create_platter, name = "create_platter"),
    path("cart", views.cart, name = "cart"),
    path("items", views.items, name = "items"),
    path("direct_checkout", views.direct_checkout, name="direct_checkout"),
    path("success", views.success, name="success"),
    path("cancel", views.cancel, name="cancel"),
    path("home", views.home, name = "home")

]
