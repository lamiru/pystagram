from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'content', 'tags', 'origin_url')

    def clean_title(self):
        title = self.cleaned_data.get('title').strip()
        if len(title) < 10:
            msg = 'Input more than 10 letters.'
            raise forms.ValidationError(msg)
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content').strip()
        if len(content) < 10:
            msg = 'Input more than 10 letters.'
            raise forms.ValidationError(msg)
        return content
