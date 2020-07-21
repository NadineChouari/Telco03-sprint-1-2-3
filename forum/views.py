
from django.shortcuts import render, redirect, get_object_or_404
from forum.models import blog_posts
from .forms import PostsForm
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.

def save_post_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            posts = blog_posts.objects.all()
            data['html_post_list'] = render_to_string('forum/templates/blog_posts/post_list.html', {
                'posts': posts
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def post_list(request):
    #posts = blog_posts.objects.all()
    #data = {}
    #data['object_list'] = posts
    #return render(request, "forum/templates/blog_posts/post_list.html", data)
    posts = blog_posts.objects.all()
    return render(request, 'forum/templates/blog_posts/post_list.html', {'posts': posts})


def post_create(request):
    if request.method == 'POST':

        form = PostsForm(request.POST or None)
        if form.is_valid():
            form.save()
    else :
            form = PostsForm()
    #return render(request,"forum/templates/blog_posts/post_list.html", {'form': form})

    return render(request, "../../telco_project/templates/pages/ui-forum.html",{'form': form})



def post_update(request, pk):
    post = get_object_or_404(blog_posts, pk=pk)
    if request.method == 'POST':
        form = PostsForm(request.POST or None, instance=post)
        form.save()
    else:
        form = PostsForm(instance=post)
    return render(request, "../../telco_project/templates/pages/ui-forum.html",{'form': form})    


def post_delete(request, pk):
    post = get_object_or_404(blog_posts, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('blog_posts:post_list')
    return render(request, "forum/templates/blog_posts/includes/partial_post_delete.html", {'post': post})
