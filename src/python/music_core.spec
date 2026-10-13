# -*- mode: python ; coding: utf-8 -*-
import os
import sys
import site

block_cipher = None

# PyInstaller runs from Python 3.14 but dependencies (yt_dlp, requests, etc.)
# are installed in Python 3.12. Add all Python site-packages to sys.path.
import glob
python_base = r'C:\Users\ASUS\AppData\Local\Programs\Python'
for sp in glob.glob(os.path.join(python_base, 'Python*', 'Lib', 'site-packages')):
    if sp not in sys.path:
        sys.path.insert(0, sp)
# Also check user site-packages
user_base = os.path.join(os.environ.get('APPDATA', ''), 'Python')
for sp in glob.glob(os.path.join(user_base, 'Python*', 'site-packages')):
    if sp not in sys.path:
        sys.path.insert(0, sp)

# Manually locate yt_dlp package and collect it
yt_dlp_datas = []

try:
    import yt_dlp
    yt_dlp_pkg_dir = os.path.dirname(yt_dlp.__file__)
    yt_dlp_datas = [(yt_dlp_pkg_dir, 'yt_dlp')]
    print(f"Found yt_dlp at: {yt_dlp_pkg_dir}")
except ImportError:
    print("WARNING: yt_dlp not found! Install it with: pip install yt_dlp")

# Also locate requests package
requests_datas = []
try:
    import requests
    requests_datas = [(os.path.dirname(requests.__file__), 'requests')]
except ImportError:
    pass

# Locate certifi for SSL certificates (needed by requests)
certifi_datas = []
try:
    import certifi
    certifi_datas = [(os.path.dirname(certifi.__file__), 'certifi')]
except ImportError:
    pass

# Locate urllib3 (needed by requests)
urllib3_datas = []
try:
    import urllib3
    urllib3_datas = [(os.path.dirname(urllib3.__file__), 'urllib3')]
except ImportError:
    pass

# Locate charset_normalizer (needed by requests)
charset_datas = []
try:
    import charset_normalizer
    charset_datas = [(os.path.dirname(charset_normalizer.__file__), 'charset_normalizer')]
except ImportError:
    pass

all_datas = yt_dlp_datas + requests_datas + certifi_datas + urllib3_datas + charset_datas

a = Analysis(
    ['music_core.py'],
    pathex=[],
    binaries=[],
    datas=all_datas,
    hiddenimports=[
        'yt_dlp',
        'requests',
        'sqlite3',
        'io',
        'certifi',
        'urllib3',
        'charset_normalizer',
        'idna',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'PIL',
        'cv2',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6',
        'wx',
        'gtk',
        'unittest',
        'test',
        'tests',
        'pydoc',
        'doctest',
        'mysql',
        'mysql.connector',
        'psycopg2',
        'pymongo',
        'redis',
        'celery',
        'flask',
        'django',
        'tornado',
        'aiohttp',
        'cryptography',
        'multiprocessing',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)


pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='music_core',
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
)
