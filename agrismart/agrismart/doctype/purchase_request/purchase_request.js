// Copyright (c) 2025, Gaurav and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Purchase Request", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Purchase Request', {
    farm: function(frm) {
        frappe.db.get_value('Farm', frm.doc.farm, 'farm_owner', function(r) {
            frm.set_value('farm_manager', r.farm_owner);
        });
    }
});
