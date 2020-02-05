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
            data = Animate.objects.filter(status__in=[1,2]).values('id','name')
            return render(request, './index.html',{'data':data})
        except:
            import traceback
            traceback.print_exc()
            return HttpResponse(status=404)

    def post(self, request):
        try:
            chapter = request.POST.get('chapter')
            animate_name = request.POST.get('animate_name')
            data = ImageBase.objects.filter(animate__name=animate_name,chapter=chapter).order_by('name').values_list('relative_path',flat=True)
            return JsonResponse({'data':[{'url':url} for url in data if url]})
        except:
            import traceback
            return HttpResponse('{}'.format(traceback.format_exc()), status=404)

@login_required
def animateChapter(request):
    animate_id = request.GET.get('animate_id')
    info = ImageBase.objects.filter(animate_id=animate_id).values('chapter').distinct().order_by('chapter')
    return JsonResponse({'data':list(info)})

