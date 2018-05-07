from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import ItemForm
from .models import Item


# Create your views here.

def post_list(request):
    posts = Item.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request,'freezer/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Item, pk = pk)
    return render(request,'freezer/post_detail.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ItemForm()
    return render(request, 'freezer/post_edit.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ItemForm(instance=post)
    return render(request, 'freezer/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Item, pk=pk)
    post.delete()
    return redirect('post_list')

