#include<bits/stdc++.h>
using namespace std;
struct ListNode{
    int val;
    ListNode *next;
    ListNode(): val(0), next(nullptr){};
    ListNode(int x): val(x), next(nullptr){};
    ListNode(int x, ListNode *next): val(x), next(next) {}
};
class Solution{
    public:
        int pivotInteger(int n){
            //找出中枢整数：给你一个整数n，找到其中1->x之和与x->n之和相等，如果不存在这样的x则返回-1
            int l=0;
            for(int i=1;i<=n;i++){
                l += i;
                int r=0;
                for(int j=i;j<=n;j++){
                    r += j;
                }
                if(l==r) return i;
            }
            return -1;
        }
        int appendCharacters(string s, string t){
            //追加字符以获得子序列，给你两个仅由小写字母组成的字符串s和t，现在需要通过向s末尾追加字符的方式,双指针实现
            int n=s.size();
            int m=t.size();
            int i=0,j=0;
            while(i<n&&j<m){
                if(s[i]==t[j]){
                    j++;
                }
                i++;
            }
            return m-j;
        }
    ListNode* removeNodes(ListNode* head){
        //从链表中移除节点
        if(head==nullptr || head->next==nullptr) return head;
        ListNode *next_node = removeNodes(head->next);
        if(next_node->val <= head->val){
            head->next = next_node;
            return head;
        }else{
            return next_node;
        }
    }
    int countSubarys(vector<int>& nums, int k){
        //统计中位数为k的子数组，向左右两边寻找大于和小于k个数
        int pos = find(nums.begin(), nums.end(), k)-nums.begin();
        int n =nums.size();
        unordered_map<int, int>res;
        res[0]=1;
        for(int i=pos+1, c=0;i<n;i++){
            c+=nums[i]>k?1:-1;
            ++res[c];
        }
        int ans = res[0] + res[1];
        for(int i=pos-1,c=0;i>=0;--i){
            c += nums[i]<k?1:-1;
            ans += res[c]+res[c+1];
        }
        return ans;
    }
};
int main(){
    return 0;
}