#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define N 10
//LU分解法实现解线性方程组
float sumU(float L[][N] ,float U[][N], int i, int j )
{
    float sU =0;
    for (int k = 1; k <= i-1 ; k++)
    {
        sU += L[i-1][k-1] * U[k-1][j-1];
    }
    return sU;
}//计算求和U

float sumL(float L[N][N] ,float U[N][N], int i, int j )
{
    float sL = 0;
    for (int k = 0; k <= j-1; k++)
    {
        sL += L[i-1][k-1] * U[k-1][j-1];
    }
    return sL;
}//计算求和L
float sumY(float L[N][N] ,float y[N],int i)
{
    float sY=0;
    for (int k = 1; k <= i - 1; k++)
    {
        sY += L[i-1][k-1] * y[k-1];
    }
    return sY;
}//计算求和Y
float sumX(float U[N][N] ,float x[N],int i ,int m)
{
    float sX = 0;
    for (int k = i+1; k <= m; k++)
    {
        sX += U[i-1][k-1] * x[k-1];
    }
    return sX;
}//计算求和X
int main(void)
{
	int i,j,k,t,temp;
    int n;//n为阶数
	printf("请输入矩阵的阶数n: ");
	scanf("%d",&n);
	float max;
    float a[N][N];//a为非奇异矩阵
    float L[N][N] = {0};
    float U[N][N] = {0};//初始化部分
    float b[N],S[N]={0.0};
	int p[N][N]={0};//p为单位矩阵，记录行交换的情况
    printf("请输入[A]------------------------:\n");
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
            scanf("%f",&a[i-1][j-1]);
    }%输入非奇异矩阵A
	//当计算方程阶数为3,7,11时，运行以下程序段A矩阵自动生成
/*    for(i=1;i<=n;i++)
    {
		for(j=1;j<=n;j++)
			a[i-1][j-1]=pow(i,j-1);
    }  
    printf("A矩阵为:---------------\n");
	for(i=1;i<=n;i++)
    {
		for(j=1;j<=n;j++)
			printf("%f   ",a[i-1][j-1]);
		printf("\n");
}%输出A矩阵
for(i=1;i<=n;i++)
{
	if(i==1)
		b[i-1]=(float)n;
	else
	{
		b[i-1]=1;
		for(j=1;j<=n;j++)
			b[i-1]=b[i-1]*i;
		b[i-1]=(float)(b[i-1]-1)/(i-1);
	}
}
printf("b矩阵为:---------------\n");
for(i=1;i<=n;i++)
	printf("%f   ",b[i-1]);*/
    printf("请输入[b]------------------------:\n");
	for(i=1;i<=n;i++)
		scanf("%f",&b[i-1]);
	for(i=1;i<=n;i++)%生成单位矩阵P
	{
		for(j=1;j<=n;j++)
		{
			if(i==j)
				p[i-1][j-1]=1;
			else
				p[i-1][j-1]=0;
		}
	}
	printf("单位矩阵p-------------------------\n");
	for(i=1;i<=n;i++)//输出p矩阵
	{
		for(j=1;j<=n;j++)
			printf("%d   ",p[i-1][j-1]);
		printf("\n");
	}
    //计算L,U
    for (i = 1; i <= n; i++)
    {
            L[i-1][i-1] = 1;//对角线元素为1
            for (j = i; j <= n; j++)
			{
				S[j]=(float)fabs(a[j][i-1] - sumL(L,U,j+1,i));
                U[i-1][j-1] = a[i-1][j-1] - sumU(L,U,i,j);
                if(j+1 <= n) 
			       L[j][i-1]=(float)(a[j][i-1]-sumL(L,U,j+1,i))/U[i-1][i-1];
//i变j+1，j变i 
			}
			for(k=i;k<=n;k++)
			{
				if(S[k]>max)%选主元
				{
					max=S[k];
					t=k;%记录最大元素的行数
				}
			}
			S[t]=max;//第t行为最大值
			for(k=1;k<=n;k++)//交换第k行与第t行元素
			{
				temp=p[i][k];
				p[i][k]=p[t][k];
                p[t][k]=temp;
			}
    }
    //输出U
    printf("U------------------------:\n");
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
            printf("%f   ",U[i-1][j-1]);
        printf("\n");
    }
    //输出L
    printf("L----------------------------:\n");
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
            printf("%f   ",L[i-1][j-1]);
        printf("\n");
    }
	//输出p
	printf("p------------------------------:\n");
    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
            printf("%d   ",p[i-1][j-1]);
        printf("\n");
    }
    //由Ly=b 求y
    float y[N] = {0};
    y[0] = b[0];
    for (i = 2; i <= n; i++)
        y[i-1] = b[i-1] - sumY(L,y,i);
    //由 Ux=y 求x
    float x[N] = {0};
    for(i = n; i >= 1; i--)
        x[i-1] =(float)(y[i-1]-sumX(U,x,i,n))/ U[i-1][i-1];
    //输出y
    printf("y的值----------------------:\n");
    for (i = 0; i < n; i++)
        printf("%f\n",y[i]);
    printf("\n");
    //输出x
    printf("x的值-------------------:\n");
    for (i = 0; i < n; i++)
        printf("%f\n",x[i]);
    printf("\n");
    return 0;
}