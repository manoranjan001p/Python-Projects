lst = [10, 11, 12, 13, 14, 15]
# the above input can also be given as
# lst=list(map(int,input().split()))
l = []  # empty list
lst.sort(reverse=True)  #lst=lst[::-1] for reversing the letter
print(lst)
# checking if elements present in the list or not
for i in lst:
    print(i)
    # reversing the list
    l.insert(0, i)
    print(l)
# printing result
print(l)
