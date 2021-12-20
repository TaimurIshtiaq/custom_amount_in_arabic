frappe.require('/assets/custom_amount_in_arabic/js/tafgeetjs.js');

frappe.ui.form.on('Sales Invoice', {

    before_save: function(frm) {
        var stringText = new Tafgeet(frm.doc.grand_total, 'SAR').parse();
        console.log(stringText);
        frm.set_value('in_words_arabic', stringText);
    }
});