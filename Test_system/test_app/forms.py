from django import forms
from .models import Test, User, Group, Message, Applications, Review
from django.forms import ModelForm, Textarea





class TestForm(forms.ModelForm):

    class Meta:
        model = Test
        groups = forms.MultipleChoiceField(
            choices=[i.group for i in Group.objects.all()],
            required=False,
            widget=forms.CheckboxSelectMultiple(),
        )
        fields = ('test_description','groups',)
        #widgets = {'groups': forms.CheckboxSelectMultiple}



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        users = forms.MultipleChoiceField(
            choices=[i.name for i in User.objects.all()],
            required=False,
            widget=forms.CheckboxSelectMultiple(),
        )
        fields = ('group','users',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        groups = forms.MultipleChoiceField(
            choices=[i.group for i in Group.objects.all()],
            required=False,
            widget=forms.CheckboxSelectMultiple(),
        )
        fields = ('text', 'groups',)

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Applications
        user_id = forms.MultipleChoiceField(
            choices = [i.id for i in User.objects.all()],
            required=False,
            widget=forms.CheckboxSelectMultiple(),
        )
        fields  = ('id', 'user_id', 'published_date',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

        fields = ('tests',)