import csv
from pathlib import Path
# import os
# import os
# print(os.getcwd())
Total_portfolio = 0
file_path = Path(__file__).parent / "loan_data.csv"
with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    print("High Risk Loans")
    for row in reader:
        # print(row)
        Total_portfolio += float(row['loan_amount'])   
        if int(row["dpd"]) > 30:
            print(
                row["loan_no"],
                row["customer_name"],
                row["dpd"]
            )     
print(f"Total Portfolio Value: ₹{Total_portfolio:,.2f}")

def get_npa_candidates(file_name):
    npa_candidates = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["dpd"]) >= 90:
                npa_candidates.append(row)
    return npa_candidates

npa_candidates = get_npa_candidates(file_path)
print("\nNPA Candidates:")
for candidate in npa_candidates:
    print(
        candidate["loan_no"],
        candidate["customer_name"],
        candidate["dpd"]
    )