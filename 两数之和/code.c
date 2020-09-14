/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) 
{   
    static int temp[2] = {0};   //不加static，此函数运行结束后，内存释放，数组消失
    int i = 0;
    int j = 0;
    for(i=0; i<numsSize-1; i++)
    {
        for ( j = i+1; j < numsSize; j++)
        {
            /* code */
            if (nums[i]+nums[j] == target)
            {
                /* code */
                temp[0] = i;
                temp[1] = j;
                return temp;
            }
            
        }
        
    }
    return 0;
}