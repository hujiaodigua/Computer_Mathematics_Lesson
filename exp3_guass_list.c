#include <stdio.h>
#include <math.h>
#define MAX 20   //最大维数 

/*https://baike.baidu.com/item/列主元消去法/7011937?fr=aladdin*/

int main()
{
    int n;
    int i,j,k;
    int mi;
    double mx,tmp;
    static double a[MAX][MAX],b[MAX],x[MAX];
    printf("\n 输入方程组的维数:");//输入AX=b的维数
    scanf("%d",&n);
    if(n>MAX)
    {
        return 1;
     } 
     if(n<=0)
     {
        return 1;
     }
     //输入矩阵的值
     printf("\n请输入A矩阵的值:"); 
     for(i=0;i<n;i++)
       for(j=0;j<n;j++) 
         scanf("%lf",&a[i][j]);
           //输入b矩阵 
      printf("\n请输入B矩阵的值:");      
      for(i=0;i<n;i++)
      scanf("%lf",&b[i]);
  
      for(i=0;i<n-1;i++)
      {
        //找主元素--主元素指的是绝对值最大的元素
        for(j=i+1,mi=i,mx=fabs(a[i][i]);j<n;j++)	//首先将绝对值最大元素暂存变量的值设置为初始对角线元素绝对值
        if(fabs(a[j][i])>mx)						//j行i列元素绝对值大于当前对角线的话
        {
            mi=j;
            mx=fabs(a[j][i]);						//将最大元素暂存变量设置为这个j行i列元素的绝对值
          }

        //交换两行--比如绝对值最大的元素为a31那么1,3行交换
        if(i<mi)
        {
            tmp=b[i];
            b[i]=b[mi];
            b[mi]=tmp;
            for(j=i;j<n;j++)
            {
                tmp=a[i][j];
                a[i][j]=a[mi][j];
                a[mi][j]=tmp;
            }
          } 

          //高斯消元 
          for(j=i+1;j<n;j++)
          {
            tmp=-a[j][i]/a[i][i];
            b[j]+=b[i]*tmp;
            for(k=i;k<n;k++)
            a[j][k]+=a[i][k]*tmp;
          }
               }
          //求解方程 
          x[n-1]=b[n-1]/a[n-1][n-1];
          for(i=n-2;i>=0;i--)
          {
              x[i]=b[i];
            for(j=i+1;j<n;j++)
                 x[i]-=a[i][j]*x[j];
                 x[i]/=a[i][i];
            }

                 //输出运行结果 
          printf("solution is :\n");
          for(i=0;i<n;i++)
          printf("%lf\n",x[i]);
          return 0;    

}
