//给定一个n*n矩阵，实现原地顺时针旋转90度
#include<bits/stdc++.h>
using namespace std;
//先上下对折然后对角反转
void rotate(vector<vector<int>>& matrix){
    int n = matrix.size();
    for(int i=0;i<n/2;i++) matrix[i].swap(matrix[n-i-1]);
    for(int i=0;i<n;i++){
        for(int j=i;j<n;j++){
            swap(matrix[i][j], matrix[j][i]);
        }
    }
}
int main(){
    //int matrix[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
    vector<vector<int> > matrix(4,vector<int>(4));
    int nums[4][4] = {{5,1,9,11},{2,4,8,10},{13,3,6,7},{15,14,12,16}};
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            matrix[i][j] = nums[i][j];
        }
    }
    rotate(matrix);
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
           printf("%3d",matrix[i][j]); 
        }
        cout<<endl;
    }
    return 0;
}