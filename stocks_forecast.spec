# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Define application name
app_name = "stocks_forecast"

# Ensure missing dependencies are included
hidden_imports = collect_submodules("yfinance") + collect_submodules("pandas") + collect_submodules("sklearn")

a = Analysis(
    ["stocks_forecast.py"],
    pathex=["."],
    binaries=[],
    datas=collect_data_files("yfinance") + collect_data_files("matplotlib"),
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=app_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to True if you want to see logs in a console window
    icon="stocks.ico",  # Ensure this icon file exists in the same directory
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name=app_name,
)
