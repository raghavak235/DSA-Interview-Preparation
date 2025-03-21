**Understanding the Recursive Function: `sum_of_digits(n)`**

### **Function Definition:**
The function `sum_of_digits(n)` calculates the sum of the digits of a given number using recursion.

### **Step-by-Step Explanation:**

#### **1. Function Definition:**
```python
def sum_of_digits(n):
```
- The function takes an integer `n` as input and returns the sum of its digits.

---

#### **2. Base Case:**
```python
if n < 9:
    return n
```
- If `n` is a single-digit number (i.e., `n < 9`), return `n` itself.
- This acts as the stopping condition for recursion.

---

#### **3. Recursive Case:**
```python
return sum_of_digits(n // 10) + n % 10
```
- `n // 10`: Removes the last digit of `n` (integer division by 10).
- `n % 10`: Extracts the last digit of `n` (modulus operation).
- Calls `sum_of_digits(n // 10)` recursively to sum up the remaining digits.
- Adds the last digit (`n % 10`) to the result of the recursive call.

---

### **Execution Example:**
#### **Function Call: `sum_of_digits(253)`**

1. `sum_of_digits(253)`
   - `253 // 10 = 25`
   - `253 % 10 = 3`
   - Calls `sum_of_digits(25)`, then adds `3`.

2. `sum_of_digits(25)`
   - `25 // 10 = 2`
   - `25 % 10 = 5`
   - Calls `sum_of_digits(2)`, then adds `5`.

3. `sum_of_digits(2)`
   - Since `2 < 9`, return `2` (base case).

---

### **Backtracking (Summing Up the Values):**
- `sum_of_digits(2) = 2`
- `sum_of_digits(25) = 2 + 5 = 7`
- `sum_of_digits(253) = 7 + 3 = 10`

---

### **Final Output:**
```python
print(sum_of_digits(253))  # Output: 10
```

---

### **Summary of the Process:**
1. The function removes the last digit in each recursive call.
2. The recursion stops when `n` is a single-digit number.
3. The last digits are summed up during the backtracking phase.
4. The final sum of digits of `253` is `10`.


def is_palindrome(num):
    # Convert the number to a string for easy comparison.
    s = str(num)
    
    def check_palindrome(start, end):
        # Base case: If we've reached the middle, it's a palindrome.
        if start >= end:
            return True
        # If the digits at the start and end don't match, it's not a palindrome.
        if s[start] != s[end]:
            return False
        # Recursive call: move one step inward.
        return check_palindrome(start + 1, end - 1)
    
    return check_palindrome(0, len(s) - 1)

# Example usage:
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")


This is how the recursive function works to compute the sum of the digits of a number!


n=5
arr=[5, 10, 10, 15, 15]
x=10

def firstOccurancebinaryserach_recursive(arr, low,high, x):
    if low > high:
        return -1
    
    mid = (low + high)//2
    
    if arr[mid] > x:
        return firstOccurancebinaryserach_recursive(arr, low ,mid-1, x)
        
    elif  arr[mid] < x:
        return firstOccurancebinaryserach_recursive(arr, mid+1, high, x)
    
    else: 
        # The reason for the below condition is we try to see if mid =0  might have our value [10,10,10]
        # And also we're trying to see if the before value is also same [2,10,10,20,20]
        # if yes we iterate again with low and mid -1 to cover the before values
        if mid == 0 or arr[mid-1] != arr[mid]:
            return mid
        else:            
            return firstOccurancebinaryserach_recursive(arr, low, mid-1, x)
            
print(firstOccurancebinaryserach_recursive(arr, 0, len(arr)-1, x))            

Detailed Steps for First Occurrence Binary Search (Recursive)
Given code:
n = 5
arr = [5, 10, 10, 15, 15]
x = 10

Function: firstOccurancebinaryserach_recursive(arr, low, high, x)

Step-by-Step Execution:
Initial Call: firstOccurancebinaryserach_recursive([5, 10, 10, 15, 15], 0, 4, 10)

1. First Call:
   - Input: arr = [5, 10, 10, 15, 15], low = 0, high = 4, x = 10
   - Check: low(0) <= high(4), condition true
   - Calculate mid: (0 + 4) // 2 = 2
   - arr[2] = 10, compare with x = 10
   - arr[mid] == x is true, so enter else block
   - Check if mid is first occurrence:
     - mid = 2 (not 0)
     - arr[mid-1] = arr[1] = 10, which equals arr[2]
     - Not first occurrence, recurse on left half
   - Recursive Call: firstOccurancebinaryserach_recursive(arr, 0, 1, 10)

2. Second Call:
   - Input: arr = [5, 10, 10, 15, 15], low = 0, high = 1, x = 10
   - Check: low(0) <= high(1), condition true
   - Calculate mid: (0 + 1) // 2 = 0
   - arr[0] = 5, compare with x = 10
   - arr[mid] < x is true
   - Recursive Call: firstOccurancebinaryserach_recursive(arr, 1, 1, 10)

3. Third Call:
   - Input: arr = [5, 10, 10, 15, 15], low = 1, high = 1, x = 10
   - Check: low(1) <= high(1), condition true
   - Calculate mid: (1 + 1) // 2 = 1
   - arr[1] = 10, compare with x = 10
   - arr[mid] == x is true, so enter else block
   - Check if mid is first occurrence:
     - mid = 1 (not 0)
     - arr[mid-1] = arr[0] = 5, which does not equal arr[1]
     - This is the first occurrence!
   - Return: mid = 1

4. Result Propagation:
   - Third call returns 1
   - Second call returns 1
   - First call returns 1
   - Final output: print(1)

Algorithm Logic:
1. Base Case:
   - If low > high, search space exhausted, return -1

2. Calculate Middle:
   - mid = (low + high) // 2

3. Three Possibilities:
   a. If arr[mid] > x:
      - Search left half: recurse with (low, mid-1)
   b. If arr[mid] < x:
      - Search right half: recurse with (mid+1, high)
   c. If arr[mid] == x:
      - Check if it's first occurrence:
        - If mid is 0 OR previous element is different: return mid
        - Otherwise, search left half: recurse with (low, mid-1)

Time Complexity: O(log n)
Space Complexity: O(log n) due to recursive call stack

Final Output: 1
- Meaning: The first occurrence of 10 is at index 1 in the array [5, 10, 10, 15, 15]
Understanding the First Occurrence Binary Search Conditions
========================================================

Key Points
----------
- The conditions `if mid == 0 or arr[mid-1] != arr[mid]` are crucial for identifying
  the first occurrence of a target value in a sorted array
- They handle duplicate values effectively
- They ensure we return the leftmost position of the target

Purpose of These Conditions
---------------------------
- Used in recursive binary search to find the first occurrence
- Designed to work with sorted arrays that may contain duplicates
- Prevents returning later occurrences when multiple matches exist

Detailed Explanation of Conditions
----------------------------------
1. First Condition: `mid == 0`
   - Checks if we're at the array's first element (index 0)
   - If this element equals the target, it's automatically the first occurrence
   - No previous elements to compare with

2. Second Condition: `arr[mid-1] != arr[mid]`
   - Checks if the element before current middle differs from current element
   - If true (and arr[mid] equals target), current position is first occurrence
   - Ensures no earlier duplicates exist

Execution Flow
--------------
For each recursive call:
1. If either condition is true:
   - Current mid is the first occurrence
   - Return mid as the result
2. If both conditions are false:
   - mid > 0 AND arr[mid-1] == arr[mid]
   - Indicates earlier occurrences exist
   - Recursively search left half (low to mid-1)

Example Walkthrough
-------------------
Array: [5, 10, 10, 15, 15]
Target: 10

Case 1:
- mid = 2, arr[2] = 10
- Check conditions:
  - mid == 0? False (2 != 0)
  - arr[1] != arr[2]? False (10 == 10)
- Result: Not first occurrence, search left

Case 2:
- mid = 1, arr[1] = 10
- Check conditions:
  - mid == 0? False (1 != 0)
  - arr[0] != arr[1]? True (5 != 10)
- Result: First occurrence found, return 1

Why It's Effective
------------------
- Handles duplicates without linear search
- Maintains O(log n) time complexity
- Always finds leftmost occurrence
- Surprisingly efficient despite multiple matches

Conclusion
----------
These conditions transform standard binary search into a specialized
version that pinpoints the first occurrence, making it invaluable for
sorted arrays with duplicate values.


                                                      def firstOccurence(arr, n, x):
    low=0 
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(x>arr[mid]):
            low=mid+1 
        elif(x<arr[mid]):
            high=mid-1 
        else:
# mid == 0: Catches cases where the first occurrence is at the start of the array.
# arr[mid-1] != arr[mid]: Ensures that if we’ve found x, there’s no earlier duplicate by checking the previous element.
# Else clause (high = mid - 1): If the condition fails, it means arr[mid-1] == arr[mid], so there’s a duplicate x earlier in the sorted array, and we need to search left.
            if mid ==0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                high = mid -1
                
    
    return -1
        
        
        
        
    
n=5
arr=[5, 10, 10, 15, 15]
x=10
# print(firstOccurenceRecursive(arr, 0, n-1, x))
print(firstOccurence(arr, n, x))
