class Solution {
public:
    std::vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> numMap;
        for (int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            auto iterator = numMap.find(diff);
            if (iterator != numMap.end()){
                return {iterator->second, i};
            }
            numMap[nums[i]] = i;
        }

        return {};
    }
};
