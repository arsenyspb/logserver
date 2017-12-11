#!/usr/bin/env python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'logserver.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(100))
    filename = db.Column(db.String(200))
    filecontent = db.Column(db.LargeBinary())

    def __init__(self, hostname, filename, filecontent):
        self.hostname = hostname
        self.filename = filename
        self.filecontent = filecontent


class LogSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('hostname', 'filename', 'filecontent')

log_schema = LogSchema()
logs_schema = LogSchema(many=True)

@app.route("/save", methods=["POST"])
def save_blob():
    hostname = request.json['hostname']
    filename = request.json['filename']
    filecontent = request.json['filecontent']

    new_blob = Log(hostname, filename, filecontent)

    db.session.add(new_blob)
    db.session.commit()

    return jsonify(new_blob)

@app.route("/query/<hostname>", methods=["GET"])
def filename_by_hostname(hostname):
    filename = Log.query.filter_by(hostname=hostname)
    filenames_on_host = logs_schema.dump(filename)
    return jsonify(filenames_on_host.data)

if __name__ == '__main__':
    app.run(debug=True)
