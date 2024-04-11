from django.shortcuts import render

# Create your views here.

def prescription (request):
    return render(request, 'prescription/prescription.html')