# polling/views.py

from django.shortcuts import render
from django.http import Http404
from polling.models import Poll

def list_view(request):
    """
    Views to render the templates.
    Takes request as an argument
    Retrieves all polls using the poll model
    render injects the poll model into the list.html template and 
    and returns an http response
    """
    context = {'polls': Poll.objects.all()}
    return render(request, 'polling/list.html', context)

def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {'poll': poll}
    return render(request, 'polling/detail.html', context)