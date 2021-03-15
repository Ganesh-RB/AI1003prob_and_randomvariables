#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
#define SIZE 100


bool isPrime(const void* ptr)
{
	int n=*((int*)ptr);
	if (n==1)
	{
		return false;
	}
	for(int i=2;i<n;i++)
	{
		if(n%i==0)
		return false;
	}
	return true;
}

size_t filter(void* out_put_arr,void* input_arr,size_t arr_size,size_t elem_size,bool (*pred)(const void*))
{
	size_t count=0;
	char *ptr_i=(char*)input_arr,*ptr_o=(char*)out_put_arr;
	
	for ( int i = 0;i < arr_size; i++)
	{
		if (pred((const void*)(ptr_i + i*elem_size)))
		{
			*(ptr_o + count*elem_size)=*(ptr_i + i*elem_size);
			count++;
		}
	}
	
	return count;
}


int main ()
{
	int inp_arr[SIZE],output_arr[SIZE],count,i;
	for (i = 0;  i < SIZE;  i += 1)
	{
		inp_arr[i]=i+1;
		output_arr[i]=0;
	}

	
	count=filter((void*)output_arr,(void*)inp_arr,SIZE,sizeof(int),isPrime);

	for (i = 0; i < count; i += 1)
	{
		printf("%d\n",output_arr[i]);
	}
        
	
	return 0;
}
