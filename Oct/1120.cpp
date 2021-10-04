#include <iostream>
#include <string>
using namespace std;

int main(void)
{
    int cnt;
    int min = 50;
    string a,b;
    cin >> a >> b;
    for(int start=0; start<b.length()-a.length()+1; start++)
    {
        cnt = 0;
        for (int i=0; i<a.length(); i++)
        {
            if(a[i] != b[i+start])
                cnt++;
        }
        if (min >= cnt)
            min = cnt;
    }
    cout << min << endl;
}