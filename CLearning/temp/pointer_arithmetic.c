#include <stdio.h>
 
const int MAX = 3;

void increase();
void decrease();
void compare();

int main()
{
	increase();
	decrease();
	compare();
	return 0;
}

void increase()
{
	int var[3] = {10, 100, 200};
	int i, *ptr;

	ptr = var;
	for (i=0; i<MAX; i++)
	{
		printf("var[%d]=%d,%p\n", i, *ptr, ptr);
		ptr++;
	}
}

void decrease()
{
	char var[3] = {'a', 'b', 'c'};
	int i;
    char *ptr;
	ptr = &var[MAX-1];
	for (i=MAX-1; i>=0; i--)
	{
		printf("var[%d]=%c, %p\n", i, *ptr, ptr);
		ptr--;
	}
}

void compare()
{
	int  var[] = {10, 100, 200};
    int  i, *ptr;
 
    /* 指针中第一个元素的地址 */
    ptr = var;
    i = 0;
    while ( ptr <= &var[MAX - 1] )
	{
		printf("var[%d]=%d, %p\n", i, *ptr, ptr);
		ptr++;
		i++;
	}
}
