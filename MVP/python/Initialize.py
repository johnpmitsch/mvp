"""
One time initialization of data for the MVP
Create a uuid to uniquely identify this MVP
# Author: Howard Webb
# Data: 2018/07/09
"""

import uuid
from datetime import tzinfo, datetime
import json

env_file = '/home/pi/MVP/python/env.py'

def initialize():
    """One time setup of the environment - get UUID of Field
        Args: None
        Returns: None
        Raises:
            None
    """    
    env = {}
    env['field'] = get_field()
#    env['location'] = str(get_location())
    save_dictionary('env', env_file, env)

def get_field(name='Field Name'):
    """ Create the field object
        Create a uuid to uniquely identify this MVP
        Args:
            name : useful name given to the MVP
        Returns:
            None
        Raises:
            None
    """    

    field = {}
    field['field_id'] = str(uuid.uuid4())
    return field


def save_dictionary(name, file_name, dict):
    """Save structure to a file
        Args:
            name : name of the structure
            file_name : name of the file to save to
            dict : dictionary structure to save
        Returns: None
        Raises:
            None
    """    
    #print(values)
    with open(file_name, 'w+') as f:
        tmp = name+'='+str(dict)
        f.write(tmp)

def pretty_print(txt):
    """Do nice formatting of the JSON structure
        Args:
            txt : json data to print
        Returns:
            msgs: array of messages
        Raises:
            None
    """    
    #print type(txt)
    print(json.dumps(txt, indent=4, sort_keys=True))
    
def test():
    """Print out the env.py dictionary
        Args:
            None
        Returns:
            None
        Raises:
            None
    """    
    from env import env
    pretty_print(env)

if __name__=="__main__":
    initialize()
    
