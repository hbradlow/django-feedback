from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from feedback.forms import FeedbackForm

def leave_feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        feedback.user = request.user
        feedback.save()
        request.user.message_set.create(message="Your feedback has been saved successfully.")
        return HttpResponseRedirect(request.POST.get('next', request.META.get('HTTP_REFERER', '/')))
    return render_to_response('feedback/feedback_form.html', {'form': form}, context_instance=RequestContext(request))