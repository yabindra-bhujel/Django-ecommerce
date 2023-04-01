from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Create your views here.


@user_passes_test(lambda u:u.is_superuser)
def index(request):
    return render(request, 'administration/index.html')
