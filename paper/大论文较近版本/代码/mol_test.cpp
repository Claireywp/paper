#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
int main()
{
	
	double run_time=0;

	int j=0;
	int t;
	int i;
	float drr[50];
	srand(3);
	while(j<1)
	{
//		printf("Case:%d\n",j);

		int N=40;
		int M=85;
		float u1,u2;
		float x[51]= {0,0.4836,0.3846,0.5842,0.5498,0.6778,0.5814,0.527,0.5592,0.742,0.4294,
	0.5334,0.6804,0.557,0.565,0.4406,0.4426,0.3544,0.3658,0.5646,0.4612,0.5476,
	0.5134,0.6464,0.4434,0.6742,0.5344,0.596,0.7046,0.5324,0.6702,0.2318,0.3866,
	0.5266,0.5768,0.5352,0.7488,0.745,0.6758,0.4904,0.597,0.4696,0.5004,0.5658,
	0.3326,0.3158,0.4934,0.5142,0.5156,0.58,0.539};
		int begintime=0,endtime=0;
		float p[5];
		float risk;
		float G1,G2;
		int pro=1;
		int next=11;
		int count=0;
//	    float drr=0;
	    float fore=0;
	    float trend=0;
	    int send=rand()%2;
	    int res=rand()%2;
		
		for(i=1;i<=50;i++)
		{
			fore = fore + x[i];
			if(x[i]>x[i-1])
			{
				count++;
			}
		}
		
		count = count-1;
		
		fore = fore/50;
		
		switch(count){
			case 0:trend=0.1;break;
			case 1:trend=0.3;break;
			case 2:trend=0.5;break;
			case 3:trend=0.7;break;
			case 4:trend=0.9;break;
		}
		fore = fore*trend;

		u1 = 0.1;
		u2 = 1-u1;

		printf("u1:%f  u2:%f\n",u1,u2);
	
		int tt;
		tt=rand()%5;
		switch(tt){
    		case 0:risk=0.9;break;
    		case 1:risk=0.9;break;
    		case 2:risk=0.65;break;
    		case 3:risk=0.4;break;
    		case 4:risk=0.15;break;
    	}
    	
    	printf("unrisk:%f\n",risk);
	    
	    printf("1 1\n");
	    G1 = risk*(-N+M);
	    G2 = risk*(3*N-M);
	    printf("G1:%f G2:%f\n",G1,G2);
	    drr[j] = u1*fore + u2*G1;
	    printf("drr:%f\n\n",drr[j]);
		j++;
	}
	printf("\n\nDRR_lie:\n");
	for(i=0;i<1;i++)
	{
		printf("%.3f\n",drr[i]);
	}
	
	printf("\n\nDRR_line:\n");
	for(i=0;i<1;i++)
	{
		printf("%.3f,",drr[i]);
	}
	
	return 0;

    
} 

