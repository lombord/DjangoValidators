from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.shortcuts import redirect, render

# Create your views here.
from .models import ClubUser


def register(request: HttpRequest):
    context = {}
    if request.method == 'POST':
        tmp = request.POST.dict()
        del tmp['csrfmiddlewaretoken']
        cUser = ClubUser(**tmp)
        try:
            ClubUser.full_clean(cUser)
        except ValidationError as e:
            context = e.message_dict
        else:
            cUser.save()
            return redirect('stub-page')
        request.POST = type(request.POST)()
    return render(request, 'base/register.html', context)


def stubPage(request: HttpRequest):
    return render(request, 'base/stub-page.html')
