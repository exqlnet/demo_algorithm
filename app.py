from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import time
from config import Default
from csv_to_excel import transform


import random

app = Flask(__name__)
app.config.from_object(Default)


def allowed_file(f):
    return True


@app.route('/csv_to_excel', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = app.config['UPLOAD_FOLDER']
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['file']  # 从表单的file字段获取文件，file为该表单的name值

    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname = secure_filename(f.filename)
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        # new_filename = str(unix_time)+'.'+ext  # 修改了上传的文件名
        new_filename = '{}{}.{}'.format(time.time(), random.random(), ext)  # 修改了上传的文件名
        f.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录
        new_filename = transform(new_filename)
        return send_file(os.path.join(file_dir, new_filename))

    else:
        return jsonify({"errno": 1001, "errmsg": "failed"})

@app.route('/download/<string:token>', methods=['GET'])
def download(token):



app.run()
