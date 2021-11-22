def factorial(n):
	return 1 if (n==1 or n==0) else n * factorial(n - 1)

def sumDigit(n):
    tot = 0
    for digit in str(n):
        tot += int(digit)
    return tot

# Driver Code
num = 100
f = factorial(num)
s = sumDigit(f)
print (f'{num}! = {f}')
print(f'Sum of digits in {num}! = {s}')
