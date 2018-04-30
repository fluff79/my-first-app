from django.shortcuts import render
from django.utils import timezone
from .models import Item


# Create your views here.

def post_list(request):
    posts = Item.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request,'freezer/post_list.html', {'posts' : posts})
