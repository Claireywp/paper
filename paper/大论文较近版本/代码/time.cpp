#include<stdio.h>
#include<stdlib.h>//�õ�rand()����
#include<time.h>   //�õ�clock()����
int main() {
	int begintime,endtime;
	int i = 0;
	int a[1002];
	begintime=clock();	//��ʱ��ʼ
	for( i = 1; i <= 1000; i++){//Ҫ��ʱ�ĳ���
		a[i] = rand()%200-100;//����-100��+100֮��������
		printf("  %d",a[i]);
	}
	endtime = clock();	//��ʱ����
	printf("\n\nRunning Time��%dms\n", endtime-begintime);
	return 0;
}

