from django.http import HttpResponse
def show_name (request):
    first_name="Mahboubeh"
    last_name="Jalalifar"
    return HttpResponse({f"Name:{first_name}<br>Lastname:{last_name}"})
# Create your views here.
