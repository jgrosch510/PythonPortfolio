#!/usr/bin/env python3

import os, sys
import json
import toml

def main():
    gitHome = os.getenv('GIT_HOME')
    baseDir = f"{gitHome}/PythonPortfolio"
    etcDir = f"{baseDir}/etc"

    tomlFile = f"{etcDir}/MusicBank.conf"
    jsonFile = f"{etcDir}/MusicBank.json"
    xmlFile  = f"{etcDir}/MusicBank.xml"

    iterms = os.environ.items()

    for key, value in os.environ.items():
        print('{}: {}'.format(key, value))
    
    sys.exit(0)
    # End of main

if __name__ == '__main__':
    main()
    
