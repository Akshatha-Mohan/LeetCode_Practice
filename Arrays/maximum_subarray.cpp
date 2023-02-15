/*
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
*/

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSub = nums[0];
        int currSum = 0;
        for (int i=0; i<nums.size(); i++){
            if(currSum < 0){
                currSum = 0;
            }
            currSum = currSum + nums[i];
            maxSub = max(maxSub, currSum);
        }
       return maxSub; 
    }
};


