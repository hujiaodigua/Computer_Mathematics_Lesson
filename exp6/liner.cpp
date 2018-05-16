#include<iostream>
using namespace std;
const int SIZE=20;
int max(int a, int b)
{
    return ((a>b)?a:b);
}
int main()
{
	int a[SIZE][SIZE];
	int d[SIZE][SIZE];
	int n,i,j;
	int tmp;
cin>>n;
	//输入各结点的值
   	for(i=0;i<n;i++)
	{
		for(j=0;j<=i;++j)
            cin>>a[i][j];
	}
	/*//最底层各结点当前最优解的值，初始状态
	for(j=0;j<n;++j)
        d[n-1][j]=a[n-1][j];
	//其他层各结点当前最优解的值，局部最优解
	for( i=n-2;i>=0;--i)
	{
		for( j=0;j<=i;j++)
		{
			d[i][j]=max(d[i+1][j],d[i+1][j+1])+a[i][j];
		}
	}
	//全局最优解
	cout<<d[0][0]<<endl;*/

	//最顶层只有一个
	d[0][0] = a[0][0];
	//左一溜，1到n-1
	for(i = 1;i <= n-1;++i)
	{
        d[i][0] = a[i][0] + d[i-1][0];
        cout<<"左"<<d[i][0]<<endl;
	}
    //右一溜，1到n-1
	for(i = 1;i <= n-1;++i)
	{
        for(j = 1;j <= n-1;++j)
        {
            if(i == j)
            {
                d[i][j] = a[i][j] + d[i-1][j-1];
                cout<<"右"<<d[i][j]<<endl;
            }
        }
	}
	//中间的i从2到n-1,j从1到n-2
    for(i = 2;i <= n-1;++i)
    {
        for(j = 1;j <= n-2;++j)
        {
            if(i > j)
            {
                d[i][j] = max(d[i-1][j], d[i-1][j-1]) + a[i][j];
                cout<<"中间"<<d[i][j]<<endl;
            }
        }
    }
    //找出最后一行中的最大值
    for(j = 0;j <= n-2;++j)
    {
        tmp = max(d[n-1][j],d[n-1][j+1]);
        d[n-1][j+1] = tmp;
        cout<<"最优"<<d[n-1][j+1]<<endl;
    }
    return 0;
}
