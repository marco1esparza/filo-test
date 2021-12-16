# Copyright 2019, Jarsa Sistemas, S.A. de C.V.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Filo Instance',
    'summary': 'Module that install Filo Instance',
    'version': '14.0.1.0.2',
    'category': 'Instance',
    'author': 'Jarsa Sistemas',
    'website': 'https://www.jarsa.com.mx',
    'license': 'LGPL-3',
    'depends': [
        'purchase',
        'sale_management',
    ],
    "data": [
        'views/sale_advance_payment_inv_views.xml',
        'views/sale_order_views.xml',
        'views/stock_product_temple.xml',
    ],
}
