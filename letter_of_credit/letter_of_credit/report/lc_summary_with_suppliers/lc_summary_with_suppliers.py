# Copyright (c) 2025, Sowaan and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	
	values = {
		'supplier' : filters.get('supplier') ,
	}

	result = frappe.db.sql("""

		SELECT
			lc.supplier as supplier,
			SUM(lc.lc_amount) as lc_amount,
			SUM(lc.total_purchase_invoice_amount) as purchase_invoice_amount,
			IFNULL(SUM(DISTINCT pe.paid_amount), 0) as payment_entry_amount ,
			(SUM(lc.lc_amount)) - ( (SUM(lc.total_purchase_invoice_amount)) + (IFNULL(SUM(DISTINCT pe.paid_amount), 0)) ) as balance

		FROM `tabLC Register` lc
		LEFT JOIN `tabPayment Entry` pe 
			ON pe.party = lc.supplier AND pe.docstatus = 1

		WHERE lc.docstatus = 1
		AND lc.lc_group = 'Import'
		AND (lc.supplier = %(supplier)s OR %(supplier)s IS NULL)

		GROUP BY lc.supplier

	""", values=values, as_dict=1)

	columns = [

			{  'label':'Supplier', 'fieldname':'supplier', 'fieldtype':'Link', 'options':'Supplier', 'width':'150%'   },
			{  'label':'LC Amount', 'fieldname':'lc_amount', 'fieldtype':'Currency', 'width':'150%'   },
			{  'label':'Total Invoice', 'fieldname':'purchase_invoice_amount', 'fieldtype':'Currency', 'width':'200%'   },
			{  'label':'Settlement', 'fieldname':'payment_entry_amount', 'fieldtype':'Currency', 'width':'200%'   },
			{  'label':'Available Balance', 'fieldname':'balance', 'fieldtype':'Currency', 'width':'200%'   },

	]

	return columns, result




