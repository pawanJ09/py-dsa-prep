
def reverse_list(nums):
    """
    O(N) Linear reversal where N is the length of the list
    :param nums:
    :return: nums list
    """
    start_index = 0
    end_index = len(nums)-1
    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1
    return nums


def palindrome_python(s: str) -> bool:
    """
    This function uses list slicing to check for palindrome and return a boolean
    :param s: str
    :return: boolean
    """
    if s == s[::-1]:
        return True
    return False


def palindrome_custom(s: str) -> bool:
    """
    This function reverses the given string and compares if the reverse and original string are
    equal to conclude if the string is palindrome. This has O(N) complexity Linear reversal where
    N is the length of the string
    :param s: str
    :return: boolean
    """
    s_list = list(s)
    start = 0
    end = len(s) - 1
    while end > start:
        s_list[start], s_list[end] = s_list[end], s_list[start]
        start = start + 1
        end = end - 1
    return s == ''.join(s_list)


def reverse_num(num: int) -> int:
    """
    This function reverses an integer number and returns the reversed number
    :param num: int
    :return: num_r int
    """
    num_r = 0
    remainder = 0
    while num > 0:
        remainder = num % 10
        num_r = num_r * 10 + remainder
        num = num//10
    return num_r


def is_anagram(str1: str, str2: str) -> bool:
    """
    This function checks if the 2 input strings are anagram and returns a boolean
    :param str1: str
    :param str2: str
    :return: boolean
    """
    s1 = list(str1)
    s2 = list(str2)
    if len(s1) != len(s2):
        return False
    s1.sort()
    s2.sort()
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def sort_dutch_national_flag(nums: list, pivot=1):
    i = 0
    j = 0
    k = len(nums)-1
    while j <= k:
        # If number is 0
        if nums[j] < pivot:
            swap(nums, i, j)
            i = i + 1
            j = j + 1
        # If number is 2
        elif nums[j] > pivot:
            swap(nums, j, k)
            k = k - 1
        # If number is 1
        else:
            j = j + 1
    return nums


def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]


def water_storage(height_list):
    if len(height_list) < 3:
        return 0
    left_max = [0 for _ in range(len(height_list))]
    right_max = [0 for _ in range(len(height_list))]
    for i in range(1, len(left_max)):
        left_max[i] = max(left_max[i-1], height_list[i-1])
    for i in range(len(right_max)-2, -1, -1):
        right_max[i] = max(right_max[i+1], height_list[i+1])
    trapped = 0
    for i in range(len(height_list)-1):
        if min(left_max[i], right_max[i]) > height_list[i]:
            trapped += min(left_max[i], right_max[i]) - height_list[i]
    return trapped


if __name__ == '__main__':
    array = [1, 4, 0, 10]
    # Printing array
    print(f'Array: {array}')
    # Unpacking and printing array
    print('Array using unpacking: {}'.format(*array))
    # Print an element of array
    print(f'Array element by index: {array[1]}')
    # Reverse a list using slicing
    print(f'Reversing list using slicing {array[::-1]}')
    # Reverse a list using reverse function to reverse in place
    array.reverse()
    print(f'Reversing list IN PLACE using reverse(): {array}')
    # Reverse using custom method
    print(f'Reverse using custom method: {reverse_list(array)}')
    # Palindrome using slicing
    s = 'car'
    print(f'Is {s} a palindrome using slicing? {palindrome_python(s)}')
    # Palindrome using custom reverse
    print(f'Is {s} a palindrome using custom? {palindrome_custom(s)}')
    # reverse a number
    num = 1234
    print(f'Reverse of {num} is {reverse_num(num)}')
    # Checking anagram
    string1 = "restful"
    string2 = "fluster"
    print(f'Are {string1} and {string2} anagrams? {is_anagram(string1, string2)}')
    # Dutch national flag problem
    nums = [1, 1, 2, 0, 0, 2, 2, 0, 1, 1]
    print(f'Sorted result of {nums} is {sort_dutch_national_flag(nums, 1)}')
    # Water storage problem
    heights = [2, 1, 3, 2, 4]
    print(f'Total units for water stored is: {water_storage(heights)}')