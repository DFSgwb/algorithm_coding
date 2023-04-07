#include<bits/stdc++.h>
using namespace std;
class Solution{
    const long long MOD = 1e9+7;
    public:
        int numberOfCuts(int n){
            //分割圆的最少切割次数
        if(n==1) return 0;
        else if(n%2==0) return n/2;
        else return n;
        }
        vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid){
            //行和列中一和零的差值，模拟就完事了
            int m = grid.size(), n=grid[0].size();
            vector<int> rows1(m), cols1(n);
            for(int i=0;i<m; i++){
                for(int j=0;j<n;j++){
                    rows1[i] += grid[i][j];
                    cols1[j] += grid[i][j];
                }
            }
            for(int i=0;i<m; i++){
                for(int j=0; j<n; j++){
                    grid[i][j] = rows1[i] + cols1[j] -(n-rows1[i]) - (m-cols1[j]);
                }
            }
            return grid;
        }
        int bestClosingTime(string customers){
            //商店的最少代价，两个子串中Y和N的个数，开店期间就算N，关店期间就算Y
            int n = customers.size();
            vector<int> l(n+2, 0), r(n+2, 0);
            for(int i=1; i<=n; i++) l[i] = l[i-1] + (customers[i-1] == 'N');
            for(int i=n; i>=1; i--) r[i] = r[i+1] + (customers[i-1] == 'Y');
            int res = 0, mv = r[1];
            for(int i=1; i<=n+1; i++) {
                if(mv > l[i-1] + r[i]) mv = l[i-1] + r[i], res = i-1;
            }
            return res;
        }
        int countPalindromes(string s){
            //统计回文子序列数目：给你数字字符串s，请你返回s中长度为5的回文子序列数目，答案取模
            int suf[10]{}, suf2[10][10]{}, pre[10]{}, pre2[10][10]{};
            for (int i = s.length() - 1; i >= 0; --i) {
                char d = s[i] - '0';
                for (int j = 0; j < 10; ++j)
                    suf2[d][j] += suf[j];
                ++suf[d];
            }
            long ans = 0L, cur=0;
            for (char d : s) {
                d -= '0';
                --suf[d];
                for (int j = 0; j < 10; ++j){
                    cur-=(long)suf[j]*pre2[d][j];
                    suf2[d][j] -= suf[j]; // 撤销
                }
                ans+=cur;
                /*for (int j = 0; j < 10; ++j)
                    for (int k = 0; k < 10; ++k)
                        ans += (long) pre2[j][k] * suf2[j][k];*/ // 枚举所有字符组合
                for (int j = 0; j < 10; ++j){
                    cur+=(long)pre[j]*suf2[d][j];
                    pre2[d][j] += pre[j];
                }
                ++pre[d];
            }
            return ans % MOD;
        }
};
int main(){
    return 0;
}