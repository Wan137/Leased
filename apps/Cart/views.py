from django.shortcuts import render, redirect

from .models import Cart
from apps.Flat.models import Flats


def create(request):
    if request.method == "POST":
        flats_id = request.POST.get('flats_id')
        flats = Flats.objects.get(id=flats_id)
        cart = Cart.objects.create(clothes_id=flats, user_id=request.user)
        # return redirect('index')

