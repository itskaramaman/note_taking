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


def delete_note(request, note_id):
    selected_note = get_object_or_404(Note, pk=note_id)
    selected_note.delete()
    return redirect('home')


def edit_note(request, note_id):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['editor']
        note = Note.objects.filter(pk=note_id).update(
            title=title, content=content)

        return redirect('home')

    selected_note = get_object_or_404(Note, pk=note_id)
    title = selected_note.title
    content = selected_note.content
    context = {
        'title': title,
        'content': content,
        'note_id': note_id
    }
    return render(request, 'home/edit_note.html', context)


def save_pdf(request, note_id):
    note = get_object_or_404(Note, note_id)
    title = note.title
    content = note.content
    pass
