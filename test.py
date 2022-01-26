a, b, c = map(int, input().split())
if a <= 5 and b <= 5 and c <= 5 and (a+b+c) <= 5:
    if (a+b+c) == 5:
        print("Alikhan is a genius")
    else:
        print("Anyway genius")