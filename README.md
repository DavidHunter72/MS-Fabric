# Microsoft Fabric Workbook Importer

A Python automation script built during training at **Mission Ready HQ** to streamline importing Power BI workbooks into a Microsoft Fabric workspace.

---

## 📋 What It Does

- Authenticates with Microsoft Azure using OAuth 2.0 client credentials
- Connects to the Power BI REST API
- Automates the import of workbooks into a specified Microsoft Fabric workspace

---

## 🛠️ Built With

- **Python** — core scripting
- **Microsoft Fabric** — target workspace platform
- **Power BI REST API** — workbook management
- **Azure AD / OAuth 2.0** — secure authentication

---

## ⚙️ Setup

1. Clone the repository:
```bash
   git clone https://github.com/DavidHunter72/MS-Fabric.git
```

2. Install dependencies:
```bash
   pip install requests
```

3. Set the following environment variables:
```bash
   CLIENT_ID=your-azure-client-id
   CLIENT_SECRET=your-azure-client-secret
   TENANT_ID=your-azure-tenant-id
   WORKSPACE_ID=your-fabric-workspace-id
```

4. Run the script:
```bash
   python import_fabric_workbooks.py
```

---

## 🔐 Security Note

All credentials are loaded from environment variables — no secrets are stored in the code.

---

## 👤 Author

**David Hunter**  
Data Analytics Trainee @ Mission Ready HQ | On Placement @ Seen Ventures  
[GitHub](https://github.com/DavidHunter72)


---

## 📊 Mission X Sales Dashboard (Power BI)

A multi-page Power BI report analysing retail sales data across 2015–2018.

**Report pages include:**
- Sales overview with total revenue ($1.92M across the dataset)
- Monthly and daily sales trend analysis
- Year-on-year comparison using DAX time intelligence (TOTALYTD)
- Top products and categories by quantity sold
- Geographic sales breakdown across multiple countries

**Skills demonstrated:**
- DAX measures including TOTALYTD and year-over-year comparisons
- Time intelligence functions
- Multi-page report design
- Geographic and categorical visualisations
