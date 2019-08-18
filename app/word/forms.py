from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('word', 'mean1', 'mean2', 'mean3', 'part_of_speech')
        widgets = {
            'word': forms.TextInput(attrs={
                'placeholder':'登録したい英単語を入力してください'
            }),
            'mean1': forms.TextInput(attrs={
                'placeholder':'登録する英単語の意味を入力してください'
            }),
            'mean2': forms.TextInput(attrs={
                'placeholder':'登録する英単語の意味が2つあれば入力してください'
            }),
            'mean3': forms.TextInput(attrs={
                'placeholder':'登録する英単語の意味が3つあれば入力してください'
            }),
            'part_of_speech': forms.NumberInput(attrs={'max':7})
        }
