purchase_price=int(input("Enter the purchase price: "))
selling_price=int(input("Enter the selling price: "))

if selling_price > purchase_price:
    profit=selling_price-purchase_price
    print("You got the profit of", str(profit) + "rs")

elif selling_price < purchase_price:
    loss=purchase_price-selling_price
    print("You are in loss of", str(loss) + "rs")

else:
    print("No profit no loss booked to this deal.")