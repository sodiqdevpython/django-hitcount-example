from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Note

class ListNote(View):
    def get(self, request):
        data = Note.objects.all()
        context = {
            'data': data
        }

        return render(request, 'list_note.html', context)

from hitcount.views import HitCountMixin
from hitcount.utils import get_hitcount_model

class DetailNoteView(View, HitCountMixin):
    def get(self, request, id):
        note = get_object_or_404(Note, id=id)

        hit_count = get_hitcount_model().objects.get_for_object(note)
        self.hit_count(request, hit_count)

        context = {
            'note': note,
        }
        return render(request, 'detail.html', context)
