from django import forms

class QuestionForm(forms.Form):
      your_name = forms.CharField(
          label='Question',
          max_length=20,
          required=True,
          widget=forms.TextInput()
      )
