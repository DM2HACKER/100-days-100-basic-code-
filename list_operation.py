# 12. Move Zeros to End
# Changing it so that user can dynamically enter their own values for the following demonstration 
z = [0, 1, 0, 3, 12]
print([x for x in z if x != 0] + [0] * z.count(0))

# 13. Second Largest Element
print(sorted(set([10, 20, 4, 45, 99]))[-2])

# 14. Find Missing Number (1 to 5)
missing_arr, n = [1, 2, 4, 5], 5
print(list(set(range(1, n+1)) - set(missing_arr))[0])

# 15. List Intersection
print(list(set([1, 2, 3]) & set([2, 3, 4])))

# 16. List Union
print(list(set([1, 2]) | set([2, 3])))
print("nizamuddin Tandel ")
    
