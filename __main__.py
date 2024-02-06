#! /usr/bin/env python3

"""
Sherlock: Find Usernames Across Social Networks Module

This module contains the main logic to search for usernames at social
networks.
"""

import sys
import sherlock

if __name__ == "__main__":
    # Check if the user is using the correct version of Python
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 6):
        print("Sherlock requires Python 3.6+\nYou are using Python %s, which is not supported by Sherlock" % (python_version))
        sys.exit(1)
    elif sys.version_info > (3, 6):
        print(
    """

 _    _         _                        _  _ 
| |  | |       | |                      | || |
| |  | |  __ _ | |_  ___   ___   _ __   | || |
| |/\| | / _` || __|/ __| / _ \ | '_ \  | || |
\  /\  /| (_| || |_ \__ \| (_) || | | | |_||_|
 \/  \/  \__,_| \__||___/ \___/ |_| |_| (_)(_)
                                              
                                              

""")
        sherlock.main()

    
    
