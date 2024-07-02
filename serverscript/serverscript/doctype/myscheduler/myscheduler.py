import frappe
from frappe.model.document import Document

class myScheduler(Document):
	pass
	

@frappe.whitelist()
def update_counter():
		schedules = frappe.get_all('myScheduler', filters={})
              
		for schedule in schedules:
			doc = frappe.get_doc('myScheduler', schedule.name)
			doc.count = doc.count + 1
			doc.save()
			frappe.db.commit()
			print("Counter updated for all myscheduler documents")
			return doc.count