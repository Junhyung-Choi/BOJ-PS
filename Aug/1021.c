#include <stdio.h>

void decrease(int N[], int current, int num)
{
    int i = current + 1;
    for (i; i < num; i++)
    {
        if (N[i] > N[current])
            N[i]--;
    }
}

int main(void){
    int N[51] = {0};
    int len,num;
    scanf("%d %d",&len,&num);
    for (int i = 0; i < num; i++){
        scanf("%d",&N[i]);
    }
    int sum = 0;
    int now = 1;
    for (int i = 0; i < num; i++){
        if (N[i] > now){
            if ((len-N[i]) + now > (N[i] - now))
                sum += N[i] - now;
            else
                sum += (len-N[i]) + now;
        }
        else
        {
            if (len - now + N[i] > now - N[i])
                sum += now - N[i];
            else
                sum += len - now + N[i];
        }
        now = N[i];
        len--;
        decrease(N,i,num);
    }
    printf("%d", sum);
    return 0;
}