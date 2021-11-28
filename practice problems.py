def squaredNumbers(numbers):
    squarednums = []
    for n in numbers:
        squarednums.append(n * n)
    return squarednums

# numbers = [2,4,7,9,10]
# print(squaredNumbers(numbers))
def findMinElement(arr):
    min = 1000000
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    print(min) 
        
def selectionSort(arr):
    size = len(arr)
    for i in range(size-1):
        minIndex = i
        for j in range(minIndex+1, size):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
# elements = [78,12,15,8,61,53,23,27]
# print(selectionSort(elements))

def sleepIn(weekday, vacation):
    if(not weekday or vacation):
        return True
    return False
# print(sleepIn(False,False))

def stringTimes(word, num):
    #return word * num //works also
    if(num == 0 or num == 1):
        return word
    value = ""
    for i in range(num):
        value += word
    return value
# print(stringTimes("hi",8))
#Difficulty Hard
def largestRange(array):  
    numbers = {x:0 for x in array}
    left = right = 0
    print(numbers)
    for number in array: #O(n) time
        if numbers[number] == 0:
            left_count = number - 1
            right_count = number + 1

            while left_count in numbers: #O(1)
                numbers[left_count] = 1
                left_count -= 1
            left_count += 1 #goes back to last value in sequence

            while right_count in numbers:
                numbers[right_count] = 1
                right_count += 1
            right_count -= 1
            if (right - left ) <= (right_count - left_count):
                right = right_count
                left = left_count
    return [left, right]
#print(largestRange([6,3,9,0,10,11,4,2,1,12,13,14,18,20]))

# medium difficulty Rivers problem
def riverSizes(matrix):
    marked = set()
    rivers = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1 and (row,col) not in marked:
                cur_river_len = 1
                marked.add((row,col))
                stack = [(row,col)]

                while stack:
                    current = stack.pop()
                    neighbors = get_neigbors(current, matrix)
                    for n in neighbors:
                        y,x = n
                        if matrix[y][x] == 1 and (y,x) not in marked:
                            marked.add((y,x))
                            cur_river_len += 1
                            stack.append((y,x))
                rivers.append(cur_river_len)
    return rivers
def get_neigbors(pos,matrix):
    y, x = pos
    ns = []
    if x >= 1:  #left
        ns.append((y,x-1))
    if x < len(matrix[0]) -1:
        ns.append((y,x+1))
    if y >= 1:
        ns.append((y-1,x))
    if y < len(matrix) -1:
        ns.append((y+1,x))
    return ns
#end of rivers problem