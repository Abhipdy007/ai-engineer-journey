def calculate_interest(principal, rate):
    interest = principal * rate / 100
    return interest


interest = calculate_interest(500000, 11.5)

print("Interest:", interest)

def calculate_monthly_interest(principal, annual_rate):
    return principal * annual_rate / 100 / 12


emi_interest = calculate_monthly_interest(
    500000,
    11.5
)

print("Monthly Interest:", round(emi_interest, 2))


def get_portfolio_value(loans):
    total = 0

    for loan in loans:
        total += loan["loan_amount"]

    return total
    
loans = [
    {"loan_no": "L001", "loan_amount": 500000},
    {"loan_no": "L002", "loan_amount": 750000},
    {"loan_no": "L003", "loan_amount": 300000}
]

portfolio_value = get_portfolio_value(loans)

print(f"Portfolio Value: ₹{portfolio_value:,}")

def get_high_value_loans(loans, threshold):
    return [
        loan
        for loan in loans
        if loan["loan_amount"] > threshold and loan["dpd"] >30
    ]
    



loans = [
    {"loan_no": "L001", "loan_amount": 500000, "dpd": 0},
    {"loan_no": "L002", "loan_amount": 750000, "dpd": 45},
    {"loan_no": "L003", "loan_amount": 300000, "dpd": 60},
]

high_value_loans = get_high_value_loans(loans, 500000)

print("High Value Loans:", high_value_loans)