import frappe
import frappe.utils

def my_function():
    import pdb; pdb.set_trace()
    # Your code here

def validate(doc, method):
    import pdb; pdb.set_trace()  # Add this line to start the debugger
    if doc.custom_customer_anniversary and doc.custom_customer_anniversary > frappe.utils.today():
        frappe.throw("Customer Anniversary cannot be a future date.")
