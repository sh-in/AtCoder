n = int(input())
nums = [i for i in range(1, 2*n+2)]
while True:
    print(nums[0])
    nums.remove(nums[0])
    a = int(input())
    if a == 0:
        exit()
    nums.remove(a)