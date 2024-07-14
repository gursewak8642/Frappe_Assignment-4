frappe.ui.form.on('Item', {
    quantity: function(frm) {
      calculate_total_cost(frm);
    },
    unit_cost: function(frm) {
      calculate_total_cost(frm);
    }
  });
  
  function calculate_total_cost(frm) {
    if (frm.doc.quantity && frm.doc.unit_cost) {
      frm.set_value('total_cost', frm.doc.quantity * frm.doc.unit_cost);
    }
  }
  