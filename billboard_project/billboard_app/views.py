from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .models import Post, Comment
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

            data = {"title":post_title,"author":post_author,"message":post_text,"pub_date":created_date}
            html = render_to_string('posts.html', {'data': data})
            return HttpResponse(html)

def comment(request):
    if request.method == 'POST':
        if request.is_ajax():
            comment_message = request.POST.get("comment")
            comment_id = request.POST.get("id")
            print(comment_message)
            obj = Post.objects.get(pk=comment_id)
            print("id_num",obj.pk)
            x = Comment(message=comment_message,post_id_id=obj.pk)
            x.save()

            data = {"message": comment_message, "post_id": obj.pk}
            print("data",data)
            html = render_to_string('comments.html', {'data': data})
            return HttpResponse(html)