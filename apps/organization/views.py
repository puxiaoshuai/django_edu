# encoding:utf-8
from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg, CityDict


# Create your views here.
class OrgView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        all_city = CityDict.objects.all()
        content = {
            'all_orgs': all_orgs
            , 'all_city': all_city
        }
        return render(request, 'org-list.html', context=content)
