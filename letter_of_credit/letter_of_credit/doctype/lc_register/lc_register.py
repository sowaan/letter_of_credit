# Copyright (c) 2025, Sowaan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LCRegister(Document):
	# pass
    def before_save(self) :
        self.caluculate_totals_of_sales_or_purchase_invoices()
        self.calculate_lc_amount()

    def on_update_after_submit(self) :
        self.caluculate_totals_of_sales_or_purchase_invoices()
        

        

    def caluculate_totals_of_sales_or_purchase_invoices(self) :
        
        net_total = 0
        vat = 0
        grand_total = 0

        if self.lc_group == 'Export' :
            if self.commercial_invoices :
                for row in self.commercial_invoices :
                    net_total = net_total + row.total
                    vat = vat + row.vat
                    grand_total = grand_total + row.grand_total
            
            self.ci_net_total = net_total
            self.ci_total_vat = vat
            self.total_commercial_invoices_amount = grand_total

        
        elif self.lc_group == 'Import' :
            if self.purchase_invoices :
                for row in self.purchase_invoices :
                    net_total = net_total + row.total
                    vat = vat + row.vat
                    grand_total = grand_total + row.grand_total
            self.pi_net_total = net_total
            self.pi_total_vat = vat
            self.total_purchase_invoice_amount = grand_total

    def calculate_lc_amount(self) :
        self.lc_amount_in_aed = self.lc_amount * self.exchange_rate


