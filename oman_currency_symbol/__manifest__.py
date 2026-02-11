{
    'name': 'OMR Symbol Font | Oman Currency Symbol | Riyal Omani Icon',
    'version': '17.0.0.0.0',
    'category': 'Accounting',
    'summary': 'Add the new Omani Riyal (OMR) symbol to your Odoo system',
    'description': """
OMR Symbol Font for Odoo
رمز الريال العماني اودو Odoo
=======================
        Credits / Acknowledgment
        ------------------------
        - Idea: Al Hussain Al Dhahli
        - Implementation: Mohamed Elamin

        This module adds the new Omani Riyal (ر.ع.) symbol to your Odoo system interfaces, including:

        * PDF Reports
        * Point of Sale Interface
        * Invoices
        * All system views

        After installing this module, copy the symbol đ and paste it in the currency symbol field 
        for the Omani Riyal (OMR) currency in: Accounting > Configuration > Accounting > Currencies.

        Note: Please ensure there are no other font-family customizations in your system views and invoices 
        that might conflict with this module.
    """,
    'author': 'Mohamed elamin <moheha2@gmail.com>,Al hussain Al dhahli <a.aldhahli1@squ.edu.om> ',
    'website': 'https://www.linkedin.com/in/mohamed-elamin-00743/',    
    "summary": "OMR New Symbol",
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'OMR',
    'depends': ['base','web'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'oman_currency_symbol/static/src/css/style.css',
        ],
        'web.assets_frontend': [
            'oman_currency_symbol/static/src/css/style.css',
        ],
        'web.assets_common': [
            'oman_currency_symbol/static/src/css/style.css',
        ],
        'web.report_assets_common': [
            'oman_currency_symbol/static/src/css/style.css',
        ],
        'web.report_assets_pdf': [
            'oman_currency_symbol/static/src/css/style.css',
        ],
        'web.assets_qweb': [
            'oman_currency_symbol/static/src/css/style.css',
        ],
        "point_of_sale.assets": [
            'oman_currency_symbol/static/src/css/style.css',
        ],
        'web.qunit_suite_tests': [
            'oman_currency_symbol/static/src/css/style.css',
        ],
        'web.assets_tests': [
            'oman_currency_symbol/static/src/css/style.css',
        ],
        'account_reports.assets_financial_report': [
            'oman_currency_symbol/static/src/css/style.css',
        ],
        'account.assets_accounting_reports': [
            'oman_currency_symbol/static/src/css/style.css',
        ],
        'web.dark_mode_assets_backend': [
            'oman_currency_symbol/static/src/css/style.css',
        ],
    },
    'icon': '/oman_currency_symbol/static/description/icon.png',
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
