# -*- mode: python -*-

block_cipher = None


a = Analysis(['Ui_MakupGUI.py'],
             pathex=['D:\\Python27\\Lib\\site-packages\\PyQt5', 'D:\\PycharmProjects\\AIMakeup-master'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Ui_MakupGUI',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='makeup.ico')
