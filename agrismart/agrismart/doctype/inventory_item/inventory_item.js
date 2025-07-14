// Copyright (c) 2025, Gaurav and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Inventory Item", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Inventory Item', {
    refresh: function(frm) {
        if (frm.doc.current_stock < frm.doc.reorder_level) {
            frappe.msgprint({
                title: __('Low Stock Alert'),
                message: __('⚠️ Stock is below reorder level!'),
                indicator: 'red'
            });
        }
        frm.add_custom_button("Check Reorder & Auto PR",function (){
            frappe.call({
                method: 'agrismart.agrismart.doctype.inventory_item.inventory_item.check_reorder',
                callback: function() {
                    frappe.msgprint("Reorder check complete.");
                }
            })
        })
    }
});
