from flask import Flask

from pages import (
    index,
    pages,
    about,
    auth,
    a1,
    a2,
    a3,
    a5,
    a6,
    a7,
    a9,
    pickle,
    faq,
    pricing,
    contact,
    insecure_log,
    sitemap
)

import models

### Initialize App
app = Flask(__name__)
app.url_map.strict_slashes = False
app.debug = True

### Register blueprints
app.register_blueprint(index.bp)
app.register_blueprint(about.bp, url_prefix="/about")
app.register_blueprint(a1.bp)
app.register_blueprint(a2.bp)
app.register_blueprint(a3.bp)
app.register_blueprint(a5.bp)
app.register_blueprint(a6.bp) # security misconf
app.register_blueprint(a7.bp) # xss
app.register_blueprint(a9.bp, url_prefix="/owasp")
app.register_blueprint(pages.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(pickle.bp)
app.register_blueprint(faq.bp)
app.register_blueprint(pricing.bp)
app.register_blueprint(contact.bp)
app.register_blueprint(insecure_log.bp)
app.register_blueprint(sitemap.bp)

### Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user.db"
models.db.init_app(app)
models.db.app = app
models.bootstrap()