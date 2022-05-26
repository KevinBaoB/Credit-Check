import functools

def credit_check(nums):
    arr = []
    nums = list(str(nums)[::-1])
    for i in range(len(nums)):
        if (i % 2 != 0) :
            arr.append(int(nums[i]) * 2)
        else:
            arr.append(int(nums[i]))
    for j in range(len(arr)) :   
        if arr[j] > 9:
            bigger = list(str(arr[j]))
            arr[j] = int(bigger[0]) + int(bigger[1])
            
    res = functools.reduce(lambda a, b : a + b, arr)   
    if res % 10 == 0 :
        return "The number is valid!"
    else : return "The number is invalid!"

    
  

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"
print(credit_check(5541808923795240))
