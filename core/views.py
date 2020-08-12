from django.shortcuts import render, redirect 
from django.http import HttpResponse, JsonResponse
# Create your views here.
from core.forms import ContactForm, PictureForm
from django.contrib import messages
from .models import *
from django.views.generic import ListView, DetailView

def index(request):
    template_name = 'core/index.html'
    title = "andi the robot"

    context = {'title': title}
    return render(request, template_name, context)


def about(request):
    template_name = 'core/about.html'
    title = "about page"

    context = {'title': title}
    return render(request, template_name, context)






def photos(request):
    template_name = 'core/photos.html'
    title = "photos page"

    context = {'title': title}
    return render(request, template_name, context)


def feed(request):
    template_name = 'core/feed.html'
    title = "feed page"

    context = {'title': title}
    return render(request, template_name, context)


def contact(request):
    if request.method != 'POST':
        title = "revive contact page"
        form = ContactForm()
        context = {'title': title, 'form': form}
        return render(request, 'core/contact.html', context)

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message Sent successfully")
            return render(request, 'core/contact.html')
            # return JsonResponse(request.POST,)



def hotel_image_view(request): 
  
    if request.method == 'POST': 
        form =PictureForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = PictureForm() 
    return render(request, 'core/gallery.html', {'form' : form}) 


def success(request): 
    return HttpResponse('successfully uploaded') 

class PhotosView(ListView):
    model = PicturePost
    template_name = 'core/photos.html'

class TextView(ListView):
    model = TextPost
    template_name = 'core/writings.html'

class WritingsDetail(DetailView):
    template_name = 'core/writings_detail.html'
    model = TextPost


