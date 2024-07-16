// Copyright (c) 2024, Gursewak Singh and contributors
// For license information, please see license.txt

// frappe.ui.form.on("testing1", {
// 	refresh(frm) {

// 	},
// });
// custom_doctype.js
frappe.ui.form.on('Custom Doctype', {
    refresh: function(frm) {
        console.log('Form refreshed');
        // Your code
    }
});
