from django.shortcuts import render

# Create your views here.
from .models import Group

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups_app/group_list.html', {'groups': groups})