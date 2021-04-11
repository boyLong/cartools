# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['C:\\Users\\13106\\Desktop\\workspace\\w\\server'],
             binaries=[],
            datas=[(r'C:\Users\13106\Desktop\workspace\w\server\server\static',r'.\server\static'),
                   (r'C:\Users\13106\Desktop\workspace\w\server\server\templates', r'.\server\templates'),
                   (r'C:\Users\13106\Desktop\workspace\w\server\server_static\static_root',r'.\server_static\static_root'),
                   (r'C:\Users\13106\Desktop\workspace\w\server\excel',r'.\excel'),
                    (r'C:\Users\13106\Desktop\workspace\w\server\all_input',r'.\all_input'),
                   ],

             hiddenimports=['django.contrib.admin.apps','django.contrib.auth.apps','django.contrib.contenttypes.apps',
'django.contrib.sessions.apps', 'django.contrib.messages.apps', 'django.contrib.staticfiles.apps',],
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
          [],
          exclude_binaries=True,
          name='run',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\13106\\Desktop\\workspace\\w\\server\\car.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='run')
