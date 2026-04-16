frappe.ui.form.on('Salary Structure Assignment', {
    employee: function(frm) {
        if (frm.doc.employee) {

            frappe.db.get_value('Employee', frm.doc.employee, 'custom_tax_regime_preference')
                .then(r => {

                    let regime = r.message.custom_tax_regime_preference;
                 
                    if (regime === "Old Regime") {
                        frm.set_value('salary_structure', 'Old Regime Structure');
                        frm.set_value('income_tax_slab', 'Old Regime FY2025-26');
                    } 
                    else if (regime === "New Regime") {
                        frm.set_value('salary_structure', 'New Regime Structure');
                        frm.set_value('income_tax_slab', 'New Regime FY 2025-26');
                    }

                });
        }
    }
});