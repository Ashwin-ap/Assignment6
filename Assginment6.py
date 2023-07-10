""" Question 1. A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1]. """
def reconstructPermutation(s):
    perm = []
    start = 0
    end = len(s)

    for char in s:
        if char == 'I':
            perm.append(start)
            start += 1
        elif char == 'D':
            perm.append(end)
            end -= 1

    perm.append(start)  # or perm.append(end), as start == end
    return perm

"""
Question 2

You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true *if* target *is in* matrix *or* false *otherwise*.
"""
def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    
    left = 0
    right = m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

""" <aside>
💡 **Question 3**

Given an array of integers arr, return *true if and only if it is a valid mountain array*.
Recall that arr is a mountain array if and only if:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False
    
    i = 1
    while i < n and arr[i] > arr[i-1]:
        i += 1
    
    if i == 1 or i == n or arr[i] == arr[i-1]:
        return False
    
    while i < n and arr[i] < arr[i-1]:
        i += 1
    
    return i == n

"""
💡 **Question 4**

Given a binary array nums, return *the maximum length of a contiguous subarray with an equal number of* 0 *and* 1.
**Example 1:**
**Input:** nums = [0,1]
**Output:** 2
**Explanation:**
[0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
"""

def findMaxLength(nums):
    max_length = 0
    count = 0
    count_map = {0: -1}

    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            count -= 1

        if count in count_map:
            max_length = max(max_length, i - count_map[count])
        else:
            count_map[count] = i

    return max_length

"""
💡 **Question 5**
The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).
"""

def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort(reverse=True)
    
    min_product_sum = 0
    
    for i in range(len(nums1)):
        min_product_sum += nums1[i] * nums2[i]
    
    return min_product_sum

"""
💡 **Question 6**
An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.
"""
def findOriginalArray(changed):
    changed.sort()
    original = []
    
    for num in changed:
        original_value = num // 2
        if original_value not in original:
            original.append(original_value)
        else:
            return []
    
    return original


"""
💡 **Question 7**
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""
def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n-1, 0, n-1
    num = 1
    
    while num <= n**2:
        for c in range(left, right+1):
            matrix[top][c] = num
            num += 1
        top += 1
        
        for r in range(top, bottom+1):
            matrix[r][right] = num
            num += 1
        right -= 1
        
        for c in range(right, left-1, -1):
            matrix[bottom][c] = num
            num += 1
        bottom -= 1
        
        for r in range(bottom, top-1, -1):
            matrix[r][left] = num
            num += 1
        left += 1
    
    return matrix


"""
💡 **Question 8**
Given two [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.
"""

def multiply(mat1, mat2):
    m = len(mat1)
    k = len(mat1[0])
    n = len(mat2[0])
    
    result = [[0] * n for _ in range(m)]
    
    mat1_dict = {}
    for i in range(m):
        for j in range(k):
            if mat1[i][j] != 0:
                mat1_dict[(i, j)] = mat1[i][j]
    
    for i in range(k):
        for j in range(n):
            if mat2[i][j] != 0:
                for (row, col), value in mat1_dict.items():
                    if col == i:
                        result[row][j] += value * mat2[i][j]
    
    return result
