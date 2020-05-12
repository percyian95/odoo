# -*- coding: utf-8 -*-
# Copyright 2019, AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        if not self.env.user.has_group('sales_team.group_sale_manager') and self.env.user.has_group('sales_team.group_sale_salesman_all_leads'):
            args += [('x_studio_division', '=', self.env.user.x_studio_field_1CtHy)]
        return super(SaleOrder, self)._search(args, offset=offset, limit=limit, order=order,
                                            count=count, access_rights_uid=access_rights_uid)

  
