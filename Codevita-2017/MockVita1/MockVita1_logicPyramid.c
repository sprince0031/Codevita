#include <stdio.h>
int totalElements(int num)
{
	int no = 0;
	while(num>0)
	{
		no += num;
		num--;
	}
	//printf("%d\n", no);
	return no;
}
int main()
{
	int N, totalNo;
	scanf("%d", &N);
	totalNo = totalElements(N);
	return 0;
}