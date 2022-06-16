# Django
from django.http import Http404

# Local
from .models import Figurine


# Create your views here.
def create_figurine(request):
    # Expects the following request header:
    # {
    #   "name": "",
    #   "description": ""
    #   "size": "",
    #   "bottom_text": ""
    # }

    if request.method == "GET":
        raise Http404(
            "create_figurine can only be called with the POST method."
        )

    name = request.POST.get("name")
    description = request.POST.get("description")
    size = request.POST.get("size")
    bottom_text = request.POST.get("bottom_text")

    figurine = Figurine(
        name=name,
        description=description,
        size=size,
        bottom_text=bottom_text,
    )
    figurine.save()
