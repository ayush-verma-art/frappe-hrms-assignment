import frappe
from frappe.utils import today

def update_employee_confirmation():

    employees = frappe.get_all(
        "Employee",
        filters=[
            ["status", "=", "Active"],
            ["final_confirmation_date", "is", "set"],
            ["final_confirmation_date", "<=", today()],
            ["custom_employment_stage", "!=", "Confirmed"]
        ],
        fields=["name", "final_confirmation_date"]
    )

    for emp in employees:
        doc = frappe.get_doc("Employee", emp.name)
        doc.custom_employment_stage = "Confirmed"
        doc.save(ignore_permissions=True)

    frappe.db.commit()