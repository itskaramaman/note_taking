from django.shortcuts import render
from .models import Note

# Create your views here.


def home(request):
    if request.method == 'POST':
        import ipdb
        ipdb.set_trace()
        title = request.POST['title']
        content = request.POST['editor']

        note = Note(title=title, content=content, author=user)
        note.save()

    # Sidebar option
    if request.user.is_authenticated:
        notes = Note.objects.order_by('-date')
        context = {'notes': notes}
    return render(request, 'home/home.html')
