#include <iostream>
#include <string>
using namespace std;

int main(void)
{
    int x,cnt = 0;
    cin >> x;
    while (x != 0)
    {
        cnt += (x%2==0?0:1);
        x/=2;
    }
    cout << cnt << endl;
}