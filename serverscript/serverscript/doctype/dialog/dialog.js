// Copyright (c) 2024, Gursewak Singh and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Dialog", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on('Dialog', {
    refresh: function(frm) {
        // Bind click event to the button field
        frm.fields_dict.input.$input.on('click', function() {
            open_task_input_dialog(frm);
        });
    }
});

function open_task_input_dialog(frm) {
    let d = new frappe.ui.Dialog({
        title: 'Enter Task Details',
        fields: [
            {
                label: 'Task Name',
                fieldname: 'task_name',
                fieldtype: 'Data'
            },
            {
                label: 'Task ID',
                fieldname: 'task_id',
                fieldtype: 'Data'
            },
            {
                label: 'Task Time',
                fieldname: 'task_time',
                fieldtype: 'Int'
            }
        ],
        primary_action_label: 'Add Task',
        primary_action(values) {
            add_task_to_child_table(values, frm);
            d.hide();
        }
    });

    d.show();
}

function add_task_to_child_table(values, frm) {
    let child = frm.add_child('link'); // Replace 'tasks' with your actual child table fieldname
    child.task_name = values.task_name;
    child.task_id = values.task_id;
    child.task_time = values.task_time;
    frm.refresh_field('link'); // Replace 'tasks' with your actual child table fieldname
    frappe.msgprint('Task Added Successfully');
}