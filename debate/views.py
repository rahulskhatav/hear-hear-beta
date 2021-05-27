from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import resolvers
from . models import motion, argument, subpoint
from django.contrib import messages
from django.http import HttpResponse
from . forms import motionCreate, argumentCreate, subpointCreate
from django.contrib.auth.decorators import login_required
from user.models import Profile

# Create your views here.
def index(request):
    context = {
        'motions' : motion.objects.all().order_by('-date_posted')
    }
    return render(request, 'debate/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = motionCreate(request.POST, instance=request.user)
        if form.is_valid():
            t = form.cleaned_data['title']
            c = form.cleaned_data['context']
            d = form.cleaned_data['difficulty']
            motion.objects.create(title=t, context=c, difficulty=d, owner=request.user)
            prof = Profile.objects.get(user=request.user)
            prof.contributions = prof.contributions+0.5
            prof.save()
            return HttpResponseRedirect(reverse('debate-index'))
    form = motionCreate()
    context = {
        "form": form,
    }
    return render(request, 'debate/create.html', context)

def spec_motion(request, motion_id):
    this_motion = motion.objects.get(pk=motion_id)
    this_arguments = argument.objects.filter(to_motion=this_motion)
    form = argumentCreate()
    context = {
        "motion" : this_motion,
        "arguments": this_arguments,
        "form": form,
    }
    return render(request, 'debate/motion.html', context)

@login_required
def make_arg(request, motion_id):
    if request.method == 'POST':
        form = argumentCreate(request.POST, instance=request.user)
        if form.is_valid():
            s = form.cleaned_data['side']
            t = form.cleaned_data['title']
            c = form.cleaned_data['content']
            m = motion.objects.get(pk=motion_id)
            argument.objects.create(side=s, title=t, content=c, to_motion=m, owner=request.user)
            prof = Profile.objects.get(user=request.user)
            prof.contributions = prof.contributions+1
            prof.save()
            messages.warning(request, "Argument added succesfully.")
        else:
            messages.warning(request, "Please make a valid argument.")
    return HttpResponseRedirect(reverse('debate-motion', args=(motion_id,)))

def spec_argument(request, arg_id):
    this_argument = argument.objects.get(pk=arg_id)
    this_points = subpoint.objects.filter(to_arg=this_argument)
    form = subpointCreate()
    context = {
        "argument" : this_argument,
        "points" : this_points,
        "form": form,
    }
    return render(request, 'debate/argument.html', context)

@login_required
def make_point(request, arg_id):
    if request.method == 'POST':
        form = subpointCreate(request.POST, instance=request.user)
        if form.is_valid():
            s = form.cleaned_data['side']
            c = form.cleaned_data['content']
            a = argument.objects.get(pk=arg_id)
            subpoint.objects.create(side=s, content=c, to_arg=a, owner=request.user)
            prof = Profile.objects.get(user=request.user)
            prof.contributions = prof.contributions+0.5
            prof.save()
            messages.warning(request, "Point added succesfully.")
        else:
            messages.warning(request, "Please make a valid point.")
    return HttpResponseRedirect(reverse('debate-spec-arg', args=(arg_id,)))

def help(request):
    return render(request, 'debate/help.html')