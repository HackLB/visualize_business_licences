#!/usr/bin/env python
import os, sys
from pprint import pprint
import simplejson as json
import requests
from license import License, Generator

if __name__ == "__main__":
    repo_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    source_path = os.path.join(os.path.dirname(repo_path), 'business_licenses', '_data')
    data_path = os.path.join(repo_path, 'data.json')


    first_year = 2017

    for directory, directories, files in os.walk(source_path, topdown=False):
        for name in files:
            if name.endswith('.json'):
                path = os.path.join(directory, name)

                with open(path) as f:
                    raw_record = json.load(f)

                start_date = raw_record['properties'].get('ISSDTTM')
                if start_date:
                    start_year = int(start_date[0:4])
                    if start_year < first_year and start_year > 1900:
                        first_year = start_year

                    # if start_year < 1900:
                    #     pprint(path)
                    #     pprint(raw_record)


    print('first_year', first_year)