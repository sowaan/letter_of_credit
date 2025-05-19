# Copyright (c) 2025, Sowaan and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	
	values = {
		'customer' : filters.get('customer') ,
	}

	result = frappe.db.sql("""

		SELECT
			lc.customer_name as customer,
			SUM(lc.lc_amount) as lc_amount,
			SUM(lc.total_commercial_invoices_amount) as comm_inv_amount,
			IFNULL(SUM(DISTINCT pe.paid_amount), 0) as payment_entry_amount ,
			(SUM(lc.lc_amount)) - ( (SUM(lc.total_commercial_invoices_amount)) + (IFNULL(SUM(DISTINCT pe.paid_amount), 0)) ) as balance

		FROM `tabLC Register` lc
		LEFT JOIN `tabPayment Entry` pe 
			ON pe.party = lc.customer_name AND pe.docstatus = 1

		WHERE lc.docstatus = 1
		AND (lc.customer_name = %(customer)s OR %(customer)s IS NULL)

		GROUP BY lc.customer_name

	""", values=values, as_dict=1)

	columns = [

			{  'label':'Customer', 'fieldname':'customer', 'fieldtype':'Link', 'options':'Customer', 'width':'150%'   },
			{  'label':'LC Amount', 'fieldname':'lc_amount', 'fieldtype':'Currency', 'width':'150%'   },
			{  'label':'Total Invoice', 'fieldname':'comm_inv_amount', 'fieldtype':'Currency', 'width':'200%'   },
			{  'label':'Settlement', 'fieldname':'payment_entry_amount', 'fieldtype':'Currency', 'width':'200%'   },
			{  'label':'Available Balance', 'fieldname':'balance', 'fieldtype':'Currency', 'width':'200%'   },

	]

	return columns, result


