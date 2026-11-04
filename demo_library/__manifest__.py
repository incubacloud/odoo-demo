{
    "name": "Demo Library",
    "summary": "A small book catalogue used to demo push-to-deploy",
    "version": "19.0.1.0.0",
    "category": "Tools",
    "author": "IncubaCloud",
    "website": "https://github.com/incubacloud/odoo-demo",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/library_book_views.xml",
    ],
    "application": True,
    "installable": True,
}
