def main():
    bill_amount = float(input("Enter the bill amount: "))
    tip_percent = float(input("Enter the tip percentage: "))

    tip_amount = bill_amount * (tip_percent / 100)
    total_amount = bill_amount + tip_amount

    print(f"\nBill amount: ${bill_amount:.2f}")
    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total amount: ${total_amount:.2f}")


if __name__ == "__main__":
    main()
