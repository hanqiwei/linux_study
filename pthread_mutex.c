#include <stdio.h>
#include <pthread.h>	

pthread_mutex_t mutex;

int count = 0;

void *print_msg(void *arg)
{
	int i = 0;
	pthread_mutex_lock(&mutex);//上锁
	for(i = 0; i < 10; ++i) {
		printf("Hello world! This is pthread%d.\n", (int)arg);
		sleep(2);
		
		switch ((int)arg) {
			case 1: printf("the count = %d\n", count);
					break;
			case 2: count++;
					break;
		}
	}
	pthread_mutex_unlock(&mutex);//解锁
    
	printf("the count = %d\n", count);
}

int main()
{
	int ret = 0;

	pthread_t pt1;
	pthread_t pt2;
	//初始化一个锁
	pthread_mutex_init(&mutex,NULL);
	//创建一个线程
	pthread_create(&pt1, NULL, print_msg, (void*)1);
	pthread_create(&pt2, NULL, print_msg, (void*)2);

	ret = pthread_join(pt1, NULL); //等待线程pt1结束
	if(ret) {
		printf("pt1:pthread_join failed!\n");
		return -1;
	} else {
		printf("pt1:OK\n");
	}
	
	ret = pthread_join(pt2, NULL); //等待线程pt2结束
	if(ret) {
		printf("pt2:pthread_join failed!\n");
		return -1;
	} else {
		printf("pt2:OK\n");	
	}
	//销毁一个锁
	pthread_mutex_destroy(&mutex);
	
	return 0;
}
