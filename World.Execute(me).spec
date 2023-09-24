# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['World_Execute_me.py'],
    pathex=[],
    binaries=[],
    datas=[('worldexecuteme.wav', '.')],
    hiddenimports=['.\\AlipThreading.py', '.\\objects.py', '.\\worldExecuteMe.py', 'time', 'objects', 'AlipThreading', 'pyaudio', 'threading', 'wave', 'sys', 'itertools', 'os', 'pywhatkit', 'random', 'pytz', 'json', 'math', 'numpy', 'datetime', 'trace', 'threading'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='World.Execute(me)',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['ico.png'],
)
