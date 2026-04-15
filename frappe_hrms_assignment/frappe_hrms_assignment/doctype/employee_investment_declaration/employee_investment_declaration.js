// Copyright (c) 2026, Ayush Verma and contributors
// For license information, please see license.txt
frappe.ui.form.on('Employee Investment Declaration', {

    calculate_totals: function(frm) {

        let total_80c = 0;
        let total_80d = 0;
        let total_other = 0;

        (frm.doc.investment_details || []).forEach(row => {

            if (row.category === "Section 80C") {
                total_80c += flt(row.amount);
            }
            else if (row.category === "Section 80D") {
                total_80d += flt(row.amount);
            }
            else if (row.category === "Other Exemptions") {
                total_other += flt(row.amount);
            }

        });

        frm.set_value('total_section_80c', total_80c);
        frm.set_value('total_section_80d', total_80d);
        frm.set_value('total_other_exemptions', total_other);

        // Grand Total
        let grand_total = total_80c + total_80d + total_other;
        frm.set_value('total', grand_total);

    },

    validate: function(frm) {
        frm.trigger('calculate_totals');

        if (frm.doc.total_section_80c > 150000) {
            frappe.throw("80C limit exceeded (Max ₹1,50,000)");
        }

        if (frm.doc.total_section_80d > 25000) {
            frappe.throw("80D limit exceeded (Max ₹25,000)");
        }
    }
});