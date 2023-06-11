from django.shortcuts import render, redirect
from .models import Photoblog
from .forms import BlogForm
# Create your views here.

def photoblog (request):
    photoblogs = Photoblog.objects.all().order_by('-id') 
    return render(request, 'photoblog.html', {'photoblogs': photoblogs})

def add_blog(request):
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = BlogForm()
            return redirect('/photoblogs')
    else:
        form = BlogForm()
    context = {'form': form }
    return render(request, 'add_blog.html', context)

def photodetails(request, photo_id):
    photoblog = Photoblog.objects.get(id=photo_id)
    return render(request, 'photodetail.html', {'photoblog': photoblog})

