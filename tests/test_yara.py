#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import os
import logging
from yara_finder.matcher import YaraClass

__author__ = "uppusaikiran"
__copyright__ = "uppusaikiran"
__license__ = "mit"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler

handler = logging.FileHandler('yara.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)


def test_yara():
    full_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'test.pdf')
    ys = YaraClass('rules/','.',True,full_path)
    ys.compile()
    result = ys.scan_single(full_path)
    result = [ str(x) for x in result]
    print result
    logger.info('result from yara {}'.format(result))
    assert result[0]=='domain'
