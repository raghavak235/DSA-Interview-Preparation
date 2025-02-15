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

This is how the recursive function works to compute the sum of the digits of a number!

