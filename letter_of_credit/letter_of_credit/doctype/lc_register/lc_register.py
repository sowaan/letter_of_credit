# Copyright (c) 2025, Sowaan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LCRegister(Document):
	# pass
    def before_save(self) :
        total = 0
        if self.commercial_invoices :
            for row in self.commercial_invoices :
                total = total + row.grand_total
        self.total_commercial_invoices_amount = total

