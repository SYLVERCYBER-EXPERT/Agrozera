from .models import Cart

def get_or_create_guest_cart(request):
    cart_id = request.session.get("cart_id")
    if cart_id:
        cart = Cart.objects.filter(id=cart_id, user=None).first()
        if cart:
            return cart

    # create new guest cart
    cart = Cart.objects.create(user=None)
    request.session["cart_id"] = cart.id
    return cart
