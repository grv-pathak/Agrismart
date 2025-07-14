// Copyright (c) 2025, Gaurav and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Stock Transaction", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Stock Transaction', {
    item: function(frm) {
        if (frm.doc.item) {
            frappe.db.get_value('Inventory Item', frm.doc.item, 'uom', function(r) {
                frm.set_value('uom', r.uom);
            });
            frm.set_df_property('quantity', 'read_only', 0);
        } else {
            frm.set_df_property('quantity', 'read_only', 1);
        }
    }
});
