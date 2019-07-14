def _fn(n=100, i=10, j=5, m=2):
    """n元=10*x+5*y+2*z  成立与否"""
    x = n // i
    y = n % 10 // 5
    if n % 10 % 5 % 2 == 0:
        z = n % 10 % 5 // 2
        return "{}={}*{} + {}*{} + {}*{}".format(n, i, x, j, y, m, z)
    return False

if __name__ == '__main__':
    print(_fn(29))
    print(_fn(395))
    print(_fn(8))
    print(_fn(7))
"""
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 算法题如下，求讲解 现有i张十元纸币，j张五元纸币，k张两元纸币，购物后要支付n元(i，j，k，n为整数)。\n",
    "# 要求编写一个复杂度O(1)的函数FindSolution(i,j,k,n)功能是计算出能否用现在手上拥有的纸币是否足够并能刚好拼凑齐n元，而不是找零。 \n",
    "# 1.如果可以，在屏幕输出一个方案并结束；(例子:‘需要2张十元纸币，1张五元纸币，1张两元纸币，刚好可凑齐27元’) \n",
    "# 2.如果不可以，在屏幕输出‘不能刚好凑齐n元’。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def succeed(res):\n",
    "    print('需要{}张十元纸币，{}张五元纸币，{}张两元纸币，刚好可凑齐{}元'\n",
    "          .format(res['n_10'], res['n_5'], res['n_2'], res['n']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def failed(n):\n",
    "    print('不能刚好凑齐{}元'.format(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def FindSolution(i, j, k, n):  # 10, 2, 0, 23\n",
    "    # 用字典保存结果\n",
    "    res = {'n_2':0, 'n_5':0, 'n_10':0, 'n':n}\n",
    "    \n",
    "    # 如果总金额是奇数，说明至少需要一张5元，这时先拿出一张5元，总金额变成了偶数\n",
    "    # 如果5元纸币的数量为0，则拼凑失败\n",
    "    if n%2 == 1:\n",
    "        res['n_5'] += 1   # n_5 =1\n",
    "        j -= 1   # j=1\n",
    "        n -=5    # n = 18\n",
    "        if j<0 or n<0:\n",
    "            failed(res['n'])\n",
    "            return\n",
    "\n",
    "    # 总金额是偶数\n",
    "    \n",
    "    # 此时5元纸币的数量为奇数，不管怎么拼凑，最后肯定会至少剩下一张5元，相当于有一张5元不起任何作用，这里直接丢掉一张5元\n",
    "    if j%2==1: \n",
    "        j-=1    # j = 0 \n",
    "\n",
    "    # 此时如果手上所有纸币的总和小于n，拼凑失败\n",
    "    if i*2 + j*5 + k*10 < n:\n",
    "        failed(res['n'])\n",
    "        return\n",
    "    \n",
    "    # 任意偶数的总金额n，个位数只能用2元纸币来凑，先把个位的钱数凑出来\n",
    "    res['n_2'] += (n%10)/2   # n_2 = 4\n",
    "    i -= (n%10)/2   # i = 6\n",
    "    n -= (n%10)   # n = 10\n",
    "    \n",
    "    # 用2元纸币凑完个位之后，纸币数量变为负数，说明2元纸币不足，拼凑失败\n",
    "    if i<0:\n",
    "        failed(res['n'])\n",
    "        return\n",
    "    \n",
    "    # 此时总金额只剩下整10的数需要凑\n",
    "    # 从10元的纸币开始拿，10元不够拿5元，5元不够拿2元，最后，如果2元的纸币不够，则拼凑失败\n",
    "    if k*10 <= n:  # i=6, j=0, k=0\n",
    "        res['n_10'] += k\n",
    "        n -= k*10\n",
    "\n",
    "        if j*5 <= n:\n",
    "            res['n_5'] += j\n",
    "            n -= j*5\n",
    "\n",
    "            if i*2 < n:\n",
    "                failed(res['n'])\n",
    "                return\n",
    "            else:\n",
    "                res['n_2'] += n/2  # n_2 = 9\n",
    "                succeed(res)\n",
    "        else:\n",
    "            res['n_5'] += n/5\n",
    "            k -= n/5\n",
    "            n -= n/5\n",
    "            succeed(res)\n",
    "    else:\n",
    "        res['n_10'] += n/10\n",
    "        k -= n/10\n",
    "        n -= n/10\n",
    "        succeed(res)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "需要0张十元纸币，1张五元纸币，9.0张两元纸币，刚好可凑齐23元\n"
     ]
    }
   ],
   "source": [
    "FindSolution(10, 2, 0, 23)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
"""
