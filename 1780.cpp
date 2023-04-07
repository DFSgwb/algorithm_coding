#include<bits/stdc++.h>
using namespace std;
bool checkPowersOfThree(int n) {
    //给你一个整数n，如果你可以将n表示成n个若干个不同的三的幂之和，请你返回true，否则请你返回false
    //对于整个整数y,如果存在整数x满足y==3^x,我们称这个整数y是三的幂
    while (n) {
        if (n % 3 == 2) {
            return false;
        }
        n /= 3;
    }
    return true;   
}
int main(){
    cout<<checkPowersOfThree(12)<<endl;
    return 0;
}