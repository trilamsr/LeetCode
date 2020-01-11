// @m_brax
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";
        int N = s.size();
        bool dp[N+1][N+1];
        memset(dp, 0, sizeof dp);
        int lo = 0, hi = 0;
        for (int substrlen = 0; substrlen < N; ++substrlen) {
            for (int start = 0; start < N - substrlen; ++start) {
                int end = start + substrlen;
                if (s[start] != s[end]) continue;
                dp[start][end] = (substrlen <= 1) || dp[start+1][end-1];
                if (dp[start][end] && (end - start) > (hi - lo)) {
                    lo = start;
                    hi = end;
                }
            }
        }
        int range = (hi - lo + 1);
        return s.substr(lo, range);
    }
};

// @fulvioabrahao
class Solution {
public:
    int dp[1001][1001];
    string str;
    bool isPalindrome(int i, int j) {
        if (i == j) return true;
        if (i+1 == j) return (str[i] == str[j]);
        if (str[i] != str[j]) return false;
        if (dp[i][j] != -1) return dp[i][j];
        return dp[i][j] = isPalindrome(i + 1, j - 1);
    }
    
    string longestPalindrome(string s) {
        str = s;
        memset(dp, -1, sizeof dp);
        int left = 0, right = 0;
        for (int len = s.size(); len >= 2; len--) {
            for (int i = 0; i < s.size() - len + 1; i++) {
                if (isPalindrome(i, i + len - 1)) {
                    left = i;
                    right = i + len - 1;
                    break;
                }
            }
            if (left !=0 || right != 0) break;
        }
        string ans;
        for (int i = left; i <= right; i++) ans.push_back(s[i]);
        return ans;
    }
};


class Solution {
public:
    int dp[1001][1001];
    string str;
    bool isPalindrome(int i, int j) {
        if (i == j) return true;
        if (i+1 == j) return (str[i] == str[j]);
        if (str[i] != str[j]) return false;
        if (dp[i][j] != -1) return dp[i][j];
        return dp[i][j] = isPalindrome(i + 1, j - 1);
    }
    
    string longestPalindrome(string s) {
        str = s;
        memset(dp, -1, sizeof dp);
        int left = 0, right = 0;
        for (int len = 2; len <= s.size(); len++) {
            for (int i = 0; i < s.size() - len + 1; i++) {
                if (isPalindrome(i, i + len - 1)) {
                    left = i;
                    right = i + len - 1;
                    break;
                }
            }
        }
        string ans;
        for (int i = left; i <= right; i++) ans.push_back(s[i]);
        return ans;
    }
};


