# Day 1 - Loan Portfolio Analyzer

loans = [
    {
        "loan_no": "L001",
        "customer_name": "Rahul Sharma",
        "loan_amount": 500000
    },
    {
        "loan_no": "L002",
        "customer_name": "Amit Kumar",
        "loan_amount": 750000
    },
    {
        "loan_no": "L003",
        "customer_name": "Priya Singh",
        "loan_amount": 300000
    }
]

print("LOAN PORTFOLIO")
print("-" * 40)

total_portfolio = 0

for loan in loans:
    print(
        f"{loan['loan_no']} | "
        f"{loan['customer_name']} | "
        f"₹{loan['loan_amount']:,}"
    )

    total_portfolio += loan["loan_amount"]

print("-" * 40)
print(f"Total Portfolio Value: ₹{total_portfolio:,}")