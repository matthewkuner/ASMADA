# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main_4_2_21.py'],
             pathex=['C:\\Users\\Matthew Kuner\\Documents\\Python Scripts\\Splitting Python into multiple files'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[
                    'alabaster',
                    'babel',
                    'bcrypt',
                    'brotli',
                    'certifi',
                    'cryptography',
                    'etc',
                    'gevent',
                    'jedi',
                    'jsonschema',
                    'lib2to3',
                    'nacl',
                    'nbconvert',
                    'nbformat',
                    'notebook',
                    'numexpr',
                    'pytz',
                    'share',
                    'sphinx',
                    'sqlalchemy',
                    'tables',
                    'win32com',
                    'zmq',
                    'zope'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main_4_2_21',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='TAM-LogoBox.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main_4_2_21')
