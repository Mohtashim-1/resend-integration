# Copyright (c) 2024, mohtashim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.password import get_decrypted_password
import resend


def get_resend_api_key():
	return get_decrypted_password("Resend Settings","Resend Settings", "api_key")


resend.api_key = get_resend_api_key()


class ResendEmailRecord(Document):
	@frappe.whitelist()
	def send(self):
		email = resend.Emails.send({
			'from':self.from_email,
			'to':self.to_email.strip().split(','),
			'subject':self.subject,
			'html':self.email_html

		})
		self.status = 'Sent'
		self.response_id = email['id']
		self.save()
	# resend.Emails.send({
	# 	"from":self.from_email,
	# 	"to": self.to_email

	# })