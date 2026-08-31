from odoo import api, fields, models


class HsaSlaMonitor(models.Model):
    _name = 'hsa.sla.monitor'
    _description = 'SLA Monitor'
    _order = 'ai_risk_score desc'

    name = fields.Char(string='Name', required=True)
    ticket_id = fields.Many2one('hsa.ticket', string='Ticket', required=True, ondelete='cascade')
    sla_type = fields.Selection([
        ('first_response', 'First Response'),
        ('resolution', 'Resolution'),
    ], string='SLA Type', required=True, default='first_response')
    target_hours = fields.Float(string='Target Hours', required=True, default=24.0)
    actual_hours = fields.Float(string='Actual Hours', default=0.0)
    breach = fields.Boolean(string='Breach', default=False)
    ai_risk_score = fields.Float(string='AI Risk Score', default=0.0)
    state = fields.Selection([
        ('on_track', 'On Track'),
        ('at_risk', 'At Risk'),
        ('breached', 'Breached'),
    ], string='State', default='on_track')

    @api.onchange('actual_hours', 'target_hours')
    def _onchange_hours(self):
        for record in self:
            if record.target_hours and record.actual_hours:
                if record.actual_hours > record.target_hours:
                    record.state = 'breached'
                    record.breach = True
                elif record.actual_hours >= record.target_hours * 0.8:
                    record.state = 'at_risk'
                    record.breach = False
                else:
                    record.state = 'on_track'
                    record.breach = False
