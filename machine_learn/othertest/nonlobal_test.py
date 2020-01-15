def fn():
	a = 123
	def wa(xxx):
		nonlocal a
		a += xxx
		return a
	return wa
d = fn()
print(d(333))
print(d(333))
print(d(333))
