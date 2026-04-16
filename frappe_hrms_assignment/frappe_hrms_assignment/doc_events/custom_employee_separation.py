import frappe

def generate_experience_letter_scheduler():

    separations = frappe.get_all(
        "Employee Separation",
        filters=[
            ["boarding_status", "=", "Completed"]
        ],
        fields=["name", "employee"]
    )

    for sep in separations:

        # Check if already exists
        existing = frappe.get_all(
            "File",
            filters={
                "attached_to_doctype": "Employee",
                "attached_to_name": sep.employee,
                "file_name": ["like", "Experience Letter%"]
            }
        )

        if existing:
            continue  # skip if already generated

        # Get Employee
        employee = frappe.get_doc("Employee", sep.employee)

        # Generate PDF
        pdf = frappe.get_print(
            "Employee",
            employee.name,
            "Experience Letter",
            as_pdf=True
        )

        # Attach PDF
        frappe.get_doc({
            "doctype": "File",
            "file_name": f"Experience Letter - {employee.employee_name}.pdf",
            "attached_to_doctype": "Employee",
            "attached_to_name": employee.name,
            "content": pdf
        }).insert(ignore_permissions=True)

    frappe.db.commit()