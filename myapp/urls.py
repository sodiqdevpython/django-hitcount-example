from django.urls import path
from .views import ListNote, DetailNoteView

urlpatterns = [
    path('', ListNote.as_view(), name='main'),
    path('<int:id>/', DetailNoteView.as_view(), name='detail')
]