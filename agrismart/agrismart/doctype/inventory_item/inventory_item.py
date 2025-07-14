# Copyright (c) 2025, Gaurav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class InventoryItem(Document):
    pass


@frappe.whitelist()
def check_reorder():
    items = frappe.get_all("Inventory Item", fields=["name", "current_stock", "reorder_level"])

    for item in items:
        if item.current_stock < item.reorder_level:
            # Check if a PR already exists for this item
            existing = frappe.get_all("Purchase Request", filters={
                "item": item.name,
                "status": ["in", ["Draft", "Approved"]]
            })

            if not existing:
                pr = frappe.new_doc("Purchase Request")
                pr.item = item.name
                pr.quantity = item.reorder_level - item.current_stock
                pr.status = "Draft"
                # Optional: assign farm and date
                pr.farm = frappe.db.get_value("Stock Transaction", {"item": item.name}, "farm") or "Farm Alpha"
                pr.required_by = nowdate()

                try:
                    pr.insert(ignore_permissions=True)
                    frappe.db.commit()
                except Exception as e:
                    frappe.log_error(f"Auto PR failed for {item.name}: {e}", "check_reorder")
