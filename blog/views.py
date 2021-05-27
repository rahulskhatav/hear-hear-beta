import blog
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from . models import BArticle
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from debate.forms import blogCreate
from user.models import Profile

# Create your views here.
def index(request):
    articles = BArticle.objects.all().order_by('-date_posted')
    context = {
        "articles" : articles,
    }
    return render(request, "blog/index.html", context)

def spec(request, blog_id):
    article = BArticle.objects.get(pk=blog_id)
    context = {
        "article" : article,
    }
    return render(request, "blog/spec.html", context)

@login_required
def create(request):
    t = ""
    ca = ""
    co = ""
    if request.method == "POST":
        form = blogCreate(request.POST)
        if form.is_valid():
            t = form.cleaned_data['title']
            ca = form.cleaned_data['caption']
            co = form.cleaned_data['content']
            BArticle.objects.create(title=t, caption=ca, content=co, owner=request.user)
            prof = Profile.objects.get(user=request.user)
            prof.contributions = prof.contributions+1
            prof.save()
            return HttpResponseRedirect(reverse('blog-home'))
        else:
            messages.warning("Please fill a valid entry.")
    form = blogCreate()
    context = {
        "form" : form,
    }
    return render(request, "blog/create.html", context)