import csv
import pandas as pd
from pathlib import Path
# file_path = pathlib.Path(__file__).parent / "loan_data.csv"
file_path = Path(__file__).parent / "loan_data.csv"
loans_df = pd.read_csv(file_path)

print("High Risk Loans:")
high_risk_loans = loans_df[loans_df["dpd"] > 30]
print(high_risk_loans[["loan_no", "customer_name", "dpd"]])

total_portfolio_value = loans_df["loan_amount"].sum()
print(f"\nTotal Portfolio Value: ₹{total_portfolio_value:,.2f}")    

average_portfolio_value = loans_df["loan_amount"].mean()
print(f"\nAverage Loan Amount: ₹{average_portfolio_value:,.2f}")    

Max_loan_value = loans_df["loan_amount"].max()
print(f"\nHighest Loan Amount: ₹{Max_loan_value:,.2f}")    

npa_candidates = loans_df[loans_df["dpd"] > 30]
print("\nNPA Candidates:")
print(npa_candidates[["loan_no", "customer_name", "dpd"]])  

conditional_value = loans_df[(loans_df["dpd"] > 30) & (loans_df["loan_amount"] > 500000)]
print("\nconditional_value:")
print(conditional_value[["loan_no", "customer_name", "dpd", "loan_amount"]])  

All_loans_where = loans_df[loans_df["loan_amount"] > 500000]
print("\nAll loans where loan_amount > 500000 :")
print(All_loans_where[["loan_no", "customer_name", "dpd", "loan_amount"]])  
