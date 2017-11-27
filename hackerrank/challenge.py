############################################

def oddNumbers(l, r):
    for item in range(l, r+1):
        if (item % 2) != 0:
            print(item)
oddNumbers(3,5)

############################################

def summation(numbers):
    total = 0
    if len(numbers) > 0:
        max = numbers[0]
        for i in range(1, max+1):
            total += numbers[i]
    return total
arr = [5, 1, 2, 3, 4, 5]
assert summation(arr) == 15

############################################

def lastLetters(word):
    return "{} {}".format(word[-1], word[-2])
assert lastLetters("HACK") == "K C"

############################################

def countPairs(numbers, k):
    n = numbers[0]
    count = 0
    for i in range(1, n):
        if (numbers[i] + k) == numbers[i+k]:
            count += 1
    return count

arr = [4,1,1,1,2,1]
assert countPairs(arr, 1) == 1

arr = [6, 1, 1, 2, 2, 3, 3, 1]
assert countPairs(arr, 1) == 2

arr = [6, 1, 2, 3, 4, 5, 6, 2]
assert countPairs(arr, 2) == 4

arr = [6, 1, 2, 5, 6, 9, 10, 2]
assert countPairs(arr, 2) == 0

############################################

totalProfit = totalUniform X saleLength X salePrice - totalCuts x costPerCut