nums = [100, -80, 3, 8, 0]
print("Lista sulla quale effettueremo le operazioni:", nums)


print("\nOriginal order:")
for num in nums:
    print(num)

print("\nIncreasing order::")
for num in sorted(nums):
    print(num)

print("\nOriginal order:")
for num in nums:
    print(num)

print("\nDecreasing order:")
for num in sorted(nums,reverse=True):
    print(num)

print("\nOriginal order:")
for num in nums:
    print(num)

print("\nReverse-positional order:")
nums.reverse()
for num in nums:
    print(num)
nums.reverse()

print("\nOriginal order:")
for num in nums:
    print(num)

print("\nPermanent increasing order:")
nums.sort()
for num in nums:
    print(num)

print("\nPermanent decreasing order:")
nums.sort(reverse=True)
for num in nums:
    print(num)

