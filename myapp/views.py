from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Note
from .utils import calculate_hit_count

class ListNote(View):
    def get(self, request):
        data = Note.objects.all()
        context = {
            'data': data
        }

        return render(request, 'list_note.html', context)


class DetailNoteView(View):
    def get(self, request, id):
        note = get_object_or_404(Note, id=id)
        
        # Hitcountni yangilash
        calculate_hit_count(request, note)

        context = {
            'note': note,
        }
        
        return render(request, 'detail.html', context)