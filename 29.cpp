#include<bits/stdc++.h>
using namespace std;
int divide(int dividend, int divisor){
    int res=0;
    //两数相除：给定两个整数，将两数相除，在不使用乘除法和mod运算符的情况下返回两数相除的商
    if(dividend<0&&divisor<0||dividend>0 && divisor>0){
        dividend=abs(dividend);
        divisor=abs(divisor);
        while(dividend>=divisor){
            dividend -= divisor;
            res++;
        }
        return res;
    }else{
        if(dividend<0&&divisor<0||dividend>0 && divisor>0){
        dividend=abs(dividend);
        divisor=abs(divisor);
        while(dividend>=divisor){
            dividend -= divisor;
            res++;
        }
        return -res;
        }
    } 
}
int main(){
    int num1=10,num2=3;
    cout<<divide(10, 3)<<endl;
}