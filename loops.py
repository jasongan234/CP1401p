for i in range(10, 101 , 10):
    print(i, end=' ')
print()
for i in range(20,0,-1):
    print(i, end=' ')
print()


stars= int(input("Number of stars: "))
for x in range(stars+1):
    for y in range(x):
        print(str("*"), end="")
    print("\n")

