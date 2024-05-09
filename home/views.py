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


def all_articles(request):
    """
    View to display articles that
    """
    articles = CommunicationContent.objects.all()
    # else:
    #     web_article = CommunicationContent.objects.all().filter(
    #     status=2, content_type=2
    #     )

    template = 'home/all_articles.html'
    context = {
        'articles': articles,
    }

    return render(request, template, context)


@login_required
def add_article(request):
    """
    View to add articles that are of type WEBSITE_ARTICLE
    """
    if not request.user.is_staff:
        messages.error(request, 'Only members of the Store Team can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CommunicationForm(request.POST, request.FILES)
        type = CommunicationType.objects.all() # filter(name='website_article')
        status = CommunicationStatus.objects.all() # filter(id=2)
        if form.is_valid():
            article = form.save(commit=False)
            article.slug = slugify(article.title)
            article.author = request.user
            article.save()
            messages.success(
                request, 
                f'{request.user}, you\'ve aded a new article!'
                )
            return redirect(reverse('all_articles'))
    else:
        form = CommunicationForm()

    form = CommunicationForm()
    template = 'home/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_article(request, slug,):
    """
    Edit an article in healthcare_advice
    """
    if not request.user.is_staff:
        messages.error(request, 'Only members of the Store Team can do that')
        return redirect(reverse('home'))

    article = get_object_or_404(CommunicationContent, slug=slug)
    article_form = CommunicationForm(request.POST, request.FILES, instance=article)

    if request.method == 'POST': 
        if article_form.is_valid():
            article.author = request.user
            article.slug = slugify(article.title)
            article.save()
            messages.success(request, 'Successfully updated article!')
            return redirect(reverse('edit_articles'))
        else:
            messages.error(request, 'Failed to update article. Please ensure the form is valid.')
    else:
        article_form = CommunicationForm(instance=article)
        messages.info(request, f'You are editing {article.title}')

    template = 'home/edit_article.html'
    context = {
        'article_form': article_form,
        'article': article,
    }

    return render(request, template, context)


def article_detail(request, article_id):
    """ A view to return a single article,
    including sorting and search queries """

    article = get_object_or_404(CommunicationContent, pk=article_id)

    context = {
        'article': article
    }

    return render(request, 'home/article_detail.html', context)


@login_required
def delete_article(request, slug):
    """
    Delete an article from the store
    """
    if not request.user.is_staff:
        messages.error(request, 'Only members of the Store Team can do that')
        return redirect(reverse('all_articles'))

    article = get_object_or_404(CommunicationContent, slug=slug)
    
    context ={
        'article': article, 
    }

    if request.method == 'GET':
        return render(request, 'home/confirm_delete.html', context)

    if request.method == 'POST':
        article.delete() 
        messages.success(request, 'Successfully deleted article!')
        return redirect(reverse('all_articles'))
    else:
        messages.error(request, 'Failed to delete article. Please ensure the form is valid.')
        return redirect(reverse('delete_articles'))


@login_required
def delete_articles(request):
    """
    Delete articles from the store
    """
    if not request.user.is_staff:
        messages.error(request, 'Only members of the Store Team can do that')
        return redirect(reverse('home'))
        
    articles = CommunicationContent.objects.all()

    template = 'home/delete_articles.html'
    context = {
        'articles': articles,
    }

    return render(request, template, context)


@login_required
def edit_articles(request):
    articles = CommunicationContent.objects.all()
    template = 'home/edit_articles.html'
    context = {
        'articles': articles,
    }

    return render(request, template, context)
    