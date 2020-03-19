from django.shortcuts import render
from .forms import User, Write
from .models import Edit, FeedFile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import auth
from django.template import RequestContext
from django.shortcuts import render_to_response
from urllib.parse import urlencode
from django import template
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

register = template.Library()
userdata = []

# Create your views here.
def index(request):
    write = Write()
    login = ''
    password = ''
    status = 'off'
    if request.user.is_authenticated:
        status = 'off'
        user = request.user
    else:
        try:
            login = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=login, password=password)
            auth.login(request, user)
        except:
            status = 'off'
    auths = User()
    user_list = Edit.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 4)
    querysetGoods = paginator.get_page(page)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    contex = {
        'users': users,
        'auth': auths,
        'page': page,
        'user_list': user_list,
        'write': write,
        'user': user
    }
    return render(request, 'index.html', contex) #{'users': users, 'auth': auth, 'user': user, 'status': status}

def single(request, id=None):
    user = request.user
    post = get_object_or_404(Edit, id=id)
    return render(request, "single.html", {'post': post, 'user': user})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def delete(request, id):
    user = request.user
    try:
        person = Edit.objects.get(id=id)
        person.delete()
        write = Write()
        return render(request, 'index.html', {'write': write, 'user': user})
    except Edit.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")@register.simple_tag(takes_context=True)

def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    query.update(kwargs)
    return query.urlencode()

def about(request):
    user = request.user
    auths = User()
    return render(request, 'about.html', {'auth': auths, "user": user})

def saveform(request):
    user = request.POST.get('user')
    write = Write()
    price = request.POST.get("price")
    about = request.POST.get("about")
    image = request.FILES['image']
    coment = request.POST.get("coment")
    files = request.FILES.getlist('files')
    post = Edit(price=price, about=about, coment=coment, image=image)
    post.save()
    post1 = Edit.objects.get(pk=post.pk)
    if files:
        for f in files:
            fl = FeedFile(feed=post1, file=f)
            fl.save()
    login = ''
    password = ''
    status = 'off'
    """try:
        login = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=login, password=password)
        auth.login(request, user)
    except:
        status = 'off'
        auth.login(request, request.user)"""
    user = request.user
    auths = User()
    user_list = Edit.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 4)
    querysetGoods = paginator.get_page(page)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    contex = {
        'users': users,
        'user': user,
        'auth': auths,
        'page': page,
        'user_list': user_list,
        'write': write
    }
    return render(request, 'index.html', contex)



