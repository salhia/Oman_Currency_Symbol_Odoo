{
    'name': 'OMR Symbol Font | Oman Currency Symbol | Riyal Omani Icon',
    "version": "18.0.1.0.0",
     'description': """
        OMR Symbol Font for Odoo
        رمز الريال العماني اودو Odoo
        =======================

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
    'author': 'Mohamed elamin',
    'website': 'https://www.linkedin.com/in/mohamed-elamin-00743/',   
    "summary": "OMR New Symbol",
    "license": "OPL-1",
    "category": "Tools",
    "depends": [
        "base",
        "web",
    ],
    "data": [
        "data/res_currency_data.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "oman_currency_symbol/static/src/css/style.css",
        ],
        "web.assets_frontend": [
            "oman_currency_symbol/static/src/css/style.css",
        ],
        "web.assets_common": [
            "oman_currency_symbol/static/src/css/style.css",
        ],
        "web.report_assets_common": [
            "oman_currency_symbol/static/src/css/style.css",
        ],
        "web.report_assets_pdf": [
            "oman_currency_symbol/static/src/css/style.css",
        ],
        "web.assets_qweb": [
            "oman_currency_symbol/static/src/css/style.css",
        ],
        "point_of_sale._assets_pos": [
            "oman_currency_symbol/static/src/css/style.css",
        ],
    },
    "images": ["static/description/banner.gif"],
    "auto_install": False,
    "application": False,
}
