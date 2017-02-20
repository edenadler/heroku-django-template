from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import Post
from django.utils import timezone
from django.template.loader import render_to_string

def check_db(request):
        database_state = Post.objects.all()
        print("database",database_state)
        return render(request, 'index.html', {'database_state': database_state})


def store(request):
    if request.method == 'POST':
        if request.is_ajax():
            post_title = request.POST.get("title")
            print("post-title",post_title)
            post_author = request.POST.get("author")
            print(post_author)
            post_text = request.POST.get("text")
            print(post_text)
            created_date = timezone.now()

            x=Post(title=post_title,author = post_author,message = post_text,pub_date=created_date)
            x.save()

            # database_state = Post.objects.all()
            # print("database_state",database_state)
            data = {"title":post_title,"author":post_author,"message":post_text,"pub_date":created_date}
            html = render_to_string('posts.html', {'data': data})
            return HttpResponse(html)