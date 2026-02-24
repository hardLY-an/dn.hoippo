#include <iostream>

using namespace std;

int main()
{
    ushort n,d,count = 0;
    cin >> n;
    cin >> d;
    
    ushort A[n];
    
    for (ushort i = 0; i < n; i++) 
    {
            cin >> A[i];
    }
    for ( ushort i = 0; i < n; i++ )
    {
        for ( ushort j = i + 1; j < n; j++ )
        {
            if ( ( A[j]- A[i] ) != d)
            {
                continue;
            }
            for ( ushort k = j + 1; k < n; k++ )
            {
                    if ( (A[j] - A[i]) != d )
                    {
                        continue;
                    }
                    
                    if( (A[k] - A[j]) != d )
                    {
                        continue;
                    }
                    
                    //cout << "A[i] = " << A[i] << " " << "A[j] = " << A[j] << " " << "A[k] = " << A[k] << "\r\n";
                    if (  A[k] - A[j] == d and A[k] > A[j]  and A[j] > A[i] )
                    {
                        //cout << "\r\n" <<"Ok" << "\r\n";
                        count += 1;
                        break;
                    }
            }
        }
    }
    
    cout << count;
    
    //cout << n << " " << d;
}
