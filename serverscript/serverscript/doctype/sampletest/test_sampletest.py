# Copyright (c) 2024, Gursewak Singh and Contributors
# See license.txt

# import frappe
# from frappe.tests.utils import FrappeTestCase
import frappe
from frappe.tests.utils import FrappeTestCase
class TestsampleTest(FrappeTestCase):
    def setUp(self):
        self.doc = frappe.get_doc({
            'doctype': 'sampleTest',
            'numer_1_daalo': 24,
            'numer_2_daalo': 12,
            'total': '36'
        })
        print("Start setUp")
        self.doc.insert()
        frappe.db.commit()
    def tearDown(self):
        if self.doc.name:
            print("Start tearDown")
            frappe.delete_doc('sampleTest', self.doc.name)
            frappe.db.commit()
    def test_field_values(self):
        print("Start test_field_values")
        doc2 = frappe.get_doc("sampleTest", self.doc.name)
        self.assertEqual(doc2.numer_1_daalo, 24)
        self.assertEqual(doc2.numer_2_daalo, 12)
        self.assertEqual(doc2.total_dekho, '36')
    def test_update(self):
        doc2 = frappe.get_doc("sampleTest", self.doc.name)
        doc2.update({
            'numer_1_daalo': 30
        })
        print("Start test_update")
        doc2.save()
        frappe.db.commit()
        updated_doc = frappe.get_doc("sampleTest", self.doc.name)
        self.assertEqual(updated_doc.numer_1_daalo, 30)







