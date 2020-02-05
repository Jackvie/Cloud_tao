#! /usr/bin/python3

### 文件用来更新或创建广义的漫画

import re,time,os
import sys
sys.path.insert(0, '/home/yuntao/firstdemo/')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstdemo.settings")
    import django
    django.setup()


def main():
    action, name = input('请输入操作(0:更新; 1:创建)'), input('请输入漫画名:')
    if action == '1':
        pk,status,last_url = input('请输入漫画ID:'),input('请输入漫画状态:'),input('请输入第一页的url')
        assert not Animate.objects.filter(Q(name=name) | Q(id=pk)).exists(), 'ID或漫画名已存在'
        assert int(status) in choices_status, '非法状态'
        Animate.objects.create(id=pk,name=name,status=status,last_url=last_url,last_url_download=True)

    elif action == '0':
        status, last_url, last_url_download = input('请输入漫画状态:'), input('请输入第一页的url'), input('输入任意值 下载当期页 ')
        assert Animate.objects.filter(name=name).exists(), '漫画名已存在'
        animate = Animate.objects.get(name=name)
        if status:
            assert int(status) in choices_status, '非法状态'
            animate.status = status
        if last_url:
            animate.last_url = last_url
        if last_url_download:
            animate.last_url_download = True
        else:
            animate.last_url_download = False
        animate.save()
    else:
        return False
    return True


if __name__ == '__main__':
    from animate.models import Animate, ImageBase
    from django.db.models import Q
    choices_status = [i[0] for i in Animate._meta.get_field('status').flatchoices]  # [0, 1, 2, 3]
    print(main())
