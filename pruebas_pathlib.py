#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 19:49:28 2022

@author: albertomengual
"""
import os
import pathlib as pl

ruta= pl.PurePosixPath('/Users/albertomengual/Documents/local alderetes/facturas local/\
plantillaFactura - local alderetes.docx')

os.path.dirname('/Users/albertomengual/Documents/local alderetes/facturas local/\
plantillaFactura - local alderetes.docx')

ruta.parts
ruta.name


ruta2 = ruta.with_name('factura 2022 - 02 - local alderetes - feb22.pdf')
ruta2.name
ruta2.parts
ruta2.root
ruta2.anchor
ruta2.parent
ruta2.suffix
ruta2.with_suffix('.docx')


r3 = pl.PosixPath(ruta2)
r3.parts
r3.home()
r3.exists()
r3.is_dir()
r3.is_file()
with r3.open('rb') as fp:
    fp.readline()
r3.read_bytes()

r3
os.fspath(r3)
str(r3)
bytes(r3) #solo se recomienda en unix

r1, r2 = str(ruta), str(ruta2)
r1
r2
