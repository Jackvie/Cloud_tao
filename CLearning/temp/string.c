#include <stdio.h>
#include <string.h>
 
int main ()
{
   char site1[7] = {'R', 'U', 'N', 'O', 'O', 'B', '\0'};
   char site2[] = "RUNOOB";
 
   printf("菜鸟教程: %s %s\n", site1, site2 );
   for (int i=0;i<7;i++)
   {
       printf("%c=", site2[i]);
   } 
   printf("\n");
   printf("strlen--%lu,%lu\n", strlen(site2), strlen(site1));
   printf("strcmp--%d\n", strcmp(site2, site1));
   return 0;
}

