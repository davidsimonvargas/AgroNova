import reflex as rx
from reflex_base.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="src",
    app_module_import="src.main",
    db_url="sqlite:///db/agronova.db",
    disable_plugins=[SitemapPlugin],
)
