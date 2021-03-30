class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
            return false;
        else if (x == 0)
            return true;
        
        string y = "";
        string s = to_string(x);
        while (x > 0) {
            y = y + to_string(x%10);
            x = x/10;
        }
        
        if (s == y)
            return true;
        
        return false; 
    }
};