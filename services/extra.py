#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource
import logging
import subprocess


class Decode(Resource):

    def get(self, extraData):
        if not extraData:
            return {}, 400

        extraData = extraData.strip()
        args = ['/root/go/bin/istanbul', 'extra', 'decode', '--extradata', extraData]
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        output = popen.stdout.read().decode('utf-8')
        output_array = output.split('\n')

        if not output_array[0]:
            return {}, 400

        result_dict = {}
        for line in output_array:
            kv = line.split(':')
            if kv[0]:
                if kv[0] == 'validator':
                    if not 'validators' in result_dict:
                        result_dict['validators'] = []
                    result_dict['validators'].append(kv[1].strip())
                elif kv[0] == 'committed seal':
                    if not 'committed_seals' in result_dict:
                        result_dict['committed_seals'] = []
                    result_dict['committed_seals'].append(kv[1].strip())
                else:
                    result_dict[kv[0].strip()] = kv[1].strip()
        return result_dict, 200
