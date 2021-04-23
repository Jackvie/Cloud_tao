#include <stdio.h>

void swap(int *x, int *y);

int main()
{
    int a=100, b=200;
    swap(&a, &b);
    printf("a=%d, b=%d\n", a, b);
}

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}
