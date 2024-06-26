# Copyright (c) 2024, Gursewak Singh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Information(Document):
	def validate(self):
		if self.check and self.first_name and self.last_name:
			self.full_name = f"{self.first_name or ''} {self.last_name or ''}"



