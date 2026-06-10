stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

total = 0

while True:
    stock = input("Enter stock name (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        qty = int(input("Enter quantity: "))
        total += stocks[stock] * qty
    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = {total}")

print("Result saved in portfolio.txt")
