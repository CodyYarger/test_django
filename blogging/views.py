from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post


# added for assignment 08
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


# removed for assignment 08
# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args:\n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")


# def list_view(request):
#     """job of a view: accepts a request and returns a response"""
#     # queries model an dgets all posts with a published date
#     published = Post.objects.exclude(published_date__exact=None)

#     # sort in published reverse order
#     posts = published.order_by('-published_date')

#     # finds the list.html templates
#     template = loader.get_template('blogging/list.html')

#     # injects into posts and returns response
#     context = {'posts': posts}
#     body = template.render(context)
#     return HttpResponse(body, content_type="text/html")
#     # return render(request, 'list.html', context) # this replaces the above two lines

# def detail_view(request, post_id):
#     # query for published posts
#     published = Post.objects.exclude(published_date__exact=None)

#     # retrieve post with post id in the path
#     try:
#         post = published.get(pk=post_id)
#     # raise 404 if post doesn't exist
#     except Post.DoesNotExist:
#         raise Http404

#     # injects post into the template
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)
