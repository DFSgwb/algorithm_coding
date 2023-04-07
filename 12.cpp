#include<bits/stdc++.h>
using namespace std;
//将给定的数字转化为罗马字符
string intToRoman(int num){
    int values[]={1000,900,500,400,100,90,50,40,10,9,5,4,1};
    string reps[]={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
    string result;
    for(int i=0;i<13;i++){
        while(num>=values[i]){
            num-=values[i];
            result += reps[i];
        }
    }
    return result;
}
int main(){
    int num=6;
    string res = intToRoman(num);
    cout<<res<<endl;
    return 0;
}