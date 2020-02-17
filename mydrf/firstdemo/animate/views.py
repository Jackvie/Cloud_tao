# from django.contrib.auth import get_user_model
# User = get_user_model()
# from django.contrib.auth.models import User
# User.objects.create_user('yuntao', password='yuntao', is_staff=True, is_active=True)
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate
from .models import ImageBase,Animate
from django.core import paginator
import itertools


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='post')
class AnimateView(View):
    def get(self, request):
        try:
            username = request.GET.get('username')
            password = request.GET.get('pwd')
            user = authenticate(username=username, password=password)
            assert user, 'xxxxx'
            # logout(request)
            login(request, user=user)
            data = list(Animate.objects.filter(status__in=[1,2]).values('id','name'))
            animate_id = request.GET.get('animate_id')
            init_data = None

            if animate_id:
                init = ImageBase.objects.filter(animate_id=animate_id,chapter=int(ImageBase.objects.filter(animate_id=animate_id).order_by('chapter').first().chapter)).order_by('name').values_list('relative_path',flat=True)
                init_data = ('<img src="{}" /><br />'*len(init)).format(*init)
                for index, i in enumerate(data):
                    if str(i['id']) == str(animate_id):
                        data.insert(0, data.pop(index))
                        break

            return render(request, './animate.html',{'data':data, 'init_data':init_data})
        except:
            import traceback
            traceback.print_exc()
            return HttpResponse(status=404)

    def post(self, request):
        try:
            chapter = request.POST.get('chapter')
            animate_name = request.POST.get('animate_name')
            data = ImageBase.objects.filter(animate__name=animate_name,chapter=chapter).order_by('name').values_list('relative_path',flat=True)
            #return JsonResponse({'data':[{'url':url} for url in data if url]})
            return HttpResponse(('<img src="{}" /><br />'*len(data)).format(*data))
        except:
            import traceback
            return HttpResponse('{}'.format(traceback.format_exc()), status=404)

@login_required
def animateChapter(request):
    animate_id = request.GET.get('animate_id')
    info = ImageBase.objects.filter(animate_id=animate_id).values('chapter').distinct().order_by('chapter')
    return JsonResponse({'data':list(info)})


@login_required
def getAllanimates(request):
    '''
    active 当期页高亮
    data 分页后当前页以4为长度拆分
    get_page 要获取的第几页
    paginators 分页的信息链接集
    999 默认代表查询全部漫画
    :return:
    '''
    get_page = int(request.GET.get('page', 1))
    get_status = int(request.GET.get('status', 999))
    info = Animate.objects.values('id', 'name', 'cover_photo') if get_status == 999 else Animate.objects.filter(status=get_status).values('id', 'name', 'cover_photo')

    paginator_ = paginator.Paginator(info, 6)
    page = paginator_.page(get_page)
    result = page and list(page)
    pre_next = {'next_page': page.has_next() and '/animate/getAllanimates/?page=%d&status=%d' % (page.next_page_number(), get_status), 'previous_page':page.has_previous() and '/animate/getAllanimates/?page=%d&status=%d' % (page.previous_page_number(), get_status)}

    data = [result[i:i + 4] for i in range(0, len(result), 4)]
    for i in data:
        for j in i:
            j.update({'goto':'/animate/?username=yuntao&pwd=yuntao&animate_id=%s' % j['id']})



    flatchoices = Animate._meta.get_field('status').flatchoices
    flatchoices.append((999, '全部'))
    paginators = [{'active':i==get_page, 'page':i, 'href':'/animate/getAllanimates/?page=%d&status=%d' % (i, get_status)} for i in range(1,paginator_.num_pages+1)]
    status_data = [{'disabled': 'disabled' if i==get_status else '', 'active': 'active' if get_status==i else '', 'status':j,'href':'/animate/getAllanimates/?status=%d' % i} for i,j in flatchoices]
    return render(request, './index.html', {'datas': data, 'paginators':paginators, 'status_data':status_data, 'pre_next':pre_next})




