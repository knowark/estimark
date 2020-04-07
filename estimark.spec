# -*- mode: python -*-
import pkgutil
import pathlib

schema_path = pathlib.Path(
    pkgutil.get_loader('altair.vegalite.v4.schema').get_filename()).parent
vegalite_schema = str(schema_path) + "/vega-lite-schema.json"


block_cipher = None


a = Analysis(['estimark/__main__.py'],
             pathex=['/home/eecheverry/Workspace/dev/github.com/knowark/estimark'],
             binaries=[],
             datas=[(vegalite_schema, 'altair/vegalite/v4/schema')],
             hiddenimports=['pkg_resources.py2_warn'],
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
          name='estimark',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
