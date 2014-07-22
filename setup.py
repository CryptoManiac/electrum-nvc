#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('version', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

usr_share = '/usr/share'
if not os.access(usr_share, os.W_OK):
    usr_share = os.getenv("XDG_DATA_HOME", os.path.join(os.getenv("HOME"), ".local", "share"))

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-nvc.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))

appdata_dir = util.appdata_dir()
if not os.access(appdata_dir, os.W_OK):
    appdata_dir = os.path.join(usr_share, "electrum-nvc")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]


setup(
    name="Electrum-NVC",
    version=version.ELECTRUM_VERSION,
    install_requires=['slowaes', 'ecdsa>=0.9', 'pbkdf2', 'requests', 'pyasn1', 'pyasn1-modules', 'tlslite>=0.4.5', 'qrcode', 'ltc_scrypt'],
    package_dir={
        'electrum_nvc': 'lib',
        'electrum_nvc_gui': 'gui',
        'electrum_nvc_plugins': 'plugins',
    },
    scripts=['electrum-nvc'],
    data_files=data_files,
    py_modules=[
        'electrum_nvc.account',
        'electrum_nvc.bitcoin',
        'electrum_nvc.blockchain',
        'electrum_nvc.bmp',
        'electrum_nvc.commands',
        'electrum_nvc.daemon',
        'electrum_nvc.i18n',
        'electrum_nvc.interface',
        'electrum_nvc.mnemonic',
        'electrum_nvc.msqr',
        'electrum_nvc.network',
        'electrum_nvc.paymentrequest',
        'electrum_nvc.paymentrequest_pb2',
        'electrum_nvc.plugins',
        'electrum_nvc.scrypt',
        'electrum_nvc.simple_config',
        'electrum_nvc.socks',
        'electrum_nvc.synchronizer',
        'electrum_nvc.transaction',
        'electrum_nvc.util',
        'electrum_nvc.verifier',
        'electrum_nvc.version',
        'electrum_nvc.wallet',
#        'electrum_nvc.wallet_bitkey',
        'electrum_nvc.x509',
        'electrum_nvc_gui.gtk',
        'electrum_nvc_gui.qt.__init__',
        'electrum_nvc_gui.qt.amountedit',
        'electrum_nvc_gui.qt.console',
        'electrum_nvc_gui.qt.history_widget',
        'electrum_nvc_gui.qt.icons_rc',
        'electrum_nvc_gui.qt.installwizard',
        'electrum_nvc_gui.qt.lite_window',
        'electrum_nvc_gui.qt.main_window',
        'electrum_nvc_gui.qt.network_dialog',
        'electrum_nvc_gui.qt.password_dialog',
        'electrum_nvc_gui.qt.paytoedit',
        'electrum_nvc_gui.qt.qrcodewidget',
        'electrum_nvc_gui.qt.qrtextedit',
        'electrum_nvc_gui.qt.receiving_widget',
        'electrum_nvc_gui.qt.seed_dialog',
        'electrum_nvc_gui.qt.transaction_dialog',
        'electrum_nvc_gui.qt.util',
        'electrum_nvc_gui.qt.version_getter',
        'electrum_nvc_gui.stdio',
        'electrum_nvc_gui.text',
        'electrum_nvc_plugins.qrscanner',
        'electrum_nvc_plugins.virtualkeyboard',
    ],
    description="Lightweight Novacoin Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU GPLv3",
    url="https://electrum.org",
    long_description="""Lightweight Novacoin Wallet"""
)
