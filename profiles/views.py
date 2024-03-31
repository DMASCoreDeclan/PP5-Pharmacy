from django.shortcuts import render


def profiles(request):
    """
    Display the Users profile
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)