# encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import CourseOrg, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operation.forms import UserAskForm


# Create your views here.
class OrgView(View):
    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        all_city = CityDict.objects.all()
        org_nums = all_orgs.count()
        # 热门机构
        hot_orgs = all_orgs.order_by('-click_num')[:3]
        # 对课程机构进行分页
        # 取出帅选的城市
        city_id = request.GET.get("city", '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 类别筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
        # 根据学生人数，课程数排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-courses')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 3, request=request)
        orgs = p.page(page)
        content = {
            'all_orgs': orgs
            , 'all_city': all_city,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            'hot_orgs': hot_orgs,
            'sort': sort
        }
        return render(request, 'org-list.html', context=content)


###ajax异步操作，返回json
class AddUserAsk_View(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            userask_form.save(commit=True)
            return HttpResponse("{'status':'success','message':'成功'}", content_type='application/json')
        else:
            return HttpResponse("{'status':'fail','message:'添加出错'}",content_type='application/json')
