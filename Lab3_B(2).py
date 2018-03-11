#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib

hashlib.sha256('what you want encrypted here'.encode()).hexdigest()
