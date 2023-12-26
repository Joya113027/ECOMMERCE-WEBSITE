
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='ShopHome'),
    path("about/",views.about,name='aboutUs'),
    path("contact/",views.contact,name='contactUs'),
    path("search/",views.search,name='search'),
    path("productview/<int:myid>",views.productview,name='productView'),
    path("checkout/",views.checkout,name='checkOut'),
    path("tracker/",views.tracker,name='tracker')
]
