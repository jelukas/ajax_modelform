# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import NoteForm


def home(request):
	if request.method == 'POST':
		note_form = NoteForm(request.POST)
		if note_form.is_valid(): 
			#do something
			#note_form.save()
			HttpResponseRedirect('/thanks/')
	else:
		note_form = NoteForm()
	return render_to_response('notes/home.html',{'note_form': note_form},context_instance=RequestContext(request))