from django.shortcuts import render


# A view that shows the landing page
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
