from odoo import api, fields, models


class LibraryBook(models.Model):
    """A book in the demo catalogue."""

    _name = "library.book"
    _description = "Book"
    _order = "name"

    name = fields.Char("Title", required=True)
    author = fields.Char()
    year = fields.Integer()
    available = fields.Boolean(default=True)
    page_count = fields.Integer("Pages")
    age = fields.Integer(compute="_compute_age")

    @api.depends("year")
    def _compute_age(self):
        """Years since the book came out."""
        this_year = fields.Date.today().year
        for book in self:
            book.age = this_year - book.year
