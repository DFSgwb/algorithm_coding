#include <iostream>
#include <string>
#include <vector>
using namespace std;
string multiply(string num1, string num2) {
    int n1 = num1.size(), n2 = num2.size();
    vector<int> res(n1 + n2);
    for (int i = n1 - 1; i >= 0; i--) {
        for (int j = n2 - 1; j >= 0; j--) {
            int mul = (num1[i] - '0') * (num2[j] - '0');
            int p1 = i + j, p2 = i + j + 1;
            int sum = mul + res[p2];
            res[p1] += sum / 10;
            res[p2] = sum % 10;
        }
    }
    string result;
    for (int i = 0; i < res.size(); i++) {
        if (result.empty() && res[i] == 0) {
            continue;
        }
        result += to_string(res[i]);
    }
    return result.empty() ? "0" : result;
}

int main() {
    cout << multiply("123", "456") << endl;
    cout << multiply("123", "0") << endl;
    cout << multiply("123", "1") << endl;
    cout << multiply("5", "5") << endl;
    cout << multiply("11", "11") << endl;
    return 0;
    }