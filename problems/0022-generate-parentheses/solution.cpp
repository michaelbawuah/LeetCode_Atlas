#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> answers;
        string path;
        path.reserve(static_cast<string::size_type>(2 * n));
        extend(0, 0, n, path, answers);
        return answers;
    }

private:
    static void extend(int opened, int closed, int n, string& path, vector<string>& answers) {
        if (closed == n) {
            answers.push_back(path);
            return;
        }
        if (opened < n) {
            path.push_back('(');
            extend(opened + 1, closed, n, path, answers);
            path.pop_back();
        }
        if (closed < opened) {
            path.push_back(')');
            extend(opened, closed + 1, n, path, answers);
            path.pop_back();
        }
    }
};
