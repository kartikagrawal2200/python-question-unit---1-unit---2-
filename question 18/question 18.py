n = int(input())
if n == 0:
	digit_count = 1
else:
	digit_count = 0
	while n > 0:
	   digit_count += 1
	   n = n // 10 
	    
print(digit_count)
