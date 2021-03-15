#include <stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void)
{
  int t,i=0,j=0,k=0,cnt=0,l=0,flag=0,pow_2;
  scanf("%d",&t);
  int *n=(int*)calloc(t,sizeof(int));
  int **arr=(int**)malloc(t*sizeof(int*));
  for(i=0;i<t;i++)
  {
    scanf("%d",&n[i]);
    arr[i]=(int*)calloc(n[i],sizeof(int));
    for(j=0;j<n[i];j++)
    scanf("%d",&arr[i][j]);
  }

for(i=0;i<t;i++)
{
  cnt=0;
  for(j=0;j<n[i]-1;j++)
  {
    if(arr[i][j]>arr[i][j+1])
    {
      flag=0;
      for(k=1;k<8;k++)
     {
       if(pow(2,k)*arr[i][j+1]==arr[i][j])
       {
         flag=-1;
         cnt=cnt+k-1;
       }
      }
      if(flag==0)
      {
        k=(int)((log(arr[i][j])-log(arr[i][j+1]))/(log(2)));
        cnt=cnt+k;
      } 
        
    }

    else
    {
      
      flag=0;
      for(k=1;k<8;k++)
     {
       if(pow(2,k)*arr[i][j]==arr[i][j+1])
       {
         flag=-1;
         cnt=cnt+k-1;
       }
      }
      if(flag==0)
      {
        k=(int)((log(arr[i][j+1])-log(arr[i][j]))/(log(2)));
        cnt=cnt+k;
      } 
        
    }
  }
  printf("%d\n",cnt);
}

  return 0;
}