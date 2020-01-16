#https://www.jianshu.com/p/2f9a2b4c3aa3
#pip install googletrans
from googletrans import Translator
translator = Translator()
print(translator.translate('星期日').text)

from googletrans import Translator
translator = Translator()
print(translator.translate('Sunday', src='en', dest='zh-CN').text)


from googletrans import Translator
translator = Translator()
print(translator.detect('일요일'))
