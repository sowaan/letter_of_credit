# Copyright (c) 2025, Sowaan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import money_in_words


class CommercialInvoice(Document):

	def before_save(self) :

		self.setting_sales_invoice_items()
		self.calculate_items_total()
	
		self.update_tax_table()
		self.calculate_total_taxes_and_charges()

		self.grand_total = self.total_amount + self.total_taxes_and_charges

		self.calculating_foreign_currency()
		self.in_words = money_in_words(self.grand_total)



	def calculate_items_total(self) :
		total_quantity = 0
		total_amount = 0

		if self.items :
			for row in self.items :
				row.amount = row.quantity * row.rate
				total_quantity = total_quantity + row.quantity
				total_amount = total_amount + row.amount

		self.total_quantity = total_quantity
		self.total_amount = total_amount
		self.amount_in_foreign_currency = self.total_amount * self.exchange_rate

	def setting_sales_invoice_items(self) :
		si_net_total = 0
		si_vat = 0
		si_grand_total = 0
		self.items = []
		item_map = {}

		if self.sales_invoices :
			for row in self.sales_invoices :
				
				si_net_total = si_net_total + row.total
				si_vat = si_vat + row.vat
				si_grand_total = si_grand_total + row.grand_total
	
				si_doc = frappe.get_doc('Sales Invoice', row.sales_invoice)
				if si_doc.items:
					for item in si_doc.items:
						key = (item.item_code, item.uom, item.rate)
						if key in item_map:
							item_map[key]['quantity'] += item.qty
							item_map[key]['amount'] += item.amount
						else:
							item_map[key] = {
								'item_code': item.item_code,
								'item_name': item.item_name,
								'uom': item.uom,
								'description': item.description,
								'quantity': item.qty,
								'rate': item.rate,
								'amount': item.amount
							}
				
		self.si_net_total = si_net_total
		self.si_vat = si_vat
		self.si_grand_total = si_grand_total
		for item in item_map.values():
			self.append('items', item)

	def update_tax_table(self) :
		if self.sales_taxes_and_charges :
			for row in self.sales_taxes_and_charges :
				row.tax_amount = self.total_amount * row.rate / 100
				row.total = row.tax_amount + self.total_amount

	def calculate_total_taxes_and_charges(self) :
		total_taxes_and_charges = 0
		if self.sales_taxes_and_charges :
			for row in self.sales_taxes_and_charges :
				total_taxes_and_charges = total_taxes_and_charges + row.tax_amount
		self.total_taxes_and_charges = total_taxes_and_charges

	def calculating_foreign_currency(self) :
		self.total_taxes_and_charges_in_foreign_currency = self.total_taxes_and_charges * self.exchange_rate
		self.grand_total_in_for_currency = self.grand_total * self.exchange_rate













































































	


	






		


