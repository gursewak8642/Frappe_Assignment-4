import frappe

@frappe.whitelist()
def get_info():
    try:
        # Return all data of Info Doctype
        return  frappe.get_all('Information', fields=['*'])
    
    except Exception as e:
        raise frappe.error_log((500, f"Failed to retrieve information: {e}"))

@frappe.whitelist()
def create_info():
    try:
        # Get Data From Local
        data=frappe.local.form_dict

        # Set Given Infomation in Info 
        newInfo=frappe.get_doc({
        'doctype':"Information",
        **data
         })
        
        newInfo.insert()
        frappe.db.commit()

        # Return Doc Name If Data SuccessFully Save
        return newInfo.name
    
    except Exception as e:
        raise frappe.error_log((500, f"Failed to Save information: {e}"))

@frappe.whitelist()
def update_info():
    try:
        data=frappe.local.form_dict
        # iF Doc Name available then data will be updated
        if(data.name):    
            doc=frappe.get_doc('Information',data.name)
            doc.update(data)
            doc.save()
            frappe.db.commit()
            return doc
        else:
             raise frappe.error_log((404, f"Name Not Found"))

    except Exception as e:
        raise frappe.error_log((500, f"Failed to Update information: {e}"))

@frappe.whitelist()
def delete_info():
    data=frappe.local.form_dict
    try:
         # iF Doc Name available then data will be deleted
        if(data.name):    
            frappe.delete_doc('Information',data.name)
            frappe.db.commit()
            return f"deleted"
        else:
            raise frappe.error_log((404, f"Name Not Found:"))
    except Exception as e:
        raise frappe.error_log((500, f"Failed to Delete information: {e}"))