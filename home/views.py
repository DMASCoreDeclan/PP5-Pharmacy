from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.defaultfilters import slugify

from .models import CommunicationContent, CommunicationType, CommunicationStatus
from .forms import CommunicationForm

# Create your views here.

def index(request):
    ''' A view to return the index page'''
    return render(request, 'home/index.html')


def subscribe(request):
    '''
    <!-- render code for mailchimp.com newsletter -->
    '''
    return render(request, 'home/subscribe.html')


def healthcare_advice(request):
    """
    View to display PUBLISHED articles that are of type WEBSITE_ARTICLE
    """
    web_article = CommunicationContent.objects.all().filter(
        status=2, content_type=2
        )

    template = 'home/healthcare_advice.html'
    context = {
        'webarticles': web_article,
    }

    return render(request, template, context)


@login_required
def add_article(request):
    """
    View to add articles that are of type WEBSITE_ARTICLE
    """
    if not request.user.is_staff:
        messages.error(request, 'Only Store Owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CommunicationForm(request.POST, request.FILES)
        type = CommunicationType.objects.filter(name='website_article')
        status = CommunicationStatus.objects.filter(id=2)
        if form.is_valid:
            article = form.save(commit=False)
            article.slug = slugify(article.title)
            article.author = request.user
            article.save()
            messages.success(
                request, 
                f'{request.user}, you\'ve aded a new article!'
                )
            return redirect(reverse('healthcare_advice'))
    else:
        form = CommunicationForm()





    form = CommunicationForm()
    template = 'home/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)