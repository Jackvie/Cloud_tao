#include <stdio.h>
  
// 宏定义在编译时把所有用到宏定义值的地方用宏定义常量替换。const常量可以看作是一个只读变量，需要指定类型，需要分配内存，有自己的作用域。
#define PI 3.1415926
const float Pi = 3.14;

/*定义两个全局变量*/
int x=1;
int y=2;
int addtwonum();
int main(void)
{
    int result;
    result = addtwonum();
    printf("x=%d,y=%d,r=%d\n",x,y,result);
    printf("%f, %f\n", PI, Pi);
    int *ptr;
    ptr = &x;
    printf("%p\n", ptr);
    return 0;
}
#include <stdio.h>
/*外部变量声明*/
extern int x ;
extern int y ;
int addtwonum()
{
    x++;
    y++;
    return x+y;
}
