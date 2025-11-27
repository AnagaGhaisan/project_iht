from odoo import models, fields

class ProjectProject(models.Model):
    _inherit = "project.project"

    lokasi_proyek = fields.Text(string="Lokasi Proyek")
    source_aplikasi_pendukung = fields.Char(
        string="Source Aplikasi Pendukung",
        help=""
    )
    daftar_perkerja_remote = fields.Json(
        string="Daftar Pekerja Remote",
        help="List pekerja remote dalam format JSON."
    )
    tanggal_mulai_proyek = fields.Date(string="Tanggal Mulai Proyek")
    tanggal_selesai_proyek = fields.Date(string="Tanggal Selesai Proyek")
    anggaran_proyek = fields.Float(string="Anggaran Proyek")
    manajer_proyek = fields.Many2one(
        comodel_name="res.users",
        string="Manajer Proyek",
        help="Pengguna yang bertanggung jawab atas proyek ini."
    )
    status_proyek = fields.Selection(
        selection=[
            ('perencanaan', 'Perencanaan'),
            ('pelaksanaan', 'Pelaksanaan'), 
            ('penyelesaian', 'Penyelesaian'), 
            ('ditutup', 'Ditutup')
        ],
        string="Status Proyek",
        default='perencanaan',
        help="Status terkini dari proyek."
    )