from django import forms
from boards.models import Topic, Post


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
    widget=forms.Textarea(
    attrs={'rows': 5, 'placeholder': 'Message'}
    ),
    max_length=4000,
    help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


    def __str__(self):
        return self.message

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]