# polling/views.py

from django.shortcuts import render
from django.http import Http404
from polling.models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# REPLACED BY THE CLASS VIEW BELOW
# def list_view(request):
#     """
#     Views to render the templates.
#     Takes request as an argument
#     Retrieves all polls using the poll model
#     render injects the poll model into the list.html template and
#     and returns an http response
#     """
#     context = {'polls': Poll.objects.all()}
#     return render(request, 'polling/list.html', context)


class PollListView(ListView):
    model = Poll
    template_name = 'polling/list.html'


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polling/detail.html'

    def post(self, request, *args, **kwargs):
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        context = {'object': poll}
        # we use the polling dir inside templates so the location of our template is easy to see
        return render(request, 'polling/detail.html', context)


# def detail_view(request, poll_id):
#     try:
#         poll = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404

#     if request.method == "POST":
#         if request.POST.get("vote") == "Yes":
#             poll.score += 1
#         else:
#             poll.score -= 1
#         poll.save()

#     context = {'poll': poll}
#     # we use the polling dir inside templates so the location of our template is easy to see
#     return render(request, 'polling/detail.html', context)
