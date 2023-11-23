from django.shortcuts import render

from .models import Notes
from django.views.generic import CreateView, ListView, DetailView

# Create your views here.

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'list_notes.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'list_note_details.html'

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    template_name = 'add_note.html'
    success_url = '/notes'

def list_notes(request):

    notes = Notes.objects.all()

    return render(request, 'list_notes.html', {'notes' : notes})


def list_note_details(request, pk):

    note = Notes.objects.get(pk=pk)

    return render(request, 'list_note_details.html', {'note' : note})