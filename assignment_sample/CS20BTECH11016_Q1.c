#include<stdio.h>
#include<stdlib.h>


int main ()
{
	int n,reverse_n=0,i=10,temp;
	printf("Enter a number : ");
	scanf("%d",&n);
	temp=n;
	while (temp)
	{
		reverse_n*=10;
		reverse_n+=(temp%10);
		temp /= 10;
		
	}
	printf("%d\n",n+reverse_n);
	return 0;
}
