#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
        hello_world = yara_finder.module:function

Then run `python setup.py install` which will install the command `hello_world`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""
from __future__ import division, print_function, absolute_import
import os
from flask import Flask,render_template, jsonify , request,redirect,url_for
from werkzeug.utils import secure_filename
from yara_finder.matcher import YaraClass

app = Flask(__name__)
ys = YaraClass(os.path.join(os.path.dirname(os.path.realpath(__file__)),'rules'),'.', True ,'.')
ys.compile()

@app.route('/yara', methods =['POST'])
def sendYara():
        file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'yara_finder/uploads')
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save( os.path.join(file_path, filename ))
            # Send the file to Yara Detector
            full_path = os.path.join(file_path,filename)
            print(full_path)
            result = ys.scan_single(full_path)
            data = {}
            data['status'] = 'success'
            data['match'] = [ str(x) for x in result]
            return jsonify(data)
        else:
            return '{"status" : "failed"}'
if __name__ == "__main__":
    app.run( host='0.0.0.0' , port=7777 , debug=False )
