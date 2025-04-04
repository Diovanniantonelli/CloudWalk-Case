# CloudWalk Risk Analyst Case Study – Diovanni Antonelli

This repository contains the complete solution for the CloudWalk Risk Analyst challenge. It includes data analysis, visualization, a fraud detection strategy, and a working anti-fraud simulation engine based on historical transaction data.

---

## 📁 Folder Structure

```
.
├── /Notebook/
│   └── analysis.ipynb         # Jupyter notebook with all analysis steps
├── /database/
│   └── Transactions.xlsx                  # Provided dataset
│   └── Transactions_with_flags.xlsx       # Output dataset with antifraud flags
├── antifraud.py  # Antifraud solution
└── README.md
```

---

## 📌 Challenge Questions Answered

✅ **Part 1 & 2 – Payment Industry:**
- Explained the money and information flow, roles of acquirers and gateways, and the chargeback process.
- Introduced anti-fraud mechanisms and how acquirers use them.
- Sources: Visa, Mastercard, EPC, PCI SSC.

✅ **Part 3 – Get Your Hands Dirty:**
- Cleaned and explored the dataset using Python (pandas, seaborn, matplotlib).
- Identified fraud patterns:
  - High-frequency transactions (under 60s)
  - High-value transactions
  - Users with prior chargebacks
- Created clear visuals and explained conclusions in a structured Word report.
- Suggested mitigation actions and flagged suspicious behaviors.

---

## ⚙️ Anti-Fraud Engine

The fraud detection logic applies 3 key business rules:

1. **Previous Chargeback:** Blocks users already identified in past disputes.
2. **High Transaction Value:** Flags any transaction over R$ 3000.
3. **High Velocity:** Flags users who perform more than one transaction in under 60 seconds.

### ✅ Output

All transactions are assigned an `antifraud_decision`:

- `Approved`
- `Previous chargeback`
- `High transaction value`
- `High velocity`

Output is saved to a new file: `Transactions_with_flags.xlsx`

---

## 📤 Deliverables

- ✔️ Jupyter Notebook (.ipynb) with code, graphs, and step-by-step analysis
- ✔️ Final Word report (.docx) with question answers
- ✔️ Excel file with antifraud flags

---

## 👤 Author

**Diovanni Antonelli**  
Risk & Data Analyst | CloudWalk Case Challenge

---

## 📬 Contact

- 📧 Email: dioantonellias@gmail.com
- 🐙 GitHub: https://github.com/Diovanniantonelli
