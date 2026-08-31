{
    'name': 'AI Helpdesk & Customer Support Automation',
    'version': '18.0.1.0.0',
    'summary': 'AI-powered helpdesk ticketing, auto-responses, SLA monitoring, '
               'knowledge base, and support analytics.',
    'description': """
AI Helpdesk & Customer Support Automation
=========================================
Comprehensive AI-driven customer support suite for Odoo:

* AI Helpdesk Tickets with sentiment analysis, category and priority prediction
* AI Auto-Response templates with confidence scoring and usage tracking
* SLA Monitoring with AI risk scoring and breach prediction
* Knowledge Base articles with AI relevance scoring
* Support Analytics dashboard with automation rate and escalation metrics
""",
    'author': 'SoftaiDev',
    'website': 'https://softaidev.pages.dev',
    'category': 'Productivity/AI',
    'license': 'LGPL-3',
    'price': 79.99,
    'currency': 'USD',
    'depends': ['base', 'web', 'mail'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/hsa_ticket_views.xml',
        'views/hsa_auto_response_views.xml',
        'views/hsa_sla_monitor_views.xml',
        'views/hsa_knowledge_article_views.xml',
        'views/hsa_support_analytics_views.xml',
        'views/menu.xml',
    ],
}
