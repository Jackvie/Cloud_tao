#include <stdio.h>
#include <time.h>
#include <stdlib.h> 
 
void getSeconds(unsigned long *par);
double getAverage(int *arr, int size);
int * getRandom( );
int max(int, int);
void populate_array(int *array, size_t, int (*getNextValue)(void));
int getNextRandomValue(void);

int main ()
{
   unsigned long sec;
   getSeconds( &sec );
   /* 输出实际值 */
   printf("Number of seconds: %ld\n", sec );

   int balance[5] = {1000, 2, 3, 17, 50};
   double avg;
   avg = getAverage( balance, 5 ) ;
   printf("Average value is: %f\n", avg );

   int *p;
   int i;
   p = getRandom();
   for ( i = 0; i < 10; i++ )
   {
       printf("*(p + [%d]) : %d-%d\n", i, *(p + i),p[i] );
   }

   int (*pmax)(int, int) = &max; // &可以省略
   int d;
   d = pmax(pmax(1, 5), 4);
   printf("%d \n", d);

   int myarray[10];
   populate_array(myarray, 10, getNextRandomValue);
   for(int i = 0; i < 10; i++) {
       printf("%d ", myarray[i]);
   }
   printf("\n");
   return 0;
}

void getSeconds(unsigned long *par)
{
   /* 获取当前的秒数 */
   *par = time( NULL );
   return;
}
double getAverage(int *arr, int size)
{
  int    i, sum = 0;      
  double avg;          
 
  for (i = 0; i < size; ++i)
  {
    sum += arr[i];
  }
 
  avg = (double)sum / size;
 
  return avg;
}

int * getRandom( )
{
   static int  r[10];
   int i;
 
   /* 设置种子 */
   srand( (unsigned)time( NULL ) );
   for ( i = 0; i < 10; ++i)
   {
      r[i] = rand();
      printf("%d======\n", r[i] );
   }
 
   return r;
}

int max(int x, int y)
{
    return x > y ? x : y;
}

// 获取随机值
int getNextRandomValue(void)
{
    return rand();
}
// 回调函数
void populate_array(int *array, size_t arraySize, int (*getNextValue)(void))
{
    for (size_t i=0; i<arraySize; i++)
        array[i] = getNextValue();
}
