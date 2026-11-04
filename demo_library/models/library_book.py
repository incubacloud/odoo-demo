from odoo import fields, models


class LibraryBook(models.Model):
    """A book in the demo catalogue."""

    _name = "library.book"
    _description = "Book"
    _order = "name"

    name = fields.Char("Title", required=True)
    author = fields.Char()
    year = fields.Integer()
    available = fields.Boolean(default=True)
