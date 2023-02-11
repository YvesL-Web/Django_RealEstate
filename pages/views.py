from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices,bedroom_choices,state_choices
from listings.models import Listing
from agent.models import Agent

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
    }

    return render(request,'pages/index.html', context)

def about(request):
    # Get all Agent
    agents = Agent.objects.order_by('-hire_date')
    
    # Get the best of all seller 
    mvp_agent = Agent.objects.all().filter(is_mvp=True)

    context = {
        'agents' : agents,
        'mvp_agent': mvp_agent
    }

    return render(request, 'pages/about.html', context)