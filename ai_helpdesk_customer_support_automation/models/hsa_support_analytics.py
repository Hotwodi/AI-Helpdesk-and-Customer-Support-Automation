from odoo import api, fields, models


class HsaSupportAnalytics(models.Model):
    _name = 'hsa.support.analytics'
    _description = 'Support Analytics'
    _order = 'period desc'

    name = fields.Char(string='Name', required=True)
    period = fields.Char(string='Period', required=True)
    total_tickets = fields.Integer(string='Total Tickets', default=0)
    avg_response_time = fields.Float(string='Avg Response Time (Hours)', default=0.0)
    avg_resolution_time = fields.Float(string='Avg Resolution Time (Hours)', default=0.0)
    satisfaction_score = fields.Float(string='Satisfaction Score (%)', default=0.0)
    ai_automation_rate = fields.Float(string='AI Automation Rate (%)', default=0.0)
    top_category = fields.Char(string='Top Category')
    escalation_rate = fields.Float(string='Escalation Rate (%)', default=0.0)
