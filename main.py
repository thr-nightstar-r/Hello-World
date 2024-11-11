def product_except_self(nums):
   
    n = len(nums)
   
    result = [1] * n

    
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result


test_cases = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [0, 0, 23, 0],
    [-1, -2, -3, -4],
    [10],
    [1, 2, 0, 4, 0],  
]

for i, case in enumerate(test_cases, 1):
    result = product_except_self(case)
    print(f"Test case {i}:")
    print(f"Input:  {case}")
    print(f"Output: {result}")
    
    for j in range(len(case)):
        expected = 1
        for k in range(len(case)):
            if k != j:
                expected *= case[k]
        assert result[j] == expected, f"Error in test case {i}, index {j}"
    
    print("Verified: Correct")
    print()

print("All test cases passed successfully!")