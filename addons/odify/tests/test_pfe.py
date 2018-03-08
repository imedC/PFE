# -*- coding: utf-8 -*-
import unittest
from odoo.tests.common import TransactionCase

class TestModelA(TransactionCase):

    def test_method(self):
        test2 = self.env['product.template'].search_read([], ['name'])
        #product_id = product.name
        #records = self.env['get.book'].search([('book_id.pages','=',100)]).mapped('name')
        #records = self.env['get.book'].search([('book_id','=','odoodjangoconnector (False)')])
        #for r in records:

        print('_______________________________', test2)
