# Copyright (c) 2025, Sowaan and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	# columns, data = [], []

	values = {
			'lc_register' : filters.get('lc_register') ,
	}

	result = frappe.db.sql("""
		SELECT
			lc.name as name,
			lc.lc_reference as lc_reference,
			so.name as sales_order ,
			so.po_no as po_no ,
			lc.customer_name as customer,
			lc.lc_date_of_issue as lc_date_of_issue,
			lc.lc_date_ofexpiry as lc_date_ofexpiry,
			lc.lc_amount as lc_amount,
			lc.total_commercial_invoices_amount as total_commercial_invoices_amount,
			IFNULL(SUM(pe.paid_amount), 0) as settlement,
			(lc.lc_amount - lc.total_commercial_invoices_amount - IFNULL(SUM(pe.paid_amount), 0)) as available_balance ,
			lc.description_of_goods_or_services as description			
					
		FROM `tabLC Register` lc
		LEFT JOIN `tabPayment Entry` pe 
			ON pe.lc_register = lc.name 
			AND pe.party = lc.customer_name 
			AND pe.docstatus = 1
		LEFT JOIN `tabSales Order` so ON so.lc_register = lc.name AND so.customer = lc.customer_name AND so.docstatus = 1
		WHERE lc.docstatus = 1
		AND lc.lc_group = 'Export'
		AND (lc.name = %(lc_register)s OR %(lc_register)s IS NULL)
		GROUP BY lc.name
	""", values=values, as_dict=True)


	max_amendments = 0
	for row in result:
		amendments = frappe.get_all("LC Amendment Details", 
			filters={"parent": row["name"]},
			fields=["lc_amendment_amount"],
			order_by="idx")
		
		for i, amend in enumerate(amendments):
			row[f"amendment_{i+1}"] = amend["lc_amendment_amount"]
		
		max_amendments = max(max_amendments, len(amendments))


	columns = [
		{ 'label':'LC Number', 'fieldname':'name', 'fieldtype':'Link', 'options':'LC Register', 'width':200 },
		{ 'label':'LC Reference', 'fieldname':'lc_reference', 'fieldtype':'Data', 'width':150 },
		
		{ 'label':'SOD NO', 'fieldname':'sales_order', 'fieldtype':'Link', 'options':'Sales Order', 'width':200 },
		{ 'label':'LPO NO / CONTRACT', 'fieldname':'po_no', 'fieldtype':'Data', 'width':150 },
		
		{ 'label':'Benificiary', 'fieldname':'customer', 'fieldtype':'Link', 'options':'Customer', 'width':150 },
		{ 'label':'Date of Issue', 'fieldname':'lc_date_of_issue', 'fieldtype':'Date', 'width':120 },
		{ 'label':'Date of Expiry', 'fieldname':'lc_date_ofexpiry', 'fieldtype':'Date', 'width':120 },
		{ 'label':'LC Amount', 'fieldname':'lc_amount', 'fieldtype':'Currency', 'width':120 },

	]

	for i in range(max_amendments):
		columns.append({
			'label': f'Amendment {i+1}',
			'fieldname': f'amendment_{i+1}',
			'fieldtype': 'Currency',
			'width': 170
		})
				
	columns.append(
			{ 'label':'Total Invoices', 'fieldname':'total_commercial_invoices_amount', 'fieldtype':'Currency', 'width':150 },
	)    
	columns.append(
			{ 'label':'Settlement', 'fieldname':'settlement', 'fieldtype':'Currency', 'width':150 },
	)    
	columns.append(
			{ 'label':'Available Balance', 'fieldname':'available_balance', 'fieldtype':'Currency', 'width':150 },
	)    
	columns.append(
			{  'label':'Description', 'fieldname':'description', 'fieldtype':'Data', 'width':'300%'   },
	)  
	

	return columns, result
