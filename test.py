#!/usr/bin/env python
import os, sys
from pprint import pprint
import simplejson as json
import requests
from license import License, Generator

if __name__ == "__main__":


    data = Generator()

    pprint(data.data)