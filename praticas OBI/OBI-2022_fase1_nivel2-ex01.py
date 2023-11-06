D = int(input())
A = int(input())
N = int(input())

if N < 15:
    custo = (31-(N-1))*(D+(N-1)*A)
else:
    custo = (31-(N-1))*(D+14*A)
print(custo)