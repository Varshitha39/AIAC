def sum_to_n(n):
    if n<=0:
        return 0
    total =0
    for i in range(1,n+1):
        total +=i
    return total

n = int(input("Enter a number:"))
result = sum_to_n(n)
print(f"The sum of numbers from 1 to {n} is {result}.")