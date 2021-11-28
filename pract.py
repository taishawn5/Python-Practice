def largestRange(array):
    list = {x:0 for x in array}
    left = right = 0
    for n in array:
        if list[n] == 0:
            leftCount = n - 1
            rightCount = n + 1

            while leftCount in list:
                list[leftCount] = 1
                leftCount -= 1
            leftCount += 1
            while rightCount in list:
                list[rightCount] = 1
                rightCount += 1
            rightCount -= 1
            if (right - left) <= (rightCount - leftCount):
                right = rightCount
                left = leftCount
    return [left,right]
print(largestRange([3,4,9,1,2,0,10,11,18]))