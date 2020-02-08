#! /usr/bin/python3

### 使用漫画名获取封面链接并保存图片
### python3 sh/getanimatecoverphoto.py

import re,time,os
import sys
sys.path.insert(0, '/home/yuntao/firstdemo/')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstdemo.settings")
    import django
    django.setup()


def main(name):
    animate= Animate.objects.get(name=name)
    url = 'https://oss.bidong8.com/{}/thumb.jpg'.format(animate.id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML    , like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    response = requests.get(url, headers=headers, verify=False, timeout=5)
    assert response.status_code==200, response.content
    filedir = './animate/static/images/{}'.format(animate.id)
    if not os.path.exists(filedir):
        os.system('mkdir -p {}'.format(filedir))  # 调用系统命令行来创建文件
    with open(filedir+'/thumb.jpg', 'wb') as f:
        f.write(response.content)
    animate.cover_photo = '/static/images/{}/thumb.jpg'.format(animate.id)
    animate.save(update_fields=['cover_photo'])


if __name__ == '__main__':
    import requests
    requests.packages.urllib3.disable_warnings()
    from animate.models import Animate

    name = input('请输入漫画的名字')
    if name != "flushall":
        main(name)
    else:
        for each in Animate.objects.values_list('name',flat=True):
            main(each)
    os.system('python3  manage.py collectstatic --noinput')
    os.system('rm -rf animate/static/images/*')