from django.http import HttpResponseRedirect
from django.urls import reverse


def custom_404_view(request, exception):
    return HttpResponseRedirect(reverse('login'))
