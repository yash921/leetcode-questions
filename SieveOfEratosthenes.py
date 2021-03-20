# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 16 15:24:58 2020

# @author: yash
# """

# # n using Sieve of Eratosthenes

# def SieveOfEratosthenes(n):
#     prime = [True for num in range(n+1)]
#     p = 2
#     while (p*p <= n):
#         if prime[p] == True:
            
#             for i in range(p*2, n+1, p):
#                 prime[i] = False
#         p += 1
    
#     prime[0] = False
#     prime[1] = False
    
#     for p in range(n+1):
#         if prime[p]:
#             print(p)
  

# # driver program

# if __name__=='__main__':

#     n = 10

#     print("Following are the prime numbers smaller")

#     #Use print("Following are the prime numbers smaller") for Python 3

#     print("than or equal to", n)

#     #Use print("than or equal to", n) for Python 3

#     SieveOfEratosthenes(n) 
# Write Python3 code here 
from decimal import Decimal 

def gcd(a,b): 
	if b==0: 
		return a 
	else: 
		return gcd(b,a%b) 
p = int(input('Enter the value of p = ')) 
q = int(input('Enter the value of q = ')) 
no = int(input('Enter the value of text = ')) 
n = p*q 
t = (p-1)*(q-1) 

for e in range(2,t): 
	if gcd(e,t)== 1: 
		break


for i in range(1,10): 
	x = 1 + i*t 
	if x % e == 0: 
		d = int(x/e) 
		break
ctt = Decimal(0) 
ctt =pow(no,e) 
ct = ctt % n 

dtt = Decimal(0) 
dtt = pow(ct,d) 
dt = dtt % n 

print('n = '+str(n)+' e = '+str(e)+' t = '+str(t)+' d = '+str(d)+' cipher text = '+str(ct)+' decrypted text = '+str(dt)) 
