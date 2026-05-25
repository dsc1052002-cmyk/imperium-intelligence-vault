import os
import re
import pandas as pd

# 1. Hardcoded Current Master Portfolio Data as of late May 2026
portfolio_data = {
    "Asset/Sector": [
        "Semiconductors (NVDA/TSM)",
        "Eli Lilly (LLY)",
        "GE Aerospace & Aviation",
        "Tesla (TSLA)",
        "Hard Bullion Anchor (Gold)",
        "Northrop Grumman (NOC)",
        "Sovereign Bank Cash Vault"
    ],
    "Allocation ($ Billions)": [27.80, 7.08, 15.48, 10.00, 10.00, 0.96, 10.00]
}

def analyze_imperium_capital():
    # 2. Convert raw matrix data into a clean Data Structure (DataFrame)
    df = pd.DataFrame(portfolio_data)
    
    # 3. Calculate mathematical totals and individual asset concentrations
    total_aum = df["Allocation ($ Billions)"].sum()
    df["Concentration %"] = (df["Allocation ($ Billions)"] / total_aum) * 100
    
    # 4. Print a clean, scannable data summary to the execution terminal
    print(f"\n================ IMPERIUM MASTER LEDGER AUDIT ================")
    print(f"TOTAL ASSETS UNDER MANAGEMENT: ${total_aum:.2f} BILLION")
    print(f"SAFE UNTOUCHED RESERVES:       $10.00 BILLION")
    print(f"ACTIVE EXPOSED MOATS:          ${total_aum - 10.00:.2f} BILLION")
    print(f"==============================================================\n")
    print(df.to_string(index=False, formatters={"Concentration %": "{:,.2f}%".format}))

if __name__ == "__main__":
    analyze_imperium_capital()
