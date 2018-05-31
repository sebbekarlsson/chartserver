from flask import Flask
from chartserver.views.chart import bp as chart_bp


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.register_blueprint(chart_bp)
