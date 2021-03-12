from distutils.core import setup, Extension

minu_scrypt_module = Extension('minu_scrypt',
                               sources = ['scryptmodule.c',
                                          'scrypt.c'],
                               include_dirs=['.'])

setup (name = 'minu_scrypt',
       version = '1.0',
       description = 'Bindings for scrypt proof of work used by minidoge',
       ext_modules = [minu_scrypt_module])
