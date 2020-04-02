def main():
    item_amount= int(input("Number of items: "))
    total=0
    for x in range(item_amount):
        for y in range(x):
            price=float(input("Price of item:"))
            total= total+price
    if total> 100:
        total1=total*10//100
        total= float(total-total1)
    print("Your total is: $" + str(total))



main()