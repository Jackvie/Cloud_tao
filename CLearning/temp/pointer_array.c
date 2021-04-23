#include <stdio.h>
 
const int MAX = 3;

int main()
{
	int var[] = {10, 20, 30};
	int i, *ptr[MAX];
    for (i=0;i<MAX;i++)
	{
		ptr[i] = &var[i];
	}
	for (i=0;i<MAX;i++)
	{
		printf("var[%d]=%d\n", i, *ptr[i]);
	}
	// 指针变量var是var第一个元素地址
	// 指针变量ptr是ptr第一个元素地址
    printf("%d, %d \n", **ptr, *var);
    printf("===============\n");
	const char *names[] = {"abc", "qwe", "rty", "mmm"};
    for ( i = 0; i < MAX; i++)
	{
        printf("Value of names[%d] = %s\n", i, names[i] );
	}

	// 字符串 实际是 字符数组 第0个元素地址的格式化输出
	char test[] = {'a', 'b', 'c', 'd', 'e'};
    printf("%p %p \n", test, &test[0]);
    printf("%s %s \n", test, &test[0]);
    char test2[] = "qwert";
    printf("%s %s\n", test2, &test2[0]);

	// 二维指针数组
	char *ptr_array[3][3]={{"asdx","qwer","fdsfaf"},{"44444","555","6666"},{"a78x","q3er","f2f"}};
	printf("%s \n", ptr_array[1][0]);

	return 0;
}
