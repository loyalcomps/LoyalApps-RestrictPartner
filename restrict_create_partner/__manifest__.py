# -*- coding: utf-8 -*-
#############################################################################
#
#    Loyal IT Solutions Pvt Ltd
#
#    Copyright (C) 2023-TODAY Loyal IT Solutions Pvt Ltd(<https://www.loyalitsolutions.com>).
#    Author: Loyal IT Solutions Pvt Ltd
#
#    You can modify it under the terms of the
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#

#   The coding is built and distributed among Odoo community in order to help
#    Odoo providers and users, but WITHOUT ANY WARRANTY.
#
#   For the copy of GNU PUBLIC LICENSE, please see
#   <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Restrict Create Customer / Vendor',
    'version': '16.0',
    'author': 'Loyal IT Solutions Pvt Ltd',
    'category': 'Uncategorized',
    'summary': 'Restrict creation of the Parnter | Restrict user to create customer | Restrict user to create Vendor',
    'description': """
        This module is for restricting customer/ vendor creation from unauthorized users. 
    """,
    'depends': ['base','contacts'],
    'website': 'www.loyalitsolutions.com.com',
    'license': 'LGPL-3',
    'support': "support@loyalitsolutions.com",
    'data': [
        'security/ir.model.access.csv',
        'views/restrict.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,

    'images': ['static/description/banner.png'],
}