// Copyright (c) 2026, Ayush Verma and contributors
// For license information, please see license.txt

frappe.query_reports["Applicant Source & Status Summary"] = {
    "filters": [
        {
            "fieldname": "name",
            "label": "Applicant ID",
            "fieldtype": "Link",
            "options": "Job Applicant"
        },
        {
            "fieldname": "applicant_name",
            "label": "Applicant Name",
            "fieldtype": "Data"
        },
        {
            "fieldname": "custom_source_of_application",
            "label": "Source",
            "fieldtype": "Select",
            "options": "\nLinkedIn\nReferral\nJob Portal"
        }
    ]
};
