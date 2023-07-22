
# used sliding window approach to find max in each array window size
def rumbling(nums, X):
    maximum = []
    first, second = 0, X
    maximum.append(max(nums[first:second]))

    while second < len(nums):
        maximum.append(max(nums[first: second+1]))
        first += 1
        second += 1

    return maximum


# test case 1
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
X = 3
print("out1: ", rumbling(nums1, X))

# test case 2
nums2 = [1, 2, -1, 2, 4, 5]
Y = 2
print("out2: ", rumbling(nums2, Y))
