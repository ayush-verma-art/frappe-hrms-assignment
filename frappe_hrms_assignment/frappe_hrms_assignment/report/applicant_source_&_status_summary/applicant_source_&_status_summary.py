# Copyright (c) 2026, Ayush Verma and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    filters = filters or {}

    conditions = ""

    if filters.get("name"):
        conditions += f" AND name = '{filters.get('name')}'"

    if filters.get("applicant_name"):
        conditions += f" AND applicant_name LIKE '%{filters.get('applicant_name')}%'"

    if filters.get("custom_source_of_application"):
        conditions += f" AND custom_source_of_application = '{filters.get('custom_source_of_application')}'"

    columns = [
        {"label": "Applicant", "fieldname": "name", "fieldtype": "Link", "options": "Job Applicant", "width": 200},
        {"label": "Applicant Name", "fieldname": "applicant_name", "fieldtype": "Data", "width": 200},
        {"label": "Email", "fieldname": "email_id", "fieldtype": "Data", "width": 200},
        {"label": "Phone", "fieldname": "phone_number", "fieldtype": "Data", "width": 150},
        {"label": "Source", "fieldname": "custom_source_of_application", "fieldtype": "Data", "width": 150},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 150},
        {"label": "Application Stage", "fieldname": "workflow_state", "fieldtype": "Data", "width": 150}
        
    ]

    data = frappe.db.sql(f"""
        SELECT
            name,
            applicant_name,
            email_id,
            phone_number,
            custom_source_of_application,
            workflow_state,
            status
        FROM `tabJob Applicant`
        WHERE 1=1 {conditions}
        ORDER BY creation DESC
    """, as_dict=1)

    return columns, data