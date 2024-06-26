import frappe

@frappe.whitelist()
def get_user():
    try:
        # Return all data of Info Doctype
        return  frappe.get_all('User', fields=['*'])
    
    except Exception as e:
        raise frappe.error_log((500, f"Failed to retrieve information: {e}"))
    
@frappe.whitelist()
def create_user():
    try:
        # Get Data From Local
        data=frappe.local.form_dict

        # Set Given Infomation in Info 
        newUser=frappe.get_doc({
        'doctype':"User",
        **data
         })
        
        newUser.insert()
        frappe.db.commit()

        # Return Doc Name If Data SuccessFully Save
        return newUser.name
    
    except Exception as e:
        raise frappe.error_log((500, f"Failed to Save information: {e}"))