from django.forms import inlineformset_factory
from insta.models import Album, Photo
from django import forms

PhotoInlineFormSet = inlineformset_factory(Album, Photo,
                                           fields=['image', 'title', 'slug'],
                                           extra=2)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo  # 사용할 모델
        fields = ['owner', 'title', 'description']  # QuestionForm에서 사용할 Question 모델의 속성
        # 'name',
        widgets = {
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),

        }
        labels = {
            'owner': '작성자',
            'title': '제목',
            'description': '내용',
        }