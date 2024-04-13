from django.shortcuts import render
from .models import CommunicationContent

# Create your views here.

def index(request):
    ''' A view to return the index page'''
    return render(request, 'home/index.html')


def healthcare(request):
    web_article = CommunicationContent.objects.all().filter(status=2, content_type=2)

    template = 'home/healthcare.html'
    # paginate_by = 6
    context = {
        'webarticles': web_article,
        # 'article': article,
    }

    return render(request, template, context)


# class NewsletterContent(generic.ListView):
#     model = CommunicationContent
#     queryset = CommunicationContent.objects.filter(status=2, content_type=1)


