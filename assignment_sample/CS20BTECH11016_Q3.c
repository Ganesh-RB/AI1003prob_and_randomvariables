#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

bool pangram(char *str,size_t n)
{
	int i=0,j,flag=0;
	for (i = 0; i < 26; i += 1)
	{
		flag =0;
		for (j = 0; j < n; j += 1)
		{
			if (str[j]==65+i || str[j]==96+i)
			{
				flag = -1;
			}
		}
		
		if (!flag)
		{
			return false;
		}
	}
	
	return true;
}

int main ()
{
	char str1[100],str[]="A quick brown fox jumps over the lazy dog";
	
	FILE *f;
	if (pangram(str,sizeof(str))==true)
	{
		printf("%s : is pangram\n",str);
	}
	
	printf("\n\n***Printing pangram strings from sentences.txt***\n\n");	

	f=fopen("sentences.txt","r");
	if (f==NULL)
	{
		printf("file not open\n");
	}


	while(!feof(f) && !ferror(f))
	{
		fgets(str1,100,f);

		if (pangram(str1,sizeof(str1))==true)
		{
			printf("%s",str1);
		}

	}
	
	return 0;
}
