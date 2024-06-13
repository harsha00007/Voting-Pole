from django.shortcuts import render
from .models import Voters, Candidates
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VoterRegistrationForm, CandidateAddForm, OfficerLoginForm, CandidateEditForm, VoterEditForm, VoterLoginForm, VotingForm
from django.contrib.auth import authenticate, login


# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def voter_register_view(request):
    if request.method == 'POST':
        form = VoterRegistrationForm(request.POST)
        if form.is_valid():
            voter = form.save()
            return redirect('registration_success', voter_id=voter.id)
    else:
        form = VoterRegistrationForm()
    return render(request, 'voter_register.html', {'form': form})


def voter_login_view(request):
    if request.method == 'POST':
        form = VoterLoginForm(request.POST)
        if form.is_valid():
            card_number = form.cleaned_data['card_number']
            try:
                voter = Voters.objects.get(card_number=card_number)
            except Voters.DoesNotExist:
                return render(request, "failure.html")

            if voter.already_vote:
                return render(request, "already_vote.html")
            else:
                voter.already_vote = True
                voter.save()
                return redirect('voting_pole')
    else:
        form = VoterLoginForm()
    
    return render(request, 'voting_pole_login.html', {'form': form})


def registration_success_view(request, voter_id):
    voter = Voters.objects.get(id=voter_id)
    return render(request, 'registration_success.html', {'voter': voter})


def voter_list_view(request):
    voters = Voters.objects.all()
    return render(request, 'voter_list.html', {"voters":voters})


def voter_edit_view(request, pk):
    voters = get_object_or_404(Voters, pk=pk)
    if request.method == 'POST':
        form = VoterEditForm(request.POST, instance=voters)
        if form.is_valid():
            form.save()
            return redirect('voter_list')
    else:
        form = CandidateEditForm(instance=voters)
        return render(request, 'voter_edit.html', {'form': form})


def voter_delete_view(request, pk):
    voters = get_object_or_404(Voters, pk=pk)
    if request.method == 'POST':
        voters.delete()
        return redirect('voter_list')
    return render(request, 'voter_delete.html', {'voters': voters})


def officer_login_view(request):
    if request.method == 'POST':
        form = OfficerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.email == email:
                login(request, user)
                return redirect('officer_dashboard')  
    else:
        form = OfficerLoginForm()
    return render(request, 'officer_login.html', {'form': form})


def candidate_add_view(request):
    if request.method == 'POST':
        form = CandidateAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CandidateAddForm()
    return render(request, 'candidate_add.html', {'form': form})


def candidate_list_view(request):
    candidates = Candidates.objects.all()
    return render(request, "candidate_list.html", {"candidates": candidates})


def candidate_edit_view(request, pk):
    candidate = get_object_or_404(Candidates, pk=pk)
    if request.method == 'POST':
        form = CandidateEditForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('candidate_list')
    else:
        form = CandidateEditForm(instance=candidate)
    return render(request, 'candidate_edit.html', {'form': form})


def candidate_delete_view(request, pk):
    candidate = get_object_or_404(Candidates, pk=pk)
    if request.method == 'POST':
        candidate.delete()
        return redirect('candidate_list')
    return render(request, 'candidate_delete.html', {'candidate': candidate})


def officer_dashboard_view(request):
    return render(request, 'officer_dashboard.html')


def voting_pole_view(request):
    return render(request, 'voting_pole.html')


def success_view(request):
    return render(request, "candidate_add_succes.html")

def failure_view(request):
    return render(request, "failure.html")

def voting_pole_view(request):
    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            candidate = form.cleaned_data['candidate']
            candidate.votes += 1
            candidate.save()
            return redirect("voting_success", candidate_sl_number=candidate.sl_number)
    else:
        form = VotingForm()

    return render(request, 'voting_pole.html', {'form': form})


def voting_success_view(request, candidate_sl_number):
    candidate = Candidates.objects.get(sl_number=candidate_sl_number)
    return render(request, "voting_success.html", {"candidate":candidate} )


def result_view(request):
    candidates = Candidates.objects.all()
    results = []
    for candidate in candidates:
        vote_count = candidate.votes
        results.append({
            'candidate': candidate,
            'vote_count': vote_count,
            'candidate_party': candidate.candidate_party
        })
    results = sorted(results, key=lambda x: x['vote_count'], reverse=True)
    
    return render(request, 'result.html', {'results': results})