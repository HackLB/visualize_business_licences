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

    print(source_path, data_path)

    data = {}
    categories = []

    chart = Generator().data

    for directory, directories, files in os.walk(source_path, topdown=False):
        for name in files:
            if name.endswith('.json'):
                path = os.path.join(directory, name)

                with open(path) as f:
                    raw_record = json.load(f)

                category = raw_record['properties'].get('LICCATDESC', '')

                start_date = raw_record['properties'].get('ISSDTTM')
                if start_date:
                    start_year = int(start_date[0:4])
                    if start_year > 1980:

                        # print('raw', raw_record)
                        if category and 'Restaurant' in category:
                            lic = License(raw_record)
                            print(lic.data)
                            print(lic.months)
                            print(lic.date_started)
                            print(lic.date_ended)
                            disti = lic.district - 1

                            print('license index:', lic.index)
                            chart['datasets'][disti]['data'][lic.index] = chart['datasets'][disti]['data'][lic.index] + 1

                            print('----------------------------------------')


    with open(data_path, 'w') as f:
        json.dump(chart, f, indent=4, ensure_ascii=False, sort_keys=True)

    # pprint(chart)


    # pprint(categories.sort())