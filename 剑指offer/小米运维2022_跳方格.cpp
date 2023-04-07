#include<bits/stdc++.h>
using namespace std;
#define Maxsize 1001
bool canJump(vector<int>& nums) {
		int max_index=0; //每次跳跃以后的最大边界
        int step=0; //记录跳跃步数
        int end=0; //每一次搜完一层以后更新end，并且将步数加1，直到可以跳到最后一格
        for(int i=0;i<nums.size()-1;i++)
        {
            if(max_index>=i)
            {
                max_index=max(max_index,i+nums[i]); //找到下次可以到达的最远边界。
                if(i==end) //如果已经搜完了这一层，就把步数加1，并更新end的位置。
                {
                    end=max_index;
                    step++;
                }
            }
        }
        return step;
    }
