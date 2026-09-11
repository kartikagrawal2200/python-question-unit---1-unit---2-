n = int(input())
reversed_num = 0
while n > 0:
   digit = n % 10  
   reversed_num = reversed_num * 10 + digit
print(reversed_num)
