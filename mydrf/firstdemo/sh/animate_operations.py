#! /usr/bin/python3
import re,time,os
import sys
sys.path.insert(0, '/home/yuntao/firstdemo/')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstdemo.settings")
    import django
    django.setup()


def main():
    action, name, pk, status = input('请输入操作(0:更新; 1:创建)'), input('请输入漫画名:'), input('请输入漫画ID:'), input('请输入漫画状态:')
    if action == '0':
        assert ImageBase.objects.filter(animate_id=pk).exists(), '漫画不存在, 请确认漫画图片表中是否有对应数据'
        animate = Animate.objects.filter(id=pk, name=name)
        animate.save()
    elif action == '1':
        assert ImageBase.objects.filter(animate_id=pk).exists(), '漫画不存在, 请确认漫画图片表中是否有对应数据'
        assert not Animate.objects.filter(Q(name=name) | Q(id=pk)).exists(), 'ID或漫画名已存在'
        assert int(status) in choices_status
        Animate.objects.create(id=pk,name=name,status=status)
    else:
        return


if __name__ == '__main__':
    from animate.models import Animate, ImageBase
    from django.db.models import Q
    choices_status = [i[0] for i in Animate._meta.get_field('status').flatchoices]  # [0, 1, 2, 3]
    main()