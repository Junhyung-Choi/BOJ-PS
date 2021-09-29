#include <iostream>
#include <string>
using namespace std;

string toBinary(int n)
{
    string r;
    while (n != 0)
    {
        r += (n%2==0?"0":"1");
        n /= 2;
    }
    return r;
}

int main(void)
{
    int x,cnt = 0;
    cin >> x;
    string bin = toBinary(x);
    for(int i=0; i<bin.size(); i++)
        if (bin.at(i) == '1') cnt++;
    cout << cnt << endl;
}