from django.shortcuts import render_to_response


def event_detail(request):
    return render_to_response('events/detail.html')