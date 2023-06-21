from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Photoblog, Like, Comment
from .forms import BlogForm, CommentForm
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

@login_required
def like_view(request, photoblog_id):
    photoblog = get_object_or_404(Photoblog, id=photoblog_id)
    
    # Check if the user has already liked the photoblog
    if photoblog.likes.filter(user=request.user).exists():
        # User has already liked the photoblog, remove the like
        photoblog.likes.remove(request.user)
    else:
        # User has not liked the photoblog, add the like
        photoblog.likes.add(request.user)
    
    # Redirect back to the appropriate page
    if photoblog.photo:
        return redirect('photodetails', photoblog_id=photoblog_id)
    else:
        return redirect('photoblogs')

@login_required
def add_comment(request, photoblog_id):
    photoblog = get_object_or_404(Photoblog, id=photoblog_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['text']
            comment = Comment.objects.create(photoblog=photoblog, user=request.user, text=comment_text)
            # You can add additional logic here, such as redirecting to the photoblog details page
            return redirect('photodetails', photoblog_id=photoblog_id)
    else:
        form = CommentForm()


    return render(request, 'add_comment.html', {'form': form, 'photoblog': photoblog})
