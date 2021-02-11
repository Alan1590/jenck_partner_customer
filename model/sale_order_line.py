# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import xlwt
from openerp.osv import fields, osv
import datetime
from openerp.osv import orm
import os
import logging
_logger = logging.getLogger(__name__)

class sale_order_line(osv.osv):

	_inherit = 'sale.order.line'

	def _lines_to_updates(self, cr, uid, ids, context=None):
		order_line_obj = self.pool['sale.order.line']
		line_ids = order_line_obj.search(cr, uid, [('partner_id', 'in', ids)], context=context)
		return line_ids

	_columns = {
	'jenck_partner_rubro':fields.related('partner_id','sector_category_id',              
		readonly=False, type='many2one',relation='res.sector.category', string='Rubro',
		store={'res.partner':(_lines_to_updates,['sector_category_id'],10)}),
	}

