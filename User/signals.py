from django.dispatch import receiver
from allauth.account.signals import user_signed_up, user_logged_in
# from store.models import Cart
from FarmerInfo.models import FarmerData
from User.models import Customer
from Orders.models import Order
# from transaction.models import Wallet




@receiver(user_signed_up)
def create_customer_on_signup(request, user, **kwargs):
    # You can also pre-fill fields if Allauth provides them
    Customer.objects.get_or_create(
        user=user,
        defaults={
            "first_name": user.first_name or "",
            "last_name": user.last_name or "",
            "phone": "",  # can be updated later by user
            "street_address": "",
            "city": "",
            "country": "",
        }
    )



@receiver(user_signed_up)
def handle_user_signup(request, user, **kwargs):
    # Create profile (farmerInfo app)
    FarmerData.objects.create(user=user)
    # Create empty cart (store app)
    Cart.objects.get_or_create(user=user)
    # Create empty order history (orders app)
    OrderHistory.objects.get_or_create(user=user)
    # Create wallet (transaction app)
    Wallet.objects.get_or_create(user=user)


@receiver(user_logged_in)
def merge_guest_cart_on_login(request, user, **kwargs):
    session_cart_id = request.session.get("cart_id")
    if session_cart_id:
        from store.models import Cart  # local import to avoid circular issues
        try:
            guest_cart = Cart.objects.get(id=session_cart_id, user=None)
            user_cart, created = Cart.objects.get_or_create(user=user)
            user_cart.merge(guest_cart)
            del request.session["cart_id"]
        except Cart.DoesNotExist:
            pass