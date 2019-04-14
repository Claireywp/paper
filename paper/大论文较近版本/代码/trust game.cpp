#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
int main()
{
	srand(0);
	double run_time=0;

	int j=1;
	int t;
	
	int N[52] = {0,40,98,84,1,75,6,41,99,21,23,99,57,52,43,22,47,61,13,69,38,39,97,35,75,46,101,37,60,93,33,39,56,100,87,61,21,35,55,22,55,63,15,88,41,5,29,98,63,24,75,16};
	
	int M[52] = {0,85,76,116,3,209,15,109,106,23,50,62,42,98,73,56,101,87,37,50,24,66,68,99,81,88,183,38,123,160,47,104,131,271,80,56,17,90,79,24,120,129,37,112,92,5,87,111,171,37,45,7};
	
	float g11[52];
	float g12[52];
	float g21[52];
	float g22[52];  

	while(j<=50)
	{
		printf("Case:%d\n",j);
		
		
		float u1,u2;
		float x[6];
		int i;
		int begintime=0,endtime=0;
		float p[5];
		float risk;
		float G1,G2;
		int pro=1;
		int next=11;
		int count=0;
	    float drr=0;
	    float fore=0;
	    float trend=0;
	    int send=rand()%2;
	    int res=rand()%2;
	    
		
		printf("N:%d  M:%d\n",N[j],M[j]);
		
		printf("Please input x[5]:\n");
		x[0]=0;
		for(i=1;i<=5;i++)
		{
			printf("x[%d]:",i);
			scanf("%f",&x[i]);
			fore = fore + x[i];
			if(x[i]>x[i-1])
			{
				count++;
			}
		}
		
		count = count-1;
		
		fore = fore/5;
		printf("fore:%f\n",fore);
		
		switch(count){
			case 0:trend=0.1;break;
			case 1:trend=0.3;break;
			case 2:trend=0.5;break;
			case 3:trend=0.7;break;
			case 4:trend=0.9;break;
		}
		printf("trend:%f\n",trend);
		fore = fore*trend;
		printf("new fore:%f\n",fore);

		u1=0.5;
		u2=0.5;

		
//		begintime=clock();	//计时开始
	
	    risk = 0.9;
	    
	    printf("1 1\n");
	    g11[j] = risk*(-N[j]+M[j]);
	    g12[j] = risk*(3*N[j]-M[j]);
	    printf("G11:%f G12:%f\n",g11[j],g12[j]);
	    drr = u1*fore + u2*g11[j];
	    printf("drr1:%f\n\n",drr);
	    
	    printf("1 0\n");
    	g21[j] = risk*(-N[j]);
    	g22[j] = risk*(3*N[j]);
    	printf("G21:%f G22:%f\n",g21[j],g22[j]);
    	drr = u1*fore + u2*g21[j];
	    printf("drr2:%f\n\n",drr);
	    
//	    endtime = clock();	//计时结束
//		printf("\nRunning Time：%dms\n", endtime-begintime);
//		
		j++;
	}
	
	for(j=1;j<=50;j++)
	{
		printf("%.2f   %.2f   %.2f   %.2f\n",g11[j],g12[j],g21[j],g22[j]);
	}
	
	//乘以1000000把单位由秒化为微秒，精度为1000 000/（cpu主频）微秒
	
	return 0;

    
} 

