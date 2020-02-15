### `https://blog.csdn.net/neweastsun/article/details/51965226`
### itertools.starmap 针对list中的每一项，调用函数功能
```python
import functools,itertools
list(itertools.starmap(lambda x,y: x+y,  [(2,5), (3,2), (10,3)]))
list(itertools.starmap(pow,  [(2,5), (3,2), (10,3)]))
list(itertools.starmap(max,  [(2,5), (3,2), (10,3)]))
```
### functools.partial 原函数固定部分参数
`list(itertools.starmap(functools.partial(max, key=len),  [('aa','bbb'), ('ccc','a'), ('ddd','eeee')]))`

### 依据真假压缩数据
`list(itertools.compress([1,2,'xxx'], [0,1,False]))`
