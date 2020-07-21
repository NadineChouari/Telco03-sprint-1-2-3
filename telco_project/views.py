from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse

@login_required(login_url="/login/")
def index(request):
    context = {'segment' : 'index'}
    return render(request, "index.html", context)


@login_required(login_url="/login/")
def calendar(request):

    return render(request, "pages/calendar.html")



@login_required(login_url="/login/")
def users(request):

    return render(request, "pages/ui-tables.html")


@login_required(login_url="/login/")
def profile(request):

    return render(request, "pages/page-user.html")

@login_required(login_url="/login/")
def post_detail(request):

    return render(request, "pages/post_detail.html")

@login_required(login_url="/login/")
def maps(request):

    return render(request, "pages/ui-maps.html")

@login_required(login_url="/login/")
def forum(request):

    return render(request, "pages/ui-forum.html")



@login_required(login_url="/login/")
def notifications(request):
 
    return render(request, "pages/ui-notifications.html")



    """
@login_required(login_url="/login/")
def pages(request):
    context = {}

    try:

        load_template = request.path.split('/')[-1]

        context['segment'] = load_template

        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request)) """
