# build.spec
import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_all

# Путь к вашему скрипту
script_path = Path('TextCombiner.py').resolve()

# Конфигурация сборки
a = Analysis(
    [str(script_path)],
    pathex=[str(script_path.parent)],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

# Генерация .exe файла
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='myapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               *[collect_all(pkg) for pkg in a.binaries],
               upx=True,
               upx_exclude=[],
               name='dist')
