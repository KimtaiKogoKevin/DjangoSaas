import helpers.billing
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render , redirect
from subscriptions.models import SubscriptionPrice , UserSubscription
from django.urls import reverse 

# Create your views here.
@login_required
def user_subscription_view(request):
    user_sub_obj , created = UserSubscription.objects.get_or_create(user=request.user)
    # subscription_data =user_sub_obj.serialize()
    if request.method == "POST":
        # Handle form submission here
        if user_sub_obj.stripe_id:
            subscription_data = helpers.billing.get_subscription(user_sub_obj.stripe_id,raw=False)
            print(("refresh subscription"))
            for k,v in subscription_data.items():
                setattr(user_sub_obj,k,v)
            user_sub_obj.save() 
            messages.success(request,"Your subscription has been updated successfully.")

        return redirect(user_sub_obj.get_absolute_url())   

    return render(request,"subscriptions/user_subscription_view.html",{"subscription":user_sub_obj})


@login_required
def user_subscription_cancel_view(request):
    user_sub_obj , created = UserSubscription.objects.get_or_create(user=request.user)
    # subscription_data =user_sub_obj.serialize()
    if request.method == "POST":
        # Handle form submission here
        if user_sub_obj.stripe_id and user_sub_obj.is_active_status:
            subscription_data = helpers.billing.cancel_subscription(user_sub_obj.stripe_id,
                                                                    raw=False,
                                                                    cancel_at_period_end=True,
                                                                    reason="user requested cancellation",
                                                                    feedback="other")
            print(("refresh subscription"))
            for k,v in subscription_data.items():
                setattr(user_sub_obj,k,v)
            user_sub_obj.save() 
            messages.success(request,"Your subscription has been cancelled successfully.")
        return redirect(user_sub_obj.get_absolute_url())   

    return render(request,"subscriptions/user_subscription_cancel.html",{"subscription":user_sub_obj})



def subscription_price_view(request,interval="month"):


    qs =SubscriptionPrice.objects.filter(featured=True)
    inv_mo = SubscriptionPrice.IntervalChoices.MONTHLY
    inv_yr= SubscriptionPrice.IntervalChoices.YEARLY
    object_list=qs.filter(interval=inv_mo)
    url_path_name= "pricing_interval"
    mo_url = reverse(url_path_name,kwargs={"interval":inv_mo})
    yr_url = reverse(url_path_name,kwargs={"interval":inv_yr})
    active= inv_mo
    if interval == inv_yr:
        active = inv_yr
        object_list=qs.filter(interval=inv_yr)
    

    return render(request,"subscriptions/pricing.html",{
        "object_list":object_list,
        "mo_url":mo_url,
        "yr_url":yr_url,
        "active":active
        
    })
