# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alquiler(models.Model):
    _name = 'alquiler.alquiler'

    locals = fields.One2many("alquiler.local", "local_number", string="Local a alquilar")
    rent = fields.Integer(string="Monto mensual de alquiler")
    rent_maintenance = fields.Integer(string="Monto mensual de mantenimiento")
    start_date = fields.Datetime(string="Fecha inicio")
    end_date = fields.Datetime(string="Fecha final")
    anual_raise_percentage = fields.Float(string="Porcentaje de aumento anual")
    renter = fields.Many2one('res.users', ondelete='set null', string="Usuario que alquila", index=True)
    invoices = fields.One2many('account.invoice', 'id', string="Facturas emitidas")

    # def facturar():
    #     your_class_records = self.browse(cr, uid, ids)
    #     for record in invoices:
    #         invoice_id = self.pool.get('account.invoice').create(cr, uid,{
    #             'name' : record.name,
    #             'date_invoice' : record.date,
    #         })
    #         for line in record.line:
    #             self.pool.get('account.invoice.line).create(cr, uid,{
    #                 'invoice_id' : invoice_id,
    #                 'name' : line.name,
    #                 'product_id' : line.product_id.id,
    #             })

class Local(models.Model):
    _name = 'alquiler.local'

    local_number = fields.Integer(string='Numero de local')
    area = fields.Float(string='Área en metros cuadrados')
    id_electric = fields.Integer(string='Id medidor de electricidad')
    id_water = fields.Integer(string='Id medidor de agua')
    id_building = fields.Many2one('alquiler.building', string="Edificio")
    id_floor = fields.Many2one('alquiler.floor',  string="Numero de piso")
    id_rent_doc = fields.Integer(string='Numero de docuemento')
    # se debe seleccionar primero el edificio y luego se deben mostrar los pisos relacionados al edificio donde esté el localself.


class Floor(models.Model):
    _name = 'alquiler.floor'

    name = fields.Char(string="Piso del edificio")
    floor_number = fields.Integer(string="Numero de piso")
    id_building = fields.Many2one('alquiler.building', string="Nombre de edificio")

class Building(models.Model):
    _name = 'alquiler.building'

    name = fields.Char(string="Nombre del edificio")
    address = fields.Text(string="Dirección del edificio")
    terrain_area = fields.Float(string="Área de terreno en metros cuadrados")
    construction_area = fields.Float(string="Área de construcción en metros cuadrados")
    floors = fields.One2many("alquiler.floor", "floor_number", string="Pisos")

class DocRent(models.Model):
    _name = 'alquiler.docrent'

    name = "Documento de Alquiler"
    contract_number = fields.Integer(string="Numero de contrato")
    # rented_locals = fields.Selection()
