class TT(object):

	def __init__(self, max_params=None):
		self.max_params = max_params

	def __enter__(self):
		print("start-enter")
		return self
		
	def print_(self):
		print self.max_params,'==='
		print 1/0
		#raise('xxx')

	def __exit__(self,exc_type,exc_value,traceback):
		print 'end==='
		print exc_type,exc_value,traceback
		#print type(exc_type),type(exc_value),type(traceback)
		### 只有返回True就代表捕获异常
		return isinstance(exc_value, ZeroDivisionError)


try:
	with TT('xxxxxx') as xx:
		xx.print_()
	print '========================'
except:
	print '---------'
