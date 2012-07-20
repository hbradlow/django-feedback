from django import forms

from feedback.models import Feedback, AnonymousFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ('user','content_type','object_id','content_object')

class AnonymousFeedbackForm(forms.ModelForm):
    class Meta:
        model = AnonymousFeedback
        exclude = ('user','content_type','object_id','content_object')
