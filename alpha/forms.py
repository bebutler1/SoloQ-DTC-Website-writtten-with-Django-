from django import forms
from django.http import HttpResponseRedirect

class DataForm(forms.Form):
    your_name = forms.CharField(max_length=30,help_text="What is your Ingame name?")
    champion = forms.CharField(max_length=20, help_text="What champion did you play this game?")
    role = forms.CharField(max_length=7,help_text="What role did you play in this game?")
    teammate_1 = forms.CharField(max_length=30,help_text="Enter a teammate's Ingame name here.")
    teammate_2= forms.CharField(max_length=30,help_text="Enter a teammate's Ingame name here.")
    teammate_3 = forms.CharField(max_length=30,help_text="Enter a teammate's Ingame name here.")
    teammate_4 = forms.CharField(max_length=30,help_text="Enter a teammate's Ingame name here.")
    outcome = forms.CharField(max_length=4,help_text="Enter 'Win' or 'Lose'.")
    mute = forms.CharField(max_length=3,help_text="Did you mute anyone this game? Enter Yes or No.")
    attitude_Score = forms.IntegerField(help_text="Enter a number between 0 and 100. 100 means you're feeling great, 0 means you're very angry/upset.")
    comments = forms.CharField(widget=forms.Textarea,help_text="How are you feeling after the game? Why'd you win or lose? Be brief please.")
