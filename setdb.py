# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:45:23 2019

@author: Shilpa_Chikkannavar
"""

#!/usr/bin/python    
#import ConfigParser
#import ConfigParser as configparser
import configparser

config = configparser.RawConfigParser()
config.read('ConfigFile.properties')

print (config.get('DatabaseSection', 'database.dbname'));