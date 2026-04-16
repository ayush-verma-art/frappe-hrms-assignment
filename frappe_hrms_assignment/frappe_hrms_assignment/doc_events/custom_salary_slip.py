import frappe

def total_exemption_amount_cal(doc, method):

    if not doc.employee:
        return

    declaration = frappe.get_all(
        "Employee Investment Declaration",
        filters={
            "employee": doc.employee,
            "docstatus": 1
        },
        fields=["name", "total"],
        order_by="creation desc",
        limit=1
    )

    if not declaration:
        return

    yearly_exemption = declaration[0].total or 0
    monthly_exemption = yearly_exemption / 12

    # Check regime
    regime = frappe.db.get_value(
        "Employee",
        doc.employee,
        "custom_tax_regime_preference"
    )

    if regime == "Old Regime":

        #  ADD OR UPDATE Investment Adjustment Component
        found = False

        for d in doc.deductions:
            if d.salary_component == "Investment Adjustment":
                d.amount = monthly_exemption
                found = True

        if not found:
            doc.append("deductions", {
                "salary_component": "Investment Adjustment",
                "amount": monthly_exemption
            })