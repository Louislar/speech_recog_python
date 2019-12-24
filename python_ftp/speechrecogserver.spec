# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['speechrecogserver.py'],
             pathex=['/home/wmlab/speech_recog_python/python_ftp'],
             binaries=[],
             datas=[('/home/wmlab/speech_recog_python/python_ftp/dist/pocketsphinx.so', '.'),
                    ('/home/wmlab/speech_recog_python/python_ftp/dist/sphinxbase.so', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='speechrecogserver',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
