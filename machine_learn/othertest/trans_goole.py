# https://www.jianshu.com/p/2f9a2b4c3aa3
# pip install googletrans
# https://py-googletrans.readthedocs.io/en/latest/
# https://github.com/ssut/py-googletrans/blob/master/README.rst
from googletrans import Translator
translator = Translator()
print(translator.translate('星期日').text)

from googletrans import Translator
translator = Translator()
print(translator.translate('Sunday', src='en', dest='zh-CN').text)


from googletrans import Translator
translator = Translator()
print(translator.detect('일요일'))
