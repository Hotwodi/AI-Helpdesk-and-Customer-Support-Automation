from odoo import api, fields, models


class HsaTicket(models.Model):
    _name = 'hsa.ticket'
    _description = 'AI Helpdesk Ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'created_date desc, priority desc'

    name = fields.Char(string='Ticket Reference', required=True, copy=False,
                       readonly=True, default=lambda self: self._get_default_name())
    partner_id = fields.Many2one('res.partner', string='Customer', tracking=True)
    subject = fields.Char(string='Subject', required=True, tracking=True)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ], string='Priority', default='medium', tracking=True)
    category = fields.Char(string='Category')
    ai_sentiment = fields.Selection([
        ('positive', 'Positive'),
        ('neutral', 'Neutral'),
        ('negative', 'Negative'),
        ('frustrated', 'Frustrated'),
    ], string='AI Sentiment', default='neutral')
    ai_category_prediction = fields.Char(string='AI Category Prediction')
    ai_priority_prediction = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ], string='AI Priority Prediction')
    state = fields.Selection([
        ('new', 'New'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ], string='State', default='new', tracking=True)
    assigned_to = fields.Many2one('res.users', string='Assigned To', tracking=True)
    created_date = fields.Datetime(string='Created Date', default=fields.Datetime.now, readonly=True)
    resolved_date = fields.Datetime(string='Resolved Date', readonly=True)
    response_time_hours = fields.Float(string='Response Time (Hours)', compute='_compute_response_time_hours',
                                       store=True)
    description = fields.Html(string='Description')

    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].next_by_code('hsa.ticket') or 'New'

    @api.depends('created_date', 'resolved_date')
    def _compute_response_time_hours(self):
        for ticket in self:
            if ticket.created_date and ticket.resolved_date:
                delta = ticket.resolved_date - ticket.created_date
                ticket.response_time_hours = delta.total_seconds() / 3600.0
            else:
                ticket.response_time_hours = 0.0

    def action_assign(self):
        for ticket in self:
            ticket.state = 'assigned'
            if not ticket.assigned_to:
                ticket.assigned_to = self.env.user

    def action_start_progress(self):
        for ticket in self:
            ticket.state = 'in_progress'

    def action_resolve(self):
        for ticket in self:
            ticket.state = 'resolved'
            ticket.resolved_date = fields.Datetime.now()

    def action_close(self):
        for ticket in self:
            ticket.state = 'closed'

    def action_reset_to_new(self):
        for ticket in self:
            ticket.state = 'new'
            ticket.resolved_date = False

    @api.model
    def create(self, vals):
        ticket = super().create(vals)
        return ticket
