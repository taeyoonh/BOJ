import sys
N = sys.stdin.readline().rstrip()
p =sys.stdin.readline().rstrip()
si=sys.stdin.readline().rstrip().split()
bre=list(map(int, si))

min1 = abs(100 - int(N))

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in bre:
            break

        elif j == len(nums) - 1:
            min1 = min(min1, abs(int(nums) - int(N)) + len(nums))

print(min1)