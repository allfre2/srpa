from modules.args import RPAArgs
from modules.rpa import RPA

import sys, logging

if not __debug__:
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
else:
    logging.basicConfig(format="%(message)s")

options = {}

try:
    options = RPAArgs(sys.argv[1:]).getOptions()
    rpa = RPA.getRPA(options)
    rpa.exec()

except Exception as e:
    logging.error(e)
