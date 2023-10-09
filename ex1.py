def find_max(input):
    max = 0
    for num in input:
        if num > max :
            max = num
              
    print(max)

input = [1,2,5,4,9,10,6]
find_max(input)