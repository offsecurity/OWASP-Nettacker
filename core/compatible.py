#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from core.alert import *

try:
    version_info = open('version').read().rsplit()
    __version__ = version_info[0]
    __code_name__ = ' '.join(version_info[1:])
except:
    __version__ = 'UNKNOWN'
    __code_name__ = 'UNKNOWN'


def _version_info():
    version_info = open('version').read().rsplit()
    return [version_info[0], ' '.join(version_info[1:])]


def logo():
    from core.alert import write_to_api_console
    from core import color
    from core.color import finish
    write_to_api_console('''    
   ______          __      _____ _____  
  / __ \ \        / /\    / ____|  __ \ 
 | |  | \ \  /\  / /  \  | (___ | |__) |
 | |  | |\ \/  \/ / /\ \  \___ \|  ___/ 
 | |__| | \  /\  / ____ \ ____) | |     {2}Version {0}{3}  
  \____/   \/  \/_/    \_\_____/|_|     {4}{1}{5}
                          _   _      _   _             _            
                         | \ | |    | | | |           | |            
  {6}github.com/viraintel{7}   |  \| | ___| |_| |_ __ _  ___| | _____ _ __ 
  {8}owasp.org{9}              | . ` |/ _ \ __| __/ _` |/ __| |/ / _ \ '__|
  {10}viraintel.com{11}          | |\  |  __/ |_| || (_| | (__|   <  __/ |   
                         |_| \_|\___|\__|\__\__,_|\___|_|\_\___|_|   
                                               
    \n\n'''.format(__version__, __code_name__, color.color('red'), color.color('reset'), color.color('yellow'),
                   color.color('reset'), color.color('cyan'), color.color('reset'), color.color('cyan'),
                   color.color('reset'), color.color('cyan'), color.color('reset')))
    finish()


def version():
    return int(sys.version_info[0])


def check(language):
    from core.color import finish
    if 'linux' in os_name() or 'darwin' in os_name():
        pass
        # os.system('clear')
    elif 'win32' == os_name() or 'win64' == os_name():
        # if language != 'en':
        #    from core.color import finish
        #    from core.alert import error
        #   error('please use english language on windows!')
        #    finish()
        #    sys.exit(1)
        # os.system('cls')
        pass
    else:
        error(messages(language, 47))
        finish()
        sys.exit(1)
    if version() is 2 or version() is 3:
        pass
    else:
        error(messages(language, 48))
        finish()
        sys.exit(1)
    logo()
    return


def os_name():
    return sys.platform
