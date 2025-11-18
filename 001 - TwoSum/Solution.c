/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    for (int i = 0; i < numsSize-1; i++){
        for (int j = i+1; j < numsSize; j++){
            if (nums[i] + nums[j] == target){
                *returnSize = 2;
                int* output = malloc(2 * sizeof(int));
                output[0] = i;
                output[1] = j;
                return output;
            }

        }
    }
    return NULL;
}
