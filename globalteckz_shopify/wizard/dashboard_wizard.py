###############################################################################
#                                                                             #
#    Globalteckz                                                              #
#    Copyright (C) 2013-Today Globalteckz (http://www.globalteckz.com)        #
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU Affero General Public License as           #
#    published by the Free Software Foundation, either version 3 of the       #
#    License, or (at your option) any later version.                          #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU Affero General Public License for more details.                      #
#                                                                             #
#    You should have received a copy of the GNU Affero General Public License #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                             #
###############################################################################



from odoo import api, fields, models


class ShopifyWizard(models.Model):
    _name = "shopify.wizard"
    
    
    gt_shopify_instance_ids = fields.Many2one('gt.shopify.instance',string='Select Instance')
    
    
    import_products = fields.Boolean('Import Products')
    import_inventory = fields.Boolean('Import Inventory')
    import_images = fields.Boolean('Import Images')
    import_orders = fields.Boolean('Import Orders')
    import_customer = fields.Boolean('Import Customer')
    
    update_shipment=fields.Boolean("Update Shipment")
    update_product=fields.Boolean('Update Product')
    update_stock=fields.Boolean('Update Stock')
    
    export_products = fields.Boolean('Export Products')
    export_images = fields.Boolean('Export Images')
    
    
    @api.model
    def default_get(self, fields):
        shop_obj = self.env['gt.shopify.instance']
        print "context...............",self._context
        rec = super(ShopifyWizard, self).default_get(fields)
        if self._context.get('active_model') == 'gt.shopify.instance':
            shop_ids = shop_obj.browse(self._context.get('active_ids')[0])
            if shop_ids:
                print "SHOPIFY INSTANCE ID",shop_ids.id
                rec.update({
                    'gt_shopify_instance_ids':shop_ids.id
                    })
        return rec    
  
    @api.one
    def import_shopify_data(self):
        instance_ids=self.gt_shopify_instance_ids
        if self.import_products == True:
            print 'IMPORT SHOPIFY PRODUCTS'
            instance_ids.gt_import_shopify_products()
        if self.import_inventory == True:
            print 'IMPORT SHOPIFY PRODUCT INVENTORY'
            instance_ids.gt_import_shopify_stock()
        if self.import_images == True:
            print 'IMPORT SHOPIFY PRODUCT IMAGES'
            instance_ids.gt_import_shopify_image()
        if self.import_customer == True:
            print 'IMPORT SHOPIFY CUSTOMERS'
            instance_ids.gt_import_shopify_customers()
        if self.import_orders == True:
            print 'IMPORT SHOPIFY ORDERS'
            instance_ids.gt_import_shopify_orders()
        if self.export_products == True:
            print 'EXPORT SHOPIFY PRODUCTS'
            instance_ids.gt_export_shopify_products()
        if self.export_images == True:
            print 'EXPORT SHOPIFY PRODUCT IMAGES'
            instance_ids.gt_export_shopify_image()
        if self.update_shipment == True:
            print "UPDATE SHOPIFY ORDER SHIPMENT"
            instance_ids.gt_export_shipment()
        if self.update_stock == True:
            print "UPDATE SHOPIFY PRODUCT INVENTORY"
            instance_ids.gt_export_shopify_stock()  
        return True
    
    