from django.forms import inlineformset_factory
from insta.models import Album, Photo, Answer
from django import forms

PhotoInlineFormSet = inlineformset_factory(Album, Photo,
                                           fields=['image', 'title',],
                                           extra=2)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo  # 사용할 모델
        fields = ['title', 'description']  # QuestionForm에서 사용할 Question 모델의 속성
        # 'name',
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),

        }
        labels = {

            'title': '제목',
            'description': '내용',
        }



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }