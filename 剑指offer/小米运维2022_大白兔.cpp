#include<bits/stdc++.h>
using namespace std;
int climbStairs(int n) {
        int a;
        int temp1=0;
        int temp2=1;
        int temp;
        if(n==1)
            return 1;
        if(n==2)
            return 2;
        if(n>2)
        {
            for(a=0;a<n;a++)
            {
                temp=temp1+temp2;
                temp1=temp2;
                temp2=temp;
            }   
        }
        return temp;
}
int main(){
    int n;
    cin>>n;
    printf("%d\n",climbStairs(n));
}