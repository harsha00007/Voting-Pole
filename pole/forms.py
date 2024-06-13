from django import forms
from .models import Voters, Candidates

class VoterRegistrationForm(forms.ModelForm):
    class Meta:
        model = Voters
        fields = ['name', 'age', 'mobile_number']
        

class VoterEditForm(forms.ModelForm):
    class Meta:
        model = Voters
        fields = ["name", "age", "mobile_number"]


class OfficerLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class CandidateAddForm(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = ["candidate_name", 'candidate_party']


class CandidateEditForm(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = ["candidate_name", 'candidate_party']

class VoterLoginForm(forms.Form):
    card_number = forms.CharField(max_length=10)


class VotingForm(forms.Form):
    candidate = forms.ModelChoiceField(queryset=Candidates.objects.all(), widget=forms.RadioSelect, empty_label=None)


