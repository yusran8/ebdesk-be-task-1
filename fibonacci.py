
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n<len(fib_seq):
        return fib_seq[n]
    else:
        return (fibonacci(n-1)**2) + fibonacci(n-2)


n = int(input("input size of fibonacci: "))
fib_seq = []
for i in range(n):
    fib_seq.append(fibonacci(i))

for _ in fib_seq:
    print(_, end=' ')