# -*- coding: utf-8 -*-
{
    'name': "Projektas1",

    'summary': """Projektas1  summary""",

    'description': """
        First Odoo module
    """,

    'author': "Olga",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/work_view.xml',
        'views/bill_view.xml',
        'views/parner_inherited_view.xml',
        'views/employee_inherited_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}