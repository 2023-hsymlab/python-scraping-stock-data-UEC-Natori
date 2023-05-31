from flask import render_template  # 追加
from flask_testapp import app


@app.route('/')
def index():
    data = 'insertテスト中...'
    my_dict = {
        'insert_something1': 'views.pyのinsert_something1部分です。',
        'insert_something2': 'views.pyのinsert_something2部分です。',
    }
    return render_template('pages/index.html', insert_test=data, dict_test=my_dict)
