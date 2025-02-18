
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
import pathlib
from visits.models import PageVisit

LOGIN_URL = settings.LOGIN_URL

this_dir = pathlib.Path(__file__).resolve().parent
def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        print(request.user.first_name)
    
    return about_view(request,*args , **kwargs )

def about_view(request, *args, **kwargs):

   
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)

    try:
        percent=(page_qs.count() * 100.0) / qs.count()
    except:
        percent=0

    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count" : page_qs.count(),
        "percent":percent,
        "total_visits_count":qs.count()
        }
    html_template="home.html"
    PageVisit.objects.create(path=request.path)
    # path= request.path
    # print("path",path)
    return render(request, html_template,my_context)

def old_home_page_view(request, *args, **kwargs):
    # print(this_dir)
    # html=""
    # html_file_path = this_dir / "home.html"
    # html = html_file_path.read_text()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
    } 
    html = """

          <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learning Django</title>
</head>
<body>
    <h1> Is this something</h1>
</body>
</html>

        """.format(**my_context)
    
    
    return HttpResponse(html)


VALID_CODE  ="abc123"

def pw_protected_view(request,*args,**kwargs):
    is_allowed = request.session.get('protected_page_allowed') or 0
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed= 1
            request.session['protected_page_allowed'] = 1
    if is_allowed:
        return render(request,"protected/view.html",{})
    return render(request, "protected/entry.html",{})

@login_required(login_url=LOGIN_URL)
def user_only_view(request, *args, **kwargs):
    return render(request,"protected/user-only.html",{})

@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request, *args, **kwargs):
    return render(request,"protected/user-only.html",{})