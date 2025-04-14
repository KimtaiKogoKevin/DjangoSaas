from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from  subscriptions.models import SubscriptionPrice
from django.conf import settings
import helpers.billing
BASE_URL = settings.BASE_URL
# Create your views here.
def product_price_redirect_view(request,price_id=None,*args,**kwargs):
    request.session['checkout_subscription_price_id'] = price_id
    return redirect("stripe-checkout-start")


@login_required
def checkout_redirect_view(request):
    checkout_subscription_price_id = request.session.get("checkout_subscription_price_id")
    print("checkout_subscription_price_id",checkout_subscription_price_id)
    try:
        obj = SubscriptionPrice.objects.get(id=checkout_subscription_price_id)
    except: 
        obj = None
    if checkout_subscription_price_id is None or obj is None:
        return redirect("pricing")
    customer_stripe_id = request.user.customer.stripe_id
    # print(customer_stripe_id)
    # success_url_base = BASE_URL
    success_url_path = reverse("stripe-checkout-end")
    pricing_url_path = reverse("pricing")
    success_url = f"{BASE_URL}{success_url_path}"
    cancel_url = f"{BASE_URL}{pricing_url_path}"
    price_stripe_id = obj.stripe_id
    url = helpers.billing.start_checkout_session(
                customer_stripe_id,
                success_url=success_url,
                cancel_url=cancel_url,
                price_stripe_id=price_stripe_id,
                raw=False)
    return redirect(url)

def checkout_finalize_redirect_view(request):
    session_id= request.GET.get("session_id")
    checkout_response = helpers.billing.get_checkout_session(session_id,raw=True)
    customer_id = checkout_response.customer
    sub_stripe_id =checkout_response.subscription
    subscription_response= helpers.billing.get_subscription(sub_stripe_id,raw=True)
    subscription_plan=subscription_response.plan
    subscription_plan_price_id =subscription_plan.id
    price_qs=SubscriptionPrice.objects.filter(stripe_id=subscription_plan_price_id)
    print(price_qs)
    # print(checkout_response)
    # print(subscription_response)
    context ={
        "subscription":subscription_response,
        "checkout":checkout_response,
    }
    return render(request,"checkout/success.html",context)