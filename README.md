# Frappe HRMS Assignment – Custom Implementation

## 📌 Overview
This project is a custom implementation built using the Frappe Framework and ERPNext HRMS module.  
It covers recruitment workflow, employee lifecycle automation, payroll setup, tax regime handling, and external API integration.

---

## ⚙️ Tech Stack
- Frappe Framework (v15)
- ERPNext HRMS
- Python
- JavaScript (Client Scripts)
- MySQL / MariaDB

---

## 🚀 Features Implemented

### 🔹 1. Recruitment Workflow
- Custom recruitment flow:
  - Job Opening → Application → Screening → Interview → Offer → Hired
- Added **Source of Application** field in Job Applicant
- Created **Job Application Source & Status Summary Report**

---

### 🔹 2. Employee Lifecycle Management
- Implemented lifecycle stages:
  - Joining → Probation → Confirmation → Exit
- Added:
  - **Probation End Date**
- Automation:
  - Employee confirmation auto-update using scheduler
  - Experience letter generation on employee exit

---

### 🔹 3. Payroll & Salary Structure
- Created salary structure with:
  - Basic
  - HRA
  - Special Allowance
  - PF
  - Professional Tax
- Configured payroll entry for multiple employees
- Custom payroll print format

---

### 🔹 4. Tax Regime Implementation
- Added **Tax Regime Preference** in Employee
- Supported:
  - Old Regime
  - New Regime
- Salary structure selection based on employee preference

---

### 🔹 5. Custom Doctype – Employee Investment Declaration
- Fields included:
  - Section 80C (LIC, PPF, ELSS)
  - Section 80D (Medical Insurance)
  - Other Exemptions
- Implemented **automatic total calculations**

---

### 🔹 6. Crypto Price API Integration
- Custom Doctype for cryptocurrency rates
- Integrated **CoinGecko API**
- Features:
  - Fetch latest crypto prices
  - Store historical data
  - Pagination support in API

---

### 🔹 7. Automation & Hooks
- Implemented:
  - Scheduler-based automation
  - Doc Events
  - Method Overrides using `hooks.py`

---

## ⚙️ Setup Instructions

cd frappe-bench

bench get-app https://github.com/ayush-verma-art/frappe-hrms-assignment.git --branch develop

bench --site your-site install-app frappe_hrms_assignment
