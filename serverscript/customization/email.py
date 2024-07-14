import frappe
@frappe.whitelist()
def send_approval_notification(doc, method):
    if doc.workflow_state == "Approved":
        recipient_email = "mrcodewick@gmail.com"
        subject = f"Sales Order {doc.name} Approved"
        message = f"""
        <p>Ram Ram Bhai Sareiyan n </p>
        <p>The sales order {doc.name} has been approved.</p>
        <p>Order Details:</p>
        <p><strong>Sales Order:</strong> {doc.name}</p>
        <p><strong>Date:</strong> {doc.transaction_date}</p>
        <p><strong>Total Amount:</strong> {doc.grand_total}</p>
        <p>Please review the sales order and confirm.</p>
        <p>Thank you,</p>
        <p>NestorBird</p>
        """
        frappe.sendmail(recipients=recipient_email, subject=subject, message=message, delayed= False)