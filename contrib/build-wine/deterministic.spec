# -*- mode: python -*-

# We don't put these files in to actually include them in the script but to make the Analysis method scan them for imports
a = Analysis(['C:/electrum-nvc/electrum-nvc', 'C:/electrum-nvc/gui/qt/main_window.py', 'C:/electrum-nvc/gui/qt/lite_window.py', 'C:/electrum-nvc/gui/text.py',
              'C:/electrum-nvc/lib/util.py', 'C:/electrum-nvc/lib/wallet.py', 'C:/electrum-nvc/lib/simple_config.py',
              'C:/electrum-nvc/lib/bitcoin.py'
              ],
             hiddenimports=["lib","gui"],
             pathex=['lib:gui:plugins'],
             hookspath=None)

##### include mydir in distribution #######
def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        for d in glob.glob(p):
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    extra_datas = []
    for f in files:
        extra_datas.append((f, f, 'DATA'))

    return extra_datas
###########################################

# append dirs

# Theme data
a.datas += extra_datas('data')

# Localization
a.datas += extra_datas('locale')

# Py folders that are needed because of the magic import finding
a.datas += extra_datas('gui')
a.datas += extra_datas('lib')
a.datas += extra_datas('plugins')

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.datas,
          name=os.path.join('build\\pyi.win32\\electrum-nvc', 'electrum-nvc.exe'),
          debug=False,
          strip=None,
          upx=False,
          icon='C:/electrum-nvc/icons/electrum.ico',
          console=False)
          # The console True makes an annoying black box pop up, but it does make Electrum output command line commands, with this turned off no output will be given but commands can still be used

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               debug=False,
               icon='C:/electrum-nvc/icons/electrum.ico',
               console=False,
               name=os.path.join('dist', 'electrum-nvc'))
