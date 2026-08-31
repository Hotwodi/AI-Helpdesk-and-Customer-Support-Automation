from odoo import api, fields, models


class HsaKnowledgeArticle(models.Model):
    _name = 'hsa.knowledge.article'
    _description = 'Knowledge Base Article'
    _order = 'view_count desc'

    name = fields.Char(string='Title', required=True)
    category = fields.Char(string='Category')
    content = fields.Html(string='Content', required=True)
    tags = fields.Char(string='Tags')
    ai_relevance_score = fields.Float(string='AI Relevance Score', default=0.0)
    view_count = fields.Integer(string='View Count', default=0)
    helpful_count = fields.Integer(string='Helpful Count', default=0)
    created_by = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user)
    last_updated = fields.Datetime(string='Last Updated', default=fields.Datetime.now)
    active = fields.Boolean(string='Active', default=True)

    def action_increment_view(self):
        for record in self:
            record.view_count += 1
            record.last_updated = fields.Datetime.now()

    def action_mark_helpful(self):
        for record in self:
            record.helpful_count += 1
