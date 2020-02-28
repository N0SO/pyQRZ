from __future__ import print_function
from __future__ import print_function
from __future__ import print_function
import os.path
import sys
import argparse

DEVMODPATH = ['qrz']
# If the development module source paths exist, 
# add them to the python path
for mypath in DEVMODPATH:
    if ( os.path.exists(mypath) and \
                       (os.path.isfile(mypath) == False) ):
        sys.path.insert(0,mypath)
#print('Python path = %s'%(sys.path))
from qrz import QRZ

DESCRIPTION = \
"""moqpcategory  - Determine which Missouri QSO Party Award
                   category a Cabrillo Format log file is in.
                
                   Based on 2019 MOQP Rules
"""

EPILOG = \
"""
Running with no parameters will launch the GUI.
"""

class get_args():
    def __init__(self):
        if __name__ == '__main__':
            self.args = self.getargs()
            
    def getargs(self):
        parser = argparse.ArgumentParser(\
                               description = DESCRIPTION,
                                           epilog = EPILOG)
        #parser.add_argument('-v', '--version', action='version', version = VERSION)
        parser.add_argument('-c', '--callsign', default=None,
            help='CALLSIGN in MOQP database to summarize. Entering allcalls = all calls in database')
        #parser.add_argument('-d', '--digital', default=None,
            #help='Summarize digital QSOs only for CALLSIGN in MOQP database. Entering allcalls = all calls in database')
        #parser.add_argument('-U', '--vhf', default=None,
            #help='Summarize VHF QSOs only for CALLSIGN in MOQP database. Entering allcalls = all calls in database')
        #parser.add_argument('-i', '--inputpath', default=None,
            #help='Specifies the path to the folder that contains the log files to summarize.')
        return parser.parse_args()


def print_keys(key_names, query_result):
    """
    Prints results and does not throw exception on queries
    like W1AW where fname key does not exist
    """
    info = ""
    for key_name in key_names:
        if key_name in query_result:
            info += query_result[key_name] + " "
    print(info)


if __name__ == '__main__':
    args = get_args()
   
    if (args.args.callsign):
        qrz = QRZ('./settings.cfg')
        result = qrz.callsign("w7atc")
        print_keys(['fname', 'name'], result)
        print_keys(['addr2', 'state'], result)
        print_keys(['country'], result)
        # Show all the data available from QRZ.com
        print('-' * 50)
        for dict_key, dict_value in sorted(result.items()):
            print(u'{0}: {1}'.format(dict_key, dict_value))
    else:
       print('Give me a sign...')