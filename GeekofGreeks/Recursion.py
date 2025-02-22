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

