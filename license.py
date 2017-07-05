#!/usr/bin/env python
import os, sys
from pprint import pprint
import arrow
from dateutil.relativedelta import relativedelta


first_year = 1980

class License():
    """
    An object representing a Business License in Long Beach
    """
    data = None
    date_started = None
    date_ended = None
    still_open = None
    months = None
    district = None
    index = None

    def __init__(self, data):
        self.data = data
        props = data['properties']

        self.category = props.get('LICCATDESC')

        self.date_started = arrow.get(props.get('ISSDTTM')).datetime
        if self.date_started.year < 1900:
            self.date_started = None

        if props.get('MILESTONE') == 'Closed':
            self.date_ended = arrow.get(props.get('MILESTONEDATE')).datetime
            self.still_open = False
        else:
            self.date_ended = arrow.utcnow().datetime
            self.still_open = True

        self.district = props.get('COUNCILDISTRICT')

        if self.date_ended < self.date_started:
            self.date_ended, self.date_started = self.date_started, self.date_ended

        self.months = (relativedelta(self.date_ended, self.date_started).years * 12) + (relativedelta(self.date_ended, self.date_started).months)

        self.index = self.date_started.year - first_year


class Generator():

    data = {}
    start_year = first_year
    end_year = 2017

    districts = 9

    def __init__(self):
        self.data['labels'] = [str(x) for x in range(self.start_year, self.end_year + 1)]

        self.data['datasets'] = []
        for district in range(1, self.districts + 1):
            dist_rec = {'label': "District {}".format(district), 'data': []}

            dist_rec['data'] = [0 for x in range(self.end_year - self.start_year + 1)]

            self.data['datasets'].append(dist_rec)
            # print (dist_rec)