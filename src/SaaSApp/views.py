
from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent
def home_view(request, *args, **kwargs):
    
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
        "total_visits_count":qs.count()}
    html_template="home.html"
    PageVisit.objects.create(path=request.path)
    path= request.path
    print("path",path)
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