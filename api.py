#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from services import extra
from conf import conf_loader as conf


if __name__ == "__main__":
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    api.add_resource(extra.Decode,
                     conf.api['base_url'] + '/extra/decode/<extraData>')

    app.run(host=conf.api['bind_address'],
            port=conf.api['port'])
