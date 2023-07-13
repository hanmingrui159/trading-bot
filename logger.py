


import logging as lg
import os
from datetime import datetime

# creating a folder for the logs
logs_path = './logs/'
try:
    os.mkdir(logs_path)
except OSError:
    print("Creation of the directory %s failed - it does not have to be bad" % logs_path) 
else:
    print("succesfully created log directory")

# renaming each log depending on the time

date = datetime.now().strftime("%Y%m%d_%H%M%S")
log_name = date + ".log"
currentLog_path = logs_path + log_name

lg.basicConfig(filename=currentLog_path, format='%(asctime)s - %(levelname)s: %(message)s', level=lg.DEBUG)
lg.getLogger().addHandler(lg.StreamHandler())
# logging levels: DEBUG, INFO, WARNING, ERROR

lg.info('This is an info message!')
lg.debug('This is a debugging message!')
lg.warning('This is a warning message.')
lg.error('This is an error message!')
