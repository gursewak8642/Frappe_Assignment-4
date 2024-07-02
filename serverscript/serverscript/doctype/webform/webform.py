# Copyright (c) 2024, Gursewak Singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class webform(Document):
	# pass
	def after_insert(self):
		self.notify_admin_on_creation()
	def notify_admin_on_creation(self):
		subject = f"New Task added: {self.description}"
		message = f"""
        A new task has been created in the system:
        Description: {self.description} 
        """
		print(frappe.sendmail(
            recipients="mrcodewick@gmail.com",
            subject= subject,
            message="message",
            delayed=False
        ))