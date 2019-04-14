#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
int main()
{
	
	double run_time=0;

	int j=1;
	while(j<=2)
	{
		printf("Case:%d\n",j++);
		srand(time(NULL));
		int N,M;
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
		
		printf("Please input N and M:");
		scanf("%d %d",&N,&M);
		printf("Please input u1 and u2:");
		scanf("%f %f",&u1,&u2);
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
		begintime=clock();	//计时开始
		/*
		_LARGE_INTEGER time_start;	//开始时间
		_LARGE_INTEGER time_over;	//结束时间
		double dqFreq;		//计时器频率
		LARGE_INTEGER f;	//计时器频率
		QueryPerformanceFrequency(&f);
		dqFreq=(double)f.QuadPart;
		QueryPerformanceCounter(&time_start);	//计时开始
		*/
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
	    //p=rand()/(double)(RAND_MAX);
	    //a=rand()/(double)(RAND_MAX);
	    //s=rand()/(double)(RAND_MAX);
	    //e=rand()/(double)(RAND_MAX);
	    //m=rand()/(double)(RAND_MAX);
	    int tt;
	    i=0;
	    while(i<5){
	    	tt=rand()%5;
	    	switch(tt){
	    		case 0:break;
	    		case 1:p[i]=0.1;break;
	    		case 2:p[i]=0.35;break;
	    		case 3:p[i]=0.6;break;
	    		case 4:p[i]=0.85;break;
	    	}
	    	if(tt==0)
	    	{
	    		continue;
	    	}
	    	i++;
	    }
	    printf("p:%f a:%f s:%f e:%f m:%f\n",p[0],p[1],p[2],p[3],p[4]);
	    
	    risk = (1-p[0])*(1-p[1])*(1-p[2])*(1-p[3])*(1-p[4]);
	    printf("risk:%f\n",risk);
	    /* 
	    if(send==1 && res==1)
	    {
	    	printf("1 1\n");
	    	G1 = risk*(-N+M);
	    	G2 = risk*(3*N-M);
	    	printf("G1:%f G2:%f\n",G1,G2);
	    }
	    else if(send==1 && res==0)
	    {
	    	printf("1 0\n");
	    	G1 = risk*(-N);
	    	G2 = risk*(3*N);
	    	printf("G1:%f G2:%f\n",G1,G2);
	    }
	    else if(send==0 && res==1)
	    {
	    	printf("0 1\n");
	    	G1 = 0;
	    	G2 = 0;
	    	printf("G1:%f G2:%f\n",G1,G2);
	    }
	    else if(send==0 && res==0)
	    {
	    	printf("0 0\n");
	    	G1 = 0;
	    	G2 = 0;
	    	printf("G1:%f G2:%f\n",G1,G2);
	    }
	    else
	    {
	    	printf("Error!\n");
	    }*/
	    
	    
	    printf("1 1\n");
	    G1 = risk*(-N+M);
	    G2 = risk*(3*N-M);
	    printf("G1:%f G2:%f\n",G1,G2);
	    //drr = u1*fore + u2*G1;
	    //printf("drr:%f\n\n",drr);
	    
	    printf("1 0\n");
    	G1 = risk*(-N);
    	G2 = risk*(3*N);
    	printf("G1:%f G2:%f\n",G1,G2);
    	//drr = u1*fore + u2*G1;
	    //printf("drr:%f\n\n",drr);
	    
	    /*
	    QueryPerformanceCounter(&time_over);	//计时结束
		run_time = 1000000*(time_over.QuadPart-time_start.QuadPart)/dqFreq;
	    printf("\nrun_time：%fus\n",run_time);
	    */
	    endtime = clock();	//计时结束
		printf("\n\nRunning Time：%dms\n", endtime-begintime);
		printf("\n\n");
	}
	
	
	//乘以1000000把单位由秒化为微秒，精度为1000 000/（cpu主频）微秒
	
	return 0;

    
} 

