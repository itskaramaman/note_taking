from django.shortcuts import render, redirect, get_object_or_404
from .models import Note

# Create your views here.


def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST['title']
            content = request.POST['editor']
            note = Note(title=title, content=content, author=request.user)
            note.save()
        else:
            return redirect('login')

    # Sidebar option
    if request.user.is_authenticated:
        notes = Note.objects.filter(author=request.user).order_by('-date')
        context = {'notes': notes}
    else:
        context = {}
    return render(request, 'home/home.html', context)


def note(request, note_id):
    selected_note = get_object_or_404(Note, pk=note_id)
    context = {'note': selected_note}
    return render(request, 'home/note.html', context)
