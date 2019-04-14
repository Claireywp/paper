#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<math.h>

double cos_dis(int v1[],int n,int v2[],int m)
{
	double dot_product = 0.0;  
    double normA = 0.0;  
    double normB = 0.0;
    int a,b;
    
    for(a=0,b=0;a<n && b<m;a++,b++)
	{
		dot_product += pow(v1[a]-v2[b],2); 
        //normA += pow(v1[a],2); 
        //normB += pow(v2[b],2);
	} 
	
	return fabs(1-sqrt(dot_product)/100);
	 
    /*     
    if(normA == 0.0 || normB==0.0)
	{
        return 0;  
    }
    else
	{
		return dot_product / (sqrt((normA*normB)));
	}  
        */
}  
    


int main()
{

	char *s = "¡¶JavaÓïÑÔÏÝÚåÓëÈ±ÏÝ¡·";
	char *c = "¡¶CÓïÑÔÏÝÚåÓëÈ±ÏÝ¡·";
	
	//char *s = "Ò½ÁÆÒÇÆ÷";
	//char *c = "¹ºÎï··Âô»ú";
	
	int num[30],num2[30],i,n=0,m=0;
	
	memset(num,0,sizeof(num));
	memset(num2,0,sizeof(num2));
	
	printf("1:%s\n",s);
	printf("2:%s\n\n",c);
	
	while(*(s + n))
	{
		num[n] = 0XFF&s[n++];
	} 
	
	while(*(c + m))
	{
		num2[m] = 0XFF&c[m++];
	} 
	printf("1:\n");
	for(i = 0;i < n;i++)
	{
		printf("%2X ",num[i]);
	}
	
	printf("\n\n");
	
	for(i = 0;i < n;i++)
	{
		printf("%d ",num[i]);
	}
	
	printf("\n\n2:\n");
	for(i = 0;i < m;i++)
	{
		printf("%2X ",num2[i]);
	}
	
	printf("\n\n");
	
	for(i = 0;i < m;i++)
	{
		printf("%d ",num2[i]);
	}
	
	printf("\n\n");
	
	printf("len:%d %d\n\n",n,m);
	
	double dis = cos_dis(num,n,num2,m);
	
	printf("sim=%.8lf\n",dis);
		
	
	return 0;

}
