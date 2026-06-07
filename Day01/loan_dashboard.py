print("=" * 40)
print("LOAN ANALYTICS DASHBOARD")
print("=" * 40)
import csv
import pandas as pd 
from pathlib import Path
file_path = Path(__file__).parent / "loan_data.csv"
loans_df = pd.read_csv(file_path)
loan_count = loans_df["loan_amount"].count()   
total_portfolio_value = loans_df["loan_amount"].sum()   
average_portfolio_value = loans_df["loan_amount"].mean()
max_loan_value = loans_df["loan_amount"].max()
npa_candidates = loans_df[loans_df["dpd"] > 30].count().loan_amount
npa_candidates1 = loans_df[loans_df["dpd"] >= 90].count().loan_amount

print(f"\nTotal Number of Loans: \n{loan_count}")
print(f"\nTotal Portfolio Value: \n₹{total_portfolio_value:,.2f}")
print(f"\nAverage Loan Amount: \n₹{average_portfolio_value:,.2f}")
print(f"\nHighest Loan Amount: \n₹{max_loan_value:,.2f}")
print(f"\nHigh Risk Loans (30+ days DPD): \n{npa_candidates}")
print(f"\nHigh Risk Loans (90+ days DPD): \n{npa_candidates1}")

def get_risk_category(dpd):
    if dpd == 0:
        return "Current"
    elif dpd <= 30:
        return "Low Risk"
    elif dpd <= 60:
        return "Medium Risk"
    else:
        return "High Risk"

loans_df["risk_category"] = loans_df["dpd"].apply(get_risk_category)
print("\nLoan Risk Categories:")
print(loans_df[["loan_no", "customer_name", "dpd", "risk_category"]])