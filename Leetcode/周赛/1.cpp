#include<bits/stdc++.h>
using namespace std;

int pivotInteger(int n){
            //找出中枢整数：给你一个整数n，找到其中1->x之和与x->n之和相等，如果不存在这样的x则返回-1
            int l=0;
            int c=n/2;
            cout<<c<<endl;
            for(int i=0;i<c;i++){
                l += i; 
            }
            for(int i=c;i<=n;i++){
                l += i;
                int r=0;
                for(int j=i;j<=n;j++){
                    r += j;
                }
                if(l==r) return i;
            }
            return -1;
}
int main(){
    int x;
    x=pivotInteger(8);
    cout<<x<<endl;
    return 0;
}