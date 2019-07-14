'''是否回文'''
n1 = 1987523
n2 = 134565431

class IsOrNot(object):
    """判等整数是否为回文"""

    def __init__(self, num = None):
        if not isinstance(num, int):
            raise ValueError("不是整数")
        self.num = num

    def __much(self):
        """判断位数"""
        i = 10
        j = 0
        while True:
            ret = self.num // i
            j += 1
            if ret == 0:
                return j
            i *= 10

    @staticmethod
    def __result(l):
        """列表判等"""
        ll = l[:]
        l.reverse()
        if ll == l:
            return True
        return False

    def isPalindrome_str(self):
        """字符串法"""
        return self.__result(list(str(self.num)))

    def isPalindrome_int(self):
        """整数法"""
        return self.__result([self.num // 10 ** i % 10 for i in range(self.__much())])

print(IsOrNot(n1).isPalindrome_str())
print(IsOrNot(n1).isPalindrome_int())
print(IsOrNot(n2).isPalindrome_str())
print(IsOrNot(n2).isPalindrome_int())
print(IsOrNot('a132').isPalindrome_int())