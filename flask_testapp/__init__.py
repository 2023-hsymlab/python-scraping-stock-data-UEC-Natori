from flask import Flask

app = Flask(__name__)
app.config.from_object('flask_testapp.config') # 追加

import flask_testapp.views