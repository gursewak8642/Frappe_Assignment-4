# purchase_order.py
import frappe
def send_notification_email(doc, method):
    supplier_email = "mrcodewick@gmail.com"
    if supplier_email:
        subject = f"Purchase Order {doc.name} Submitted"
        message = f"""
        <p>Dear {doc.supplier_name},</p>
        <p>Apka Data {doc.name} has been submitted.</p>
        <p>Order Details:</p>
        <p><strong>Purchase Order:</strong> {doc.name}</p>
        <p><strong>Date:</strong> {doc.transaction_date}</p>
        <p><strong>Total Amount:</strong> {doc.grand_total}</p>
        <p>Please review the purchase order and confirm.</p>
        <p>Thank you,</p>
        <p>Mr Codewick</p>
        """
        frappe.sendmail(recipients=supplier_email, subject=subject, message=message, delayed=False)