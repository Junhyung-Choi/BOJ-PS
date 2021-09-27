#include <iostream>
#include <cstring>
#define MAX 1000000
using namespace std;


int main(void)
{
    bool isPrime[MAX+1] = {0,};
    isPrime[0] = true;
    isPrime[1] = true;
    for(int i=2; i<MAX+1; i++)
    {
        if(isPrime[i] == false)
        {
            for(int j=i*2; j<MAX+1; j+=i)
            {
                isPrime[j] = true;
            }
        }
    }

    for(int i=1; i<MAX+1; i++)
    {
        isPrime[i] = !isPrime[i];
    }

    int TC;
    cin >> TC;
    for(int i=0; i<TC; ++i)
    {
        int num,cnt=0;
        cin >> num;
        for(int j=2; j<(num/2)+1; ++j)
        {
            if(isPrime[j] && isPrime[num-j])
            {
                cnt++;
            }
        }
        cout << cnt << endl;
    }
}