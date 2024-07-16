// frappe.ui.form.on('Item Child', {
//   quantity: function(frm, cdt, cdn) {
//       console.log("========")
//       let row = locals[cdt][cdn];
//       calculate_total_cost(row);
//       frm.refresh_field('custom_item_child_');
//   },
//   unit_cost: function(frm, cdt, cdn) {
//       let row = locals[cdt][cdn];
//       calculate_total_cost(row);
//       frm.refresh_field('custom_item_child_');
//   }
// });

// function calculate_total_cost(row) {
//   row.total_cost = row.quantity * row.unit_cost;
//   frappe.model.set_value(row.doctype, row.name, 'total_cost', row.total_cost);
// }
