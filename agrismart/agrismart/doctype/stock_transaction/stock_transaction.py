# Copyright (c) 2025, Gaurav and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StockTransaction(Document):
    def on_submit(self):
        item = frappe.get_doc("Inventory Item", self.item)

        if self.type == "In":
            item.current_stock += self.quantity
        elif self.type == "Out":
            item.current_stock -= self.quantity

        item.save()
