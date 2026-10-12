#include <unordered_map>
#include <vector>

using std::vector;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        std::unordered_map<long long, int> frequencies{{0, 1}};
        frequencies.reserve(nums.size() + 1);
        long long prefix = 0;
        int answer = 0;
        for (const int value : nums) {
            prefix += value;
            const auto found = frequencies.find(prefix - k);
            if (found != frequencies.end()) {
                answer += found->second;
            }
            ++frequencies[prefix];
        }
        return answer;
    }
};
