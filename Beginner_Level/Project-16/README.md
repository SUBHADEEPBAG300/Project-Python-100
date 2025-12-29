# Factorial Calculator ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow) [![License](https://img.shields.io/github/license/Debanga-06/Code-Odessey)](https://github.com/Debanga-06/Code-Odessey/blob/main/LICENSE)

Professional factorial calculator with multiple calculation methods, step-by-step visualization, performance comparison, and mathematical analysis.

## Features

### Calculation Methods
- **Recursive**: Traditional recursive approach
- **Iterative**: Loop-based calculation (more efficient)
- **Built-in**: Python's optimized math.factorial()

### Advanced Features
- **Step-by-Step Display**: See calculation process
- **Performance Comparison**: Benchmark different methods
- **Factorial Properties**: Mathematical analysis
- **Factorial Tables**: Generate ranges
- **Trailing Zeros Counter**: Count zeros at end
- **Applications Guide**: Real-world uses

## What is a Factorial?

The factorial of a non-negative integer n, denoted n!, is the product of all positive integers less than or equal to n.

### Formula
```
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

### Special Cases
- **0! = 1** (by definition)
- **1! = 1**
- **Negative numbers**: Undefined

### Examples
```
3! = 3 × 2 × 1 = 6
5! = 5 × 4 × 3 × 2 × 1 = 120
10! = 10 × 9 × 8 × ... × 2 × 1 = 3,628,800
```

## Requirements

- Python 3.x
- Built-in modules: `math`, `time`

## Installation

```bash
python factorial_calculator.py
```

## Usage Examples

### Basic Calculation
```
Your choice: 1

Enter a non-negative integer: 5

==================================================
RESULT: 5! = 120
==================================================
Number of digits: 3
Full value: 120
```

### Step-by-Step Calculation
```
Your choice: 2

Enter a non-negative integer (0-20): 5

==================================================
STEP-BY-STEP CALCULATION: 5!
==================================================

5! = 5 × 4 × 3 × 2 × 1

Calculation steps:
  Step 1: 1 = 1
  Step 2: 1 × 2 = 2
  Step 3: 1 × 2 × 3 = 6
  Step 4: 1 × 2 × 3 × 4 = 24
  Step 5: 1 × 2 × 3 × 4 × 5 = 120

✓ Final Result: 5! = 120
==================================================
```

### Factorial Properties
```
Your choice: 3

Enter a non-negative integer: 10

==================================================
FACTORIAL PROPERTIES: 10!
==================================================

📊 Basic Information:
   Value:           3,628,800
   Number of digits: 7
   Scientific:      3.63e+06

🔢 Number Analysis:
   Trailing zeros:  2
   Even/Odd:        Even

🔗 Related Factorials:
   9! = 362,880
   10! = 3,628,800
   11! = 39,916,800

📐 Mathematical Facts:
   10! / 10 = 9! = 362,880
   10! / 10! = 1
   10! × 1 = 3,628,800
==================================================
```

### Performance Comparison
```
Your choice: 4

Enter a non-negative integer: 100

==================================================
PERFORMANCE COMPARISON: 100!
==================================================

⏱️  Execution Times:
   Recursive                 0.0234 ms
   Iterative                 0.0156 ms
   Built-in (math.factorial) 0.0089 ms

🏆 Fastest: Built-in (math.factorial)

✓ All methods produce identical results
==================================================
```

### Factorial Table
```
Your choice: 5

Start value (default 0): 0
End value (default 10): 10

==================================================
FACTORIAL TABLE: 0! to 10!
==================================================

n     n!                       Digits     Trailing 0s
----------------------------------------------------------------------
0     1                        1          0
1     1                        1          0
2     2                        1          0
3     6                        1          0
4     24                       2          0
5     120                      3          1
6     720                      3          1
7     5,040                    4          1
8     40,320                   5          1
9     362,880                  6          1
10    3,628,800                7          2
==================================================
```

## Calculation Methods Explained

### 1. Recursive Method
```python
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
```

**Pros:**
- Clear and elegant
- Matches mathematical definition
- Easy to understand

**Cons:**
- Stack overflow for large n (n > 1000)
- Slower than iterative
- More memory usage

**Best for:** Small numbers, teaching recursion

### 2. Iterative Method
```python
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

**Pros:**
- No stack overflow
- More efficient
- Less memory usage

**Cons:**
- Slightly less intuitive
- More code lines

**Best for:** Large numbers, production use

### 3. Built-in Method
```python
import math
result = math.factorial(n)
```

**Pros:**
- Fastest (C implementation)
- Most optimized
- Well-tested

**Cons:**
- Black box (can't see implementation)
- Less educational

**Best for:** Production code, performance-critical

## Common Factorials Reference

| n | n! | Digits |
|---|---|--------|
| 0 | 1 | 1 |
| 1 | 1 | 1 |
| 2 | 2 | 1 |
| 3 | 6 | 1 |
| 4 | 24 | 2 |
| 5 | 120 | 3 |
| 6 | 720 | 3 |
| 7 | 5,040 | 4 |
| 8 | 40,320 | 5 |
| 9 | 362,880 | 6 |
| 10 | 3,628,800 | 7 |
| 15 | 1,307,674,368,000 | 13 |
| 20 | 2,432,902,008,176,640,000 | 19 |
| 50 | 3.04 × 10^64 | 65 |
| 100 | 9.33 × 10^157 | 158 |

## Trailing Zeros Formula

The number of trailing zeros in n! is determined by how many times 10 divides n!.

Since 10 = 2 × 5, and there are always more 2s than 5s, we count factors of 5:

```
Trailing zeros = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ...
```

### Examples
- **10!** = 3,628,800 → 2 trailing zeros
  - ⌊10/5⌋ + ⌊10/25⌋ = 2 + 0 = 2
  
- **25!** → 6 trailing zeros
  - ⌊25/5⌋ + ⌊25/25⌋ + ⌊25/125⌋ = 5 + 1 + 0 = 6

- **100!** → 24 trailing zeros
  - ⌊100/5⌋ + ⌊100/25⌋ + ⌊100/125⌋ = 20 + 4 + 0 = 24

## Real-World Applications

### 1. Permutations
Number of ways to arrange n items:
```
P(n) = n!

Example: 5 books can be arranged in 5! = 120 ways
```

### 2. Combinations
Selecting r items from n items:
```
C(n,r) = n! / (r! × (n-r)!)

Example: Choose 3 from 5: C(5,3) = 5!/(3!×2!) = 10 ways
```

### 3. Probability
Calculating event probabilities:
```
P(specific order) = 1/n!

Example: Probability of specific card order: 1/52!
```

### 4. Password Strength
Number of possible passwords:
```
With 26 letters: 26! ≈ 4.03 × 10^26 possible orders
```

### 5. Tournament Brackets
Ways to arrange tournament:
```
8 teams: Ways to seed = 8! = 40,320
```

## Mathematical Properties

### Growth Rate
Factorials grow extremely fast:
```
1! = 1
5! = 120
10! = 3,628,800
20! = 2.43 × 10^18
100! = 9.33 × 10^157
```

### Stirling's Approximation
For large n:
```
n! ≈ √(2πn) × (n/e)^n

Example: 10! ≈ 3,598,695 (actual: 3,628,800)
Error: ~0.83%
```

### Factorial Relationships
```
n! = n × (n-1)!
(n+1)! = (n+1) × n!
n! × m! ≠ (n×m)!
(n!)! is much larger than n!
```

### Divisibility
- For n ≥ 2: n! is always even
- n! is divisible by all integers from 1 to n
- n! mod k = 0 for all k ≤ n

## Performance Benchmarks

### Execution Time (approximate)

| n | Recursive | Iterative | Built-in |
|---|-----------|-----------|----------|
| 10 | 0.002 ms | 0.001 ms | 0.001 ms |
| 100 | 0.023 ms | 0.016 ms | 0.009 ms |
| 1000 | Stack overflow | 0.150 ms | 0.089 ms |
| 10000 | Stack overflow | 15.2 ms | 8.9 ms |

### Memory Usage
- **Recursive**: O(n) stack space
- **Iterative**: O(1) extra space
- **Built-in**: Optimized C implementation

### Limits
- **Recursive**: ~1000 (Python stack limit)
- **Iterative**: Limited by integer size
- **Built-in**: Same as iterative

## Code Structure

### Functions

```python
factorial_recursive(n)          # Recursive calculation
factorial_iterative(n)          # Iterative calculation
factorial_builtin(n)            # Built-in math.factorial
display_factorial_steps(n)     # Show step-by-step
factorial_properties(n)         # Display properties
count_trailing_zeros(n)         # Count trailing zeros
compare_methods(n)              # Performance test
factorial_table(start, end)     # Generate table
factorial_applications()        # Show applications
```

## Use Cases

### Education
- Teaching recursion concepts
- Understanding factorial growth
- Learning algorithm complexity
- Mathematical proofs

### Mathematics
- Combinatorics problems
- Probability calculations
- Series expansions
- Number theory

### Computer Science
- Algorithm analysis
- Data structure problems
- Complexity calculations
- Interview questions

### Statistics
- Binomial distributions
- Permutation tests
- Sampling calculations
- Confidence intervals

## Tips & Tricks

### For Large Numbers
- Use iterative method (avoid recursion)
- Consider using logarithms: log(n!) = Σlog(k)
- Use Stirling's approximation for estimates
- Work in scientific notation

### For Programming
- Cache results for repeated calculations
- Use built-in when possible
- Handle overflow gracefully
- Validate input (non-negative)

### For Problem Solving
- Break into smaller factorials
- Use factorial properties
- Consider combinations formula
- Check for simplifications

## Common Mistakes

### 1. Negative Input
```python
❌ factorial(-5)  # Undefined
✓  Check: if n < 0: raise ValueError
```

### 2. Stack Overflow
```python
❌ factorial_recursive(5000)  # Crashes
✓  Use iterative for large n
```

### 3. Integer Overflow
```python
# Python handles automatically
# Other languages may need BigInteger
```

### 4. Off-by-One Errors
```python
❌ range(1, n)     # Misses n
✓  range(1, n+1)   # Includes n
```

## Future Enhancements

- [ ] Factorial visualization graphs
- [ ] Double factorial (n!!)
- [ ] Subfactorial (!n)
- [ ] Factorial prime detection
- [ ] Gamma function (generalized factorial)
- [ ] Factorial modulo calculator
- [ ] Prime factorization of n!
- [ ] Export results to file

## License

Free to use and modify for educational purposes.

## References

- Donald Knuth: "The Art of Computer Programming"
- OEIS: A000142 (Factorial Numbers)
- Wikipedia: Factorial
- Wolfram MathWorld: Factorial