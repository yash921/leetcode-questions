#CodeForces
############################################

# Problem -  4A - Watermelon 
# n = int(input())
# if n % 2 == 0:
#     print("YES")
# else:
#     print("NO")

############################################

# Problem - 71A - Way Too Long Words
# n = int(input())
# lisT = []
# for i in range(n):
#     lisT.append(input())
# for j in lisT:
#     if len(j[:]) > 10:
#         print(j[0]+ str(len(j)-2) + j[-1])
#     else:
#         print(j)

############################################

# Problem - 3
# n = input()
# s = ""
# for i in range(len(n)):
#     char = n[i].lower()    
#     if char in "bcdfghjklmnpqrstvwxz":
#         s = s + "." + char    
# print(s)

###########################################

# Problem - A. Petya and Strings

# #Sol - 1
# s1 = input().lower()
# s2 = input().lower()

# result = 0

# for i in range(len(s1)):
#     if ord(s1[i]) > ord(s2[i]):
#         result = 1
#         break
#     elif ord(s1[i]) < ord(s2[i]):
#         result = -1
#         break
#     else:
#         result = 0

# print(result)
        
#Sol - 2
# z = input;a = z().lower();b = z().lower()
# print((a>b) - (a<b))

##############################################

# Problem - A. Helpful Maths

# n = input()
# lisT = n.rsplit("+")
# lisT.sort()
# print("+".join(lisT))

##############################################
# n = int(input())
# liSt = list(map(int, input().strip().split()))
# sums = count = 0
# liSt.sort()
# for i in reversed(range(len(liSt))):
#     sums = sums + liSt[i]
#     liSt.remove(liSt[i])
#     count += 1
#     if sums > sum(liSt):
#         break
# print(count)

# s = input()
# # lisT = list(s)
# # lisT.sorted()
# # print(lisT)
# # # if emp == "hello":
# # #     print("YES")
# # # else:
# # #     print("No")
# S = ''.join(sorted(set(s), key=s.index))
# ans = ""
# for i in S:
#     if i == "h" or i == "e" or i == "l" or i == "o":
#         ans += i
# if ans == "helo":
#     print("YES")
# else:
#     print("NO")
        
    
#############################################################
# Problem - A. Lucky Division
# n = int(input())
# if n % 4 == 0 or n % 7 == 0 or n % 47 == 0:
#     ans = "YES"
# else:
#     string = str(n)
#     for i in range(len(string)):
#         if string[i] == "4" or string[i] == "7":
#             ans = "YES"
#             continue
#         ans = "NO"
#         break
# print(ans)

        
    
    