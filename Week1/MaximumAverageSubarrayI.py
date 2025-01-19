class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
  
        # Space Complexity: O(1)
        # Time Complexity: O(n)
        avg=0
        n = len(nums)
        curr_sum = 0 

        if (n)==1:
            return sum(nums)/k
    
        for i in range(k):
            curr_sum += nums[i]
        
        avg = curr_sum/k
        for i in range(k,n):
            curr_sum +=  nums[i]
            curr_sum -= nums[i-k]
            avg = max(avg, curr_sum/k)
        
      
      # Brute Force Approach
        # Space Complexity: O(1)
        # Time Complexity: O(n2)
  
      Example
Suppose we have:

makefile
Copy
nums = [1, 12, -5, -6, 50, 3]
k = 4
Here:

𝑛
=
6
n=6 (the length of nums)
𝑘
=
4
k=4
1. Outer Loop Range: range(0, n - k + 1)
We write range(0, 6 - 4 + 1) = range(0, 3).
That means 
𝑖
∈
{
0
,
1
,
2
}
i∈{0,1,2}.
Why up to 2? Because the last valid starting index for a subarray of length 4 is index 2:
If you start at index 2, the subarray covers indices [2, 3, 4, 5].
If you tried to start at index 3, you’d need [3, 4, 5, 6], but 6 is out of bounds in a 6-element list (valid indices are 0 to 5).
So, the outer loop iterates over three possible starting points:

i = 0
i = 1
i = 2
Each value of i corresponds to a subarray of length k=4:

For i = 0: subarray is nums[0..3] = [1, 12, -5, -6]
For i = 1: subarray is nums[1..4] = [12, -5, -6, 50]
For i = 2: subarray is nums[2..5] = [-5, -6, 50, 3]
2. Inner Loop Range: range(i, i + k)
Let’s see what happens inside the outer loop for each i. We do:

python
Copy
current_sum = 0
for j in range(i, i + k):
    current_sum += nums[j]
This loop accumulates exactly the k (=4) elements starting at index i.

a. When i = 0
range(0, 0 + 4) → range(0, 4) → j takes values [0, 1, 2, 3]
nums[0] = 1
nums[1] = 12
nums[2] = -5
nums[3] = -6
current_sum = 1 + 12 + (-5) + (-6) = 2
b. When i = 1
range(1, 1 + 4) → range(1, 5) → j takes values [1, 2, 3, 4]
nums[1] = 12
nums[2] = -5
nums[3] = -6
nums[4] = 50
current_sum = 12 + (-5) + (-6) + 50 = 51
c. When i = 2
range(2, 2 + 4) → range(2, 6) → j takes values [2, 3, 4, 5]
nums[2] = -5
nums[3] = -6
nums[4] = 50
nums[5] = 3
current_sum = -5 + (-6) + 50 + 3 = 42
3. Compare current_sum with max_sum After the Inner Loop
Once the inner loop finishes (for a given i), we have the sum of that subarray of length k. We then compare it with our running max_sum:

python
Copy
if current_sum > max_sum:
    max_sum = current_sum
After i=0: current_sum = 2
After i=1: current_sum = 51 (bigger than 2, so max_sum = 51)
After i=2: current_sum = 42 (not bigger than 51, so max_sum stays 51)
Why These Ranges?
range(0, n - k + 1) for the outer loop

Ensures you only pick valid starting indices for subarrays of length k.
The largest starting index is n-k, because if you start at n-k, the subarray ends at (n-k) + k - 1 = n-1 (the last valid element in the array).
range(i, i + k) for the inner loop

Ensures you capture exactly k elements beginning at index i.
You accumulate those k items into current_sum.


        # for i in range(0,n-k+1):
        #     for j in range(i,i+k):
        #         sublist = sum(nums[i:i+k])/k
        #         print(nums[i:i+k])
        #         if sublist > avg:
        #             avg=max(avg,sublist)
        # print(avg)
        return avg
