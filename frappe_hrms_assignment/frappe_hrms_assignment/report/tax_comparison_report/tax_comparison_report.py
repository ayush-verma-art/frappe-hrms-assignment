# Copyright (c) 2026, Ayush Verma and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):

    columns = [
        {"label": "Employee", "fieldname": "employee", "fieldtype": "Data", "width": 140},
        {"label": "Employee Name", "fieldname": "employee_name", "fieldtype": "Data", "width": 150},
        {"label": "Regime", "fieldname": "regime", "fieldtype": "Data", "width": 120},
        {"label": "Gross Pay", "fieldname": "gross_pay", "fieldtype": "Currency", "width": 120},
        {"label": "Investment Benefit", "fieldname": "investment", "fieldtype": "Currency", "width": 150},
        {"label": "Income Tax", "fieldname": "income_tax", "fieldtype": "Currency", "width": 120},
        {"label": "Net Pay", "fieldname": "net_pay", "fieldtype": "Currency", "width": 120},
        {"label": "Better Regime", "fieldname": "better_regime", "fieldtype": "Data", "width": 150},
    ]

    data = []

    salary_slips = frappe.get_all(
        "Salary Slip",
        fields=[
            "name",
            "employee",
            "employee_name",
            "gross_pay",
            "total_deduction",
            "net_pay"
        ]
    )

    for slip in salary_slips:

        #  Get regime
        regime = frappe.db.get_value(
            "Employee",
            slip.employee,
            "custom_tax_regime_preference"
        )

        # Default values
        income_tax = 0
        investment = 0

        #  Get deductions (Income Tax + Investment Adjustment)
        deductions = frappe.get_all(
            "Salary Detail",
            filters={
                "parent": slip.name,
                "parentfield": "deductions"
            },
            fields=["salary_component", "amount"]
        )

        for d in deductions:
            if d.salary_component == "Income Tax":
                income_tax = d.amount

            if d.salary_component == "Investment Adjustment":
                investment = d.amount

        if regime == "Old Regime" and investment > 0:
            better = "Old Regime (Benefit Taken)"
        else:
            better = "New Regime (No Benefit)"

        data.append({
            "employee": slip.employee,
            "employee_name": slip.employee_name,
            "regime": regime,
            "gross_pay": slip.gross_pay,
            "investment": investment,
            "income_tax": income_tax,
            "net_pay": slip.net_pay,
            "better_regime": better
        })

    return columns, data