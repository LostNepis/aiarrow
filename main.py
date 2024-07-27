mylist = eval(input())


def find_missing_questions(nums):
    n = len(nums)
    all_numbers = set(range(1, n + 1))
    present_numbers = set(nums)
    missing_numbers = sorted(all_numbers - present_numbers)
    return missing_numbers


result = find_missing_questions(mylist)
print(result)
