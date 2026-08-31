from odoo import api, fields, models


class HsaAutoResponse(models.Model):
    _name = 'hsa.auto.response'
    _description = 'AI Auto-Response Template'
    _order = 'usage_count desc'

    name = fields.Char(string='Name', required=True)
    trigger_keyword = fields.Char(string='Trigger Keyword', required=True)
    category = fields.Char(string='Category')
    response_template = fields.Html(string='Response Template', required=True)
    ai_confidence = fields.Float(string='AI Confidence (%)', default=0.0)
    auto_send = fields.Boolean(string='Auto Send', default=False)
    active = fields.Boolean(string='Active', default=True)
    usage_count = fields.Integer(string='Usage Count', default=0)
    success_rate = fields.Float(string='Success Rate (%)', default=0.0)

    def action_increment_usage(self):
        for record in self:
            record.usage_count += 1
