// Copyright (c) 2025, Sowaan and contributors
// For license information, please see license.txt



frappe.ui.form.on("Commercial Invoice", {
	// refresh(frm) {
	// },


    async sales_taxes_and_charges_template(frm)
    {
        frm.clear_table("sales_taxes_and_charges");
        if (frm.doc.sales_taxes_and_charges_template)
        {
           var sal_tax_temp_doc = await frappe.db.get_doc('Sales Taxes and Charges Template', frm.doc.sales_taxes_and_charges_template) ;
        
           sal_tax_temp_doc.taxes.forEach(template_row => {
                let child = frm.add_child("sales_taxes_and_charges", {
                    charge_type: template_row.charge_type,
                    account_head: template_row.account_head,
                    description: template_row.description,
                    cost_center: template_row.cost_center,
                    rate: template_row.rate,
                    tax_amount: (frm.doc.total_amount * template_row.rate) / 100,
                    total: ((frm.doc.total_amount * template_row.rate) / 100) + frm.doc.total_amount
                });
            });
        }
        frm.refresh_field("sales_taxes_and_charges");
    }


});





frappe.ui.form.on("Commercial Invoice Item", {


    rate: function(frm, cdt, cdn)
    {
        var row = locals[cdt][cdn] ;
        if((row.rate && row.quantity) || (row.rate == 0 || row.quantity == 0) )
        {   
            frappe.model.set_value(row.doctype, row.name, 'amount', row.rate * row.quantity) ;
        }
    },

    quantity: function(frm, cdt, cdn)
    {
        var row = locals[cdt][cdn] ;
        if((row.rate && row.quantity) || (row.rate == 0 || row.quantity == 0) )
        {   
            frappe.model.set_value(row.doctype, row.name, 'amount', row.rate * row.quantity) ;
        }
    },

});
