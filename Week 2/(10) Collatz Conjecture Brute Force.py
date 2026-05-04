# odd = 3n+1, even = n/2, settles on 1 always
start = 1
end = 100000
for number in range(start,end+1):
    n = number
    sequence = [n]

    while n !=1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    print(sequence)
    sequence.clear()
