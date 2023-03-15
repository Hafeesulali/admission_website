import base64

from odoo import http
from odoo.http import request


class WebsiteForm(http.Controller):
    @http.route(['/admission'], type='http', auth="user", website=True)
    def admission(self):
        course = request.env['college.courses'].sudo().search([])
        academic_year = request.env['college.academic'].sudo().search([])
        values = {}
        values.update({
            'courses': course,
            'academic_years': academic_year
        })
        return request.render("admission_website.online_admission_form", values)

    @http.route(['/admission/submit'], type='http', auth='user', website=True)
    def admission_submit(self, **post):
        admission = request.env["college.admission"].create({
            'first_name': post.get("first name"),
            'last_name': post.get("last name"),
            'email': post.get("email"),
            'phone': post.get("phone"),
            'course_id': post.get("course_id"),
            'academic_year_id': post.get("academic_year"),
            'communication_address': post.get("communication address"),
            'permanent_address': post.get("permanent address"),
            'same_as_communication': post.get("same as communication"),
            "previous_educational_qualification": post.get("previous_educational_qualification"),
            "father": post.get("fathers_name"),
            "mother": post.get("mothers_name"),
            "date_of_application": post.get("date of application"),
            "education_institute": post.get("educational institute")

        })
        transfer_certificate_name = post.get("transfer certificate").filename
        transfer_certificate_file = post.get("transfer certificate")
        request.env['ir.attachment'].sudo().create({
            'name': transfer_certificate_name,
            "type": "binary",
            'datas': base64.b64encode(transfer_certificate_file.read()),
            'res_model': 'college.admission',
            'res_id': admission.id,
            'res_field': 'transfer_certificate'
        })
        vals = {
            'student': admission
        }
        return request.render("admission_website.admission_success", vals)
