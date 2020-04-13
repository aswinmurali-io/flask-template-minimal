# !/usr/bin/env python
# -*- mode: python ; coding: utf-8 -*-
# PyInstaller Build Script

import os
block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[os.getcwd()],
    binaries=[],
    datas=[
        ("templates" , "templates"),
    ],
    hiddenimports=[],
    hookspath=[],
    excludes=[
        '_asyncio',
        '_bz2',
        '_decimal',
        '_hashlib',
        '_lzma',
        '_multiprocessing',
        '_overlapped',
        '_queue',
        '_ssl',
        '_win32sysloader',
        'win32com',
        'win32trace',
        'win32ui',
        'win32wnet',
    ],
    runtime_hooks=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

# The binaries that pyinstaller bundle but not required
a.binaries -= TOC([
    ('libssl-1_1.dll', None, None),
    ('libcrypto-1_1.dll', None, None),
    # ('ucrtbase.dll', None, None)
])

pyz = PYZ(
    a.pure, a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Flask App',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='main'
)
