#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import tarfile


tar = tarfile.open("/tmp/teste/sample.tar.xz", "w:xz")
tar.add("/home/rmelo/Downloads/TREINAMENTO/DataScience/", arcname='.')
tar.close()
