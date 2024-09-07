"""from py2exe import freeze

freeze(

  console=['py2exe_code.py']

)"""


from py2exe import freeze

freeze(

  console = [{'script':'py2exe_code.py'}],

  options = {'py2exe': {'bundle_files': 1, 'compressed' : True}},

  zipfile = None

)