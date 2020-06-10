from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from core.forms import ContactForm
from django.contrib import messages

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


def tech(request):
    template_name = 'core/tech.html'
    title = "tech page"

    context = {'title': title}
    return render(request, template_name, context)


def hobbies(request):
    template_name = 'core/hobbies.html'
    title = "hobbies page"

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
