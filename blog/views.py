from django.shortcuts import render,redirect
from .forms import PostFrom
from .models import User,Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login_url')
def add_post(request):
    template_name = 'blog/post.html'
    form = PostFrom()
    if request.method == 'POST':
        form = PostFrom(request.POST)
        # author_id = User.objects.get(id=request.user.id)
        # form.author = author_id
        # form['author'] = author_id
        if form.is_valid():
            # form.save(commit=False)
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home_url')

    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login_url')
def home_view(request):
    template_name = 'blog/home.html'
    all_posts = Post.objects.all().order_by('-posted_at')
    context={'all_posts':all_posts}
    return render(request,template_name,context)

@login_required(login_url='login_url')
def blog_details(request,pk):
    template_name = 'blog/blog_details.html'
    blog_post =  Post.objects.get(id=pk)
    context={'blog_post':blog_post}
    return render(request,template_name,context)


@login_required(login_url='login_url')
def my_posts(request):
    template_name = 'blog/my_posts.html'

    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user).order_by('-posted_at')
    else:
        posts = Post.objects.all().order_by('-posted_at')
    context= {'posts': posts}
    return render(request, template_name,context)



@login_required(login_url='login_url')
def edit_post(request, post_id):
    post=Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostFrom(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('my_posts_url')
    else:
        form = PostFrom(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required(login_url='login_url')
def delete_post(request, post_id):
    # post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    post=Post.objects.get(id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('my_posts_url')
    return render(request, 'blog/delete_post.html', {'post': post})



def sample_view():
    pass



