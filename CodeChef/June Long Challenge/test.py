#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int x;
    cin >> x ;
    
    for( int a = 0; a < x; a = a + 1 ) {
      long int ts;
      cin >> ts;
      
      if ( ts % 2 == 0){
          long int ts1 = ts;
          int count = 0;
          
          while(ts1%2 == 0){
            ts1 = ts1/2;
            count++;
          }
          double answer;
          answer = floor(ts1/2);
          cout<< answer;
          
      }
      else{
          double answer;
          answer = floor(ts/2);
          cout<< answer;
      }
   }

    return 0;
}