frappe.ui.form.on('Employee', {

    validate: function(frm) {

        let today = frappe.datetime.get_today();

        //  1. Probation (DOJ <= today <= probation_end_date)
        if (
            frm.doc.date_of_joining &&
            frm.doc.custom_probation_end_date &&
            today >= frm.doc.date_of_joining &&
            today <= frm.doc.custom_probation_end_date
        ) {
            frm.set_value('custom_employment_stage', 'Probation');
        }

        //  2. Joining (before probation OR fallback)
        else if (frm.doc.date_of_joining) {
            frm.set_value('custom_employment_stage', 'Joining');
        }

    }

});