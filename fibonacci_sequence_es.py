def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n

n = int(input('Inserisci il numero: ' ))
print('Sequenza fibonacci')
for i in range(1, n+1):
    print(rec_fib(i))
