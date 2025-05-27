// Copyright (c) 2025, Sowaan and contributors
// For license information, please see license.txt





frappe.ui.form.on("LC Register", {
	
    // refresh(frm) {
	// },


    lc_amount(frm) {
        calculate_amount_in_foreign_currency(frm) ;
        calculate_tolerance(frm) ;
    } ,


    exchange_rate(frm) {
        calculate_amount_in_foreign_currency(frm) ;
        calculate_tolerance(frm) ;
    } ,



    tolerence(frm) {
        calculate_tolerance(frm) ;
    } ,


    



});



function calculate_amount_in_foreign_currency(frm)
{
    if (!frm.doc.lc_amount)
    {
        frm.set_value('lc_amount', 0)
    }
    if (!frm.doc.exchange_rate)
    {
        frm.set_value('exchange_rate', 0)
    } 

    frm.set_value('lc_amount_in_aed', frm.doc.lc_amount * frm.doc.exchange_rate) ;
}

function calculate_tolerance(frm) {
    if (!frm.doc.lc_amount_in_aed)
    {
        frm.set_value('lc_amount_in_aed', 0) ;
    }
    if (!frm.doc.tolerence)
    {
        frm.set_value('tolerence', 0) ;
    }

    frm.set_value('lc_amount_after_tolerance', (frm.doc.lc_amount_in_aed*frm.doc.tolerence/100) + frm.doc.lc_amount_in_aed ) ;

}
























