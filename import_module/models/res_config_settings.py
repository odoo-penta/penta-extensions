from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    penta_skip_import_check_landed_cost = fields.Boolean(
        string="Permitir costos en destino sin Importación",
        config_parameter="penta.skip_import_check_landed_cost",
        help="Si está activo, permite crear Costos en destino desde factura aunque no tenga Importación asociada.",
        default = True,
    )

    penta_calculate_customs_taxes = fields.Boolean(
        string="Calcular impuestos de aduana",
        config_parameter="penta.calculate_customs_taxes",
        help="Si está activo, se habilita el cálculo de impuestos en Costos en destino.",
        default=False,
    )
