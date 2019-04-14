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
		dot_product += v1[a]*v2[b]; 
        normA += pow(v1[a],2); 
        normB += pow(v2[b],2);
	}  
         
    if(normA == 0.0 || normB==0.0)
	{
        return 0;  
    }
    else
	{
		return dot_product / (sqrt((normA*normB)));
	}  
        
}  
    


int main()
{
	
	int num[10]= {1,1,1,0,0,0,0,0,0,0};
	int num2[10]={1,0,0,0,0,1,0,0,1,0};
	int i,n=10,m=10;
	
	printf("len:%d %d\n\n",n,m);
	
	double dis = cos_dis(num,n,num2,m);
	
	printf("sim=%.8lf\n",dis);
		
	
	return 0;

}
