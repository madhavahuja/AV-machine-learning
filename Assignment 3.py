# question 1

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(l[7:12])
print(l[-9:-4])

# question 2
even = []
for x in l:
    if x%2==0:
        even.append(x)
print("Even list",even)

# question 3
print(l[0:17:4])
