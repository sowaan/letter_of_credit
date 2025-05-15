# Copyright (c) 2025, Sowaan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import money_in_words


class CommercialInvoice(Document):

	def before_save(self) :
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

		self.update_tax_table()
		self.calculate_total_taxes_and_charges()

		self.grand_total = self.total_amount + self.total_taxes_and_charges

		self.calculating_foreign_currency()
		self.in_words = money_in_words(self.grand_total)


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




	


	






		


