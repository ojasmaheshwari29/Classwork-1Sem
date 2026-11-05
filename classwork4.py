#Sets { },
#unordered, unique elements, allow different datatype, no duplicate elements
# {20,30,40}
# {"a","b","c"}
#{(20,30),(50,60)}
# {[20,30],[40,50]} #gives error 

# s = {10,20,10,30,40}
# print(s)
# s1 = set()
# print(s1)
# s2=set([10,20,30,10])
# print(s2)
# s3={(1,2),(3,4)}
# print(s3)
# s3={[1,2],[3,4]}
# print(s3)
# s = {10,20,10,30,40}
# print(s)
# for x in s:
#     print(x)
# s.add(50)
# s.remove(20)
# l=len(s)
# print(s)
# print(l)
s1 ={1,2,3}
s2 ={3,4,5}
print(s1 | s2) #union  {1, 2, 3, 4, 5}
print(s1 & s2) #intersection {3}
print(s1 - s2) #difference {1, 2}
print(s1 ^ s2) #symmetric difference {1, 2, 4, 5}