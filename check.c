#include<stdio.h>
void check(int *a,int n)
{
	int i,j,temp=0;
	for(i=0;i<n;i++)
	{
		temp=*(a+i);
		for(j=i+1;j<n;j++)
		{
			if(temp==*(a+j))
			{
				*(a+j)=0;
			}			
		}
	}
	
}

void main()
{
	int i,n,a[10];
	printf("Enter the size\n");
	scanf("%d",&n);
	printf("Enter the elements\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
		
	}
	
	printf("Before\n");
	for(i=0;i<n;i++)
	{
		printf("%d\t",a[i]);
		
	}
	check(a,n);
	printf("\nAfter\n");
	for(i=0;i<n;i++)
	{
		printf("%d\t",a[i]);
		
	}
}