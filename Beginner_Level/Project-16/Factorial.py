"""
Factorial Calculator - Program 25
Calculate factorials with multiple methods, visualization, and analysis.
"""

import math
import time


def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    
    Formula: n! = n × (n-1)!
    Base case: 0! = 1, 1! = 1
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """
    Calculate factorial using iteration (loop).
    More efficient than recursion for large numbers.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def factorial_builtin(n):
    """
    Calculate factorial using Python's built-in math.factorial().
    Optimized C implementation.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    return math.factorial(n)


def display_factorial_steps(n):
    """Display step-by-step calculation of factorial."""
    if n < 0:
        print("❌ Factorial is not defined for negative numbers.")
        return
    
    print("\n" + "=" * 70)
    print(f"STEP-BY-STEP CALCULATION: {n}!")
    print("=" * 70)
    
    if n == 0 or n == 1:
        print(f"\n{n}! = 1 (by definition)")
    else:
        # Show multiplication sequence
        sequence = " × ".join(str(i) for i in range(n, 0, -1))
        print(f"\n{n}! = {sequence}")
        
        # Show step-by-step multiplication
        print("\nCalculation steps:")
        result = 1
        for i in range(1, n + 1):
            result *= i
            print(f"  Step {i}: {' × '.join(str(j) for j in range(1, i + 1))} = {result:,}")
    
    final_result = factorial_iterative(n)
    print(f"\n✓ Final Result: {n}! = {final_result:,}")
    print("=" * 70)


def factorial_properties(n):
    """Display mathematical properties of factorial."""
    if n < 0:
        print("❌ Factorial is not defined for negative numbers.")
        return
    
    result = factorial_iterative(n)
    
    print("\n" + "=" * 70)
    print(f"FACTORIAL PROPERTIES: {n}!")
    print("=" * 70)
    
    print(f"\n📊 Basic Information:")
    print(f"   Value:           {result:,}")
    print(f"   Number of digits: {len(str(result))}")
    print(f"   Scientific:      {result:.2e}")
    
    # Trailing zeros
    trailing_zeros = count_trailing_zeros(n)
    print(f"\n🔢 Number Analysis:")
    print(f"   Trailing zeros:  {trailing_zeros}")
    print(f"   Even/Odd:        {'Even' if result % 2 == 0 else 'Odd'}")
    
    # Related factorials
    if n > 0:
        print(f"\n🔗 Related Factorials:")
        print(f"   {n-1}! = {factorial_iterative(n-1):,}")
        print(f"   {n}! = {result:,}")
        if n < 20:  # Avoid huge numbers
            print(f"   {n+1}! = {factorial_iterative(n+1):,}")
    
    # Factorial relationships
    print(f"\n📐 Mathematical Facts:")
    print(f"   {n}! / {n} = {n-1}! = {result // n if n > 0 else 1:,}")
    if n >= 2:
        print(f"   {n}! / {n}! = 1")
        print(f"   {n}! × 1 = {result:,}")
    
    print("=" * 70)


def count_trailing_zeros(n):
    """
    Count trailing zeros in n!
    Formula: Sum of floor(n/5^i) for i = 1, 2, 3, ...
    """
    count = 0
    i = 5
    while i <= n:
        count += n // i
        i *= 5
    return count


def compare_methods(n):
    """Compare performance of different factorial calculation methods."""
    if n < 0:
        print("❌ Factorial is not defined for negative numbers.")
        return
    
    if n > 1000:
        print("⚠️  Warning: Using smaller value (1000) for recursive method to avoid stack overflow.")
        test_n = 1000
    else:
        test_n = n
    
    print("\n" + "=" * 70)
    print(f"PERFORMANCE COMPARISON: {n}!")
    print("=" * 70)
    
    methods = []
    
    # Test recursive (if safe)
    if test_n <= 1000:
        start = time.time()
        result_rec = factorial_recursive(test_n)
        time_rec = time.time() - start
        methods.append(("Recursive", time_rec, result_rec))
    
    # Test iterative
    start = time.time()
    result_iter = factorial_iterative(n)
    time_iter = time.time() - start
    methods.append(("Iterative", time_iter, result_iter))
    
    # Test built-in
    start = time.time()
    result_builtin = factorial_builtin(n)
    time_builtin = time.time() - start
    methods.append(("Built-in (math.factorial)", time_builtin, result_builtin))
    
    # Display results
    print(f"\n⏱️  Execution Times:")
    for method, exec_time, _ in methods:
        print(f"   {method:<25} {exec_time*1000:.4f} ms")
    
    # Find fastest
    fastest = min(methods, key=lambda x: x[1])
    print(f"\n🏆 Fastest: {fastest[0]}")
    
    # Verify all methods produce same result
    results = [m[2] for m in methods]
    if len(set(results)) == 1:
        print(f"\n✓ All methods produce identical results")
    
    print("=" * 70)


def factorial_table(start, end):
    """Display a table of factorials."""
    if start < 0 or end < 0:
        print("❌ Factorial is not defined for negative numbers.")
        return
    
    if end > 20:
        print("⚠️  Limiting table to n=20 to avoid huge numbers.")
        end = 20
    
    print("\n" + "=" * 70)
    print(f"FACTORIAL TABLE: {start}! to {end}!")
    print("=" * 70)
    print(f"\n{'n':<5} {'n!':<25} {'Digits':<10} {'Trailing 0s'}")
    print("-" * 70)
    
    for n in range(start, end + 1):
        result = factorial_iterative(n)
        digits = len(str(result))
        trailing = count_trailing_zeros(n)
        
        # Format large numbers
        if result < 1000000:
            result_str = f"{result:,}"
        else:
            result_str = f"{result:.2e}"
        
        print(f"{n:<5} {result_str:<25} {digits:<10} {trailing}")
    
    print("=" * 70)


def factorial_applications():
    """Display real-world applications of factorials."""
    print("\n" + "=" * 70)
    print("FACTORIAL APPLICATIONS")
    print("=" * 70)
    
    print("\n📚 Mathematics:")
    print("  • Permutations: Number of ways to arrange n items = n!")
    print("  • Combinations: C(n,r) = n! / (r! × (n-r)!)")
    print("  • Taylor Series: Many series use factorials")
    print("  • Binomial Theorem: Expansion coefficients")
    
    print("\n🔬 Science:")
    print("  • Probability: Calculating event probabilities")
    print("  • Statistics: Distribution functions")
    print("  • Chemistry: Molecular arrangements")
    print("  • Physics: Quantum mechanics calculations")
    
    print("\n💻 Computer Science:")
    print("  • Algorithm Analysis: Time complexity")
    print("  • Recursion Examples: Teaching recursion")
    print("  • Combinatorial Problems: Solving arrangements")
    print("  • Data Structures: Tree calculations")
    
    print("\n🎲 Real-World Examples:")
    print("  • Lottery Odds: Calculating winning chances")
    print("  • Password Combinations: Security analysis")
    print("  • Seating Arrangements: Event planning")
    print("  • Tournament Brackets: Sports scheduling")
    
    print("=" * 70)


def main():
    """Main program execution."""
    print("=" * 70)
    print("                 FACTORIAL CALCULATOR")
    print("=" * 70)
    print("\nCalculate n! = n × (n-1) × (n-2) × ... × 2 × 1")
    print("Example: 5! = 5 × 4 × 3 × 2 × 1 = 120")
    
    while True:
        print("\n" + "-" * 70)
        print("Options:")
        print("  1. Calculate factorial")
        print("  2. Show step-by-step calculation")
        print("  3. View factorial properties")
        print("  4. Compare calculation methods")
        print("  5. Display factorial table")
        print("  6. View applications")
        print("  7. Quick reference")
        print("  q. Quit")
        print("-" * 70)
        
        choice = input("\nYour choice: ").strip().lower()
        
        if choice == 'q':
            print("\n✓ Thank you for using Factorial Calculator!")
            break
        
        try:
            if choice == '1':
                # Calculate factorial
                n = int(input("\nEnter a non-negative integer: "))
                
                if n < 0:
                    print("❌ Factorial is not defined for negative numbers.")
                    continue
                
                if n > 10000:
                    print("⚠️  Warning: Very large number. This may take time.")
                    confirm = input("Continue? (y/n): ")
                    if confirm.lower() != 'y':
                        continue
                
                result = factorial_iterative(n)
                
                print("\n" + "=" * 70)
                print(f"RESULT: {n}! = {result:,}")
                print("=" * 70)
                print(f"Number of digits: {len(str(result))}")
                
                if len(str(result)) <= 100:
                    print(f"Full value: {result}")
                else:
                    print(f"Scientific notation: {result:.6e}")
            
            elif choice == '2':
                # Step-by-step
                n = int(input("\nEnter a non-negative integer (0-20): "))
                
                if n < 0:
                    print("❌ Factorial is not defined for negative numbers.")
                    continue
                
                if n > 20:
                    print("⚠️  Using n=20 for readability.")
                    n = 20
                
                display_factorial_steps(n)
            
            elif choice == '3':
                # Properties
                n = int(input("\nEnter a non-negative integer: "))
                factorial_properties(n)
            
            elif choice == '4':
                # Compare methods
                n = int(input("\nEnter a non-negative integer: "))
                compare_methods(n)
            
            elif choice == '5':
                # Factorial table
                start = int(input("\nStart value (default 0): ") or "0")
                end = int(input("End value (default 10): ") or "10")
                
                factorial_table(start, end)
            
            elif choice == '6':
                # Applications
                factorial_applications()
            
            elif choice == '7':
                # Quick reference
                print("\n" + "=" * 70)
                print("QUICK REFERENCE")
                print("=" * 70)
                print("\n📖 Common Factorials:")
                print("   0! = 1")
                print("   1! = 1")
                print("   2! = 2")
                print("   3! = 6")
                print("   4! = 24")
                print("   5! = 120")
                print("   10! = 3,628,800")
                print("   20! = 2,432,902,008,176,640,000")
                
                print("\n📐 Formulas:")
                print("   n! = n × (n-1)!")
                print("   n! = n × (n-1) × (n-2) × ... × 2 × 1")
                print("   0! = 1 (by definition)")
                
                print("\n💡 Properties:")
                print("   • n! grows extremely fast")
                print("   • n! is always divisible by all numbers ≤ n")
                print("   • For n ≥ 2, n! is always even")
                print("   • Trailing zeros = floor(n/5) + floor(n/25) + ...")
                
                print("=" * 70)
            
            else:
                print("❌ Invalid choice. Please try again.")
        
        except ValueError as e:
            print(f"❌ Invalid input: {e}")
        except RecursionError:
            print("❌ Number too large for recursive calculation. Use iterative method.")
        except Exception as e:
            print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    main()