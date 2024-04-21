from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import CommunicationContent
from .forms import CommunicationForm

# Create your views here.

def index(request):
    ''' A view to return the index page'''
    return render(request, 'home/index.html')


# def subscribe(request):
#     return render(request, 'home/subscribe.html')


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


# @user_passes_test(lambda u: u.is_superuser)
# https://stackoverflow.com/questions/12003736/django-login-required-decorator-for-a-superuser
def add_web_article(request):
    """
    View to add articles that are of type WEBSITE_ARTICLE
    """
    form = CommunicationForm()
    template = 'home/article_add.html'
    context = {
        'form': form,
    }

    return render(request, template, context)