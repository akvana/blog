from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Post
from .forms import  PostForm,CommentForm
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q
# Create your views here.
def post_index(request):
    post_list=Post.objects.all()
    query=request.GET.get('q')
    if query:
        post_list=post_list.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(user__first_name__icontains=query) |
        Q(user__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(post_list, 6)

    page = request.GET.get('sayfa')
    post = paginator.get_page(page)
    return render(request, 'post/post_index.html', {'posts': post})



def post_detail(request,slug):
    post=get_object_or_404(Post,slug=slug)

    form=CommentForm(request.POST or None)
    if form.is_valid():
        comment=form.save(commit=False)
        comment.post=post
        comment=form.save()
        messages.success(request,'Başarılı bir şekilde Yorum oluşturdunuz.')
        return HttpResponseRedirect(post.get_absolute_url())
    context={
        'post':post,
        'form':form,

    }

    return render(request,'post/post_detail.html',context)




def post_crate(request):
    if not request.user.is_authenticated:
        return Http404
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post=form.save(commit=False)
        post.user=request.user
        post=form.save()
        messages.success(request,'Başarılı bir şekilde oluşturdunuz.')
        return HttpResponseRedirect(post.get_absolute_url())
    context={
            'form':form,
    }
    return render(request,'post/post_create.html',context)



def post_update(request,slug):
    post=get_object_or_404(Post,slug=slug)
    form=PostForm(request.POST or None,request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request,'Başarılı bir şekilde Yenilediniz.')
        return HttpResponseRedirect(post.get_absolute_url())
    context={
        'form':form,
    }
    return render(request,'post/post_update.html',context)


def post_delete(request,slug):
    post=get_object_or_404(Post,slug=slug)
    post.delete()
    return redirect('post:index')
