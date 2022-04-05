from django.shortcuts import render
from familyapp.models import Family



# Create your views here.
def family(request):
    family_member = Family.objects.all()
    return render(request, 'familyapp/family.html', {'family': family_member})