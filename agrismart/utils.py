import frappe

@frappe.whitelist()
def get_farm_items(doctype, txt, searchfield, start, page_len, filters):
    farm = filters.get("farm")

    if not farm:
        return []

    # Fetch distinct items used in stock transactions at that farm
    return frappe.db.sql("""
        SELECT DISTINCT item
        FROM `tabStock Transaction`
        WHERE farm = %s AND item LIKE %s
        LIMIT %s OFFSET %s
    """, (farm, "%" + txt + "%", page_len, start))
