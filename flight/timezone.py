#! /usr/bin/env python
#coding=utf-8

import sys
import time
import datetime
import traceback

reload(sys)
sys.setdefaultencoding('utf-8')


Airport = {
    'VLY': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'EXT': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ABZ': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'EDI': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'AAL': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'AAR': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'AES': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ADD': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'AJA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'AGA': {'standard':'0', 'summer':'0', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SCN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BCM': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'FKB': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'GYD': {'standard':'4', 'summer':'4', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DPS': {'standard':'7', 'summer':'7', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CMB': {'standard':'6', 'summer':'6', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BCN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BSL': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BIA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'AUH': {'standard':'4', 'summer':'4', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'NCL': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ACE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'CFR': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'CAI': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ATL': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CLY': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'CBG': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LPA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'CUN': {'standard':'-6', 'summer':'-6', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SEA': {'standard':'-8', 'summer':'-8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CWL': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'IOM': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CMN': {'standard':'0', 'summer':'0', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ADA': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ZAD': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ADB': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DFW': {'standard':'-6', 'summer':'-6', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DAT': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LEI': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'AHO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'EMA': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'AGB': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ANE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'AGH': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ALG': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'AGP': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ZAG': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LGW': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CDG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SOG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'HAJ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'LEH': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ATH': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'HHN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'HAM': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'HAN': {'standard':'7', 'summer':'7', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'HRB': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CGK': {'standard':'7', 'summer':'7', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'AMM': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ALC': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ERF': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SGN': {'standard':'7', 'summer':'7', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LYS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'IAS': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TLV': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TPE': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TYN': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TER': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LLA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KLX': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KHH': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KLV': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KSF': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KZN': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'ALA': {'standard':'6', 'summer':'6', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'FMM': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'PMI': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'MMX': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'LMP': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'LCA': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SZG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'AMS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FRA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KUF': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'MLA': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'MAN': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'MNL': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'PNA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TMP': {'standard':'2', 'summer':'3', \
        'summer_start':'2014-3-30T3:00:00', 'summer_end':'2014-10-26T4:00:00'},
    'MRS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'GRZ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'XCR': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SLM': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'MRU': {'standard':'4', 'summer':'4', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'AOI': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ANR': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'AYT': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'YVR': {'standard':'-8', 'summer':'-8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TSF': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'NKG': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ESB': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'NTE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'NAP': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KOW': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LHW': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'HOV': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ORN': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'OSL': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TRF': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'RYG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ORY': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BVA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'PUF': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'MOL': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ARN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'WAW': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'WMI': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'OVD': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TSE': {'standard':'6', 'summer':'6', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TAS': {'standard':'5', 'summer':'5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'IAD': {'standard':'-8', 'summer':'-8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'EAS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SCQ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ASR': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SJJ': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TNG': {'standard':'0', 'summer':'0', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'FLL': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'VLC': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'YNT': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'RGN': {'standard':'7', 'summer':'7', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DTW': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ZAZ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BHX': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BRS': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BLK': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BHD': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BFS': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LBA': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'PMO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BRI': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'OTP': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BUD': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BOO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BDS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BEG': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BWN': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BLR': {'standard':'6', 'summer':'6', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BGO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BRE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BRN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BGY': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BER': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SXF': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TXL': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BES': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BEY': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BIO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BIQ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'IBZ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'PEK': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'NAY': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BLL': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TBS': {'standard':'4', 'summer':'4', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'PSA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BZO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BLQ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BOM': {'standard':'6', 'summer':'6', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BMA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BRQ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BOD': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TGD': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'OPO': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KBP': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BOS': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'POZ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FDE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'RGS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BRU': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'CRL': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'PUS': {'standard':'9', 'summer':'9', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'PRG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'CEG': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LCY': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CAG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'REG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'GVA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TRN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SIN': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CAN': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TUN': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CTA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'COK': {'standard':'6', 'summer':'6', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'NGO': {'standard':'9', 'summer':'9', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CFE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'HER': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CGQ': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CSX': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CHC': {'standard':'12', 'summer':'12', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ORD': {'standard':'-6', 'summer':'-6', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CTU': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'NRT': {'standard':'9', 'summer':'9', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CKG': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KIV': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LPI': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'CIA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'GRO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'LCG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ORK': {'standard':'0', 'summer':'0', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CFU': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CPH': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FSC': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'CUF': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'DND': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DSA': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DME': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'DAC': {'standard':'6', 'summer':'6', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DBV': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DUB': {'standard':'0', 'summer':'0', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DXB': {'standard':'4', 'summer':'4', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DRS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'DEL': {'standard':'6', 'summer':'6', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DJE': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DIJ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TIA': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TRS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FIH': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DLC': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CFN': {'standard':'0', 'summer':'0', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'PVG': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DTM': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'DOH': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'HND': {'standard':'9', 'summer':'9', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'DUS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'NRN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SVX': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'YYZ': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LHR': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'JED': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'HFE': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'PEG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'GOA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'HEL': {'standard':'2', 'summer':'3', \
        'summer_start':'2014-3-30T3:00:00', 'summer_end':'2014-10-26T4:00:00'},
    'HDF': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'IKA': {'standard':'4', 'summer':'4', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LEJ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'JER': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KEF': {'standard':'0', 'summer':'0', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'JFK': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'NBO': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'YUL': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'MLN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'RMI': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'PMF': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'MAH': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'RAK': {'standard':'0', 'summer':'0', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SXB': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'RNS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'NQY': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'GMP': {'standard':'9', 'summer':'9', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ICN': {'standard':'9', 'summer':'9', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LED': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'VRN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'REU': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'GWT': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SVQ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TFS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TFN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'VCE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'EWR': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'FUE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FAO': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'FDH': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FCO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FLR': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FRO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FOC': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'WRO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FUK': {'standard':'9', 'summer':'9', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'GLA': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'GCI': {'standard':'0', 'summer':'0', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'GDN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'GRX': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'GOT': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'GSE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'GNB': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'GRQ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KWL': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KWE': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KHV': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'VVO': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'HAU': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'HAK': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SKG': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'HET': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'HGH': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'HKG': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'HKT': {'standard':'7', 'summer':'7', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SHA': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'PHL': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'RHO': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SVO': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'SNN': {'standard':'0', 'summer':'0', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TSA': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'IEV': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TLN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SOU': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TSN': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'NCE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'VIE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'VGO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TNA': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'RJK': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'IKT': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'SYD': {'standard':'10', 'summer':'10', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KRN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'LIN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'MXP': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'LIL': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'LIG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'VNO': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LNZ': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'LLW': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LIS': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LPL': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'MIA': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'MSQ': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'INV': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'INC': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'XNN': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'INN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'RIX': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'RUH': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ISB': {'standard':'5', 'summer':'5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'IST': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SAW': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'XMN': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'GOJ': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'JNB': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LJU': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KLR': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KLU': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KRK': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KJA': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'KSU': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KGS': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KHN': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KIX': {'standard':'9', 'summer':'9', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KRS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'CGN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KMG': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KTW': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'KUL': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'KWI': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'STN': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SEN': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'ULN': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LAX': {'standard':'-8', 'summer':'-8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LXR': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LUG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'LGA': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LXA': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LTN': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'LUX': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'MPL': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FMO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'MLH': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'MUC': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'VKO': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'NWI': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'OXF': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'FNI': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'OVB': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'NUE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SOF': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'OLB': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'RTM': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'OUL': {'standard':'2', 'summer':'3', \
        'summer_start':'2014-3-30T3:00:00', 'summer_end':'2014-10-26T4:00:00'},
    'SPU': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'PUY': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'RZE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'MCO': {'standard':'-5', 'summer':'-5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'RLG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TOS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SYY': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SVG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SKP': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'NYO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ZRH': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'UUD': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'URC': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BKK': {'standard':'7', 'summer':'7', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'WUX': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'VXO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'VBY': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SFO': {'standard':'-8', 'summer':'-8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'MAD': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FNC': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'PDL': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'NGB': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TAO': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'MIR': {'standard':'1', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'MLE': {'standard':'5', 'summer':'5', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SMI': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SZF': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TLL': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'NNG': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CGO': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'WNZ': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SHE': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SJW': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'TRD': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SIA': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'VST': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SUF': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'SDR': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TKU': {'standard':'2', 'summer':'3', \
        'summer_start':'2014-3-30T3:00:00', 'summer_end':'2014-10-26T4:00:00'},
    'TLS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'STR': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'TZX': {'standard':'2', 'summer':'2', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'WUH': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SYX': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SZX': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'STO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'AMS': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ARN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BCN': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BFS': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'BRU': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'BUD': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'CAN': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'CDG': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FCO': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'FRA': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'HEL': {'standard':'2', 'summer':'3', \
        'summer_start':'2014-3-30T3:00:00', 'summer_end':'2014-10-26T4:00:00'},
    'LHR': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'MAD': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'MAN': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'MUC': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'MXP': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'PEK': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'PVG': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'SHA': {'standard':'8', 'summer':'8', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'VCE': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'WAW': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'ZRH': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}
    }


Station = {
    'stt100012': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100013': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100010': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100011': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100016': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100017': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100014': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100015': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100302': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100303': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100018': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100019': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100306': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100307': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100304': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100305': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100098': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100099': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100232': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100092': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100093': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100090': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100091': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100096': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100097': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100094': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100095': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100108': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100109': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100178': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100233': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100168': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100169': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100166': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100167': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100164': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100165': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100162': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100163': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100160': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100161': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100027': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100026': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100025': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100024': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100023': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100022': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100021': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100020': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100029': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100028': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100230': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100292': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'stt100289': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100293': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100102': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100234': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100103': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100221': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100320': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100179': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100153': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100152': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100151': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100150': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100157': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100156': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100155': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100154': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100250': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100251': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100159': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100158': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100254': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100255': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100256': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100257': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100131': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100130': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100133': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100132': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100135': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100134': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100137': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100136': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100139': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100138': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100245': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100301': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100244': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100308': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100298': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100243': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100242': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100220': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100213': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100311': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100241': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100322': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100259': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100240': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100299': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100144': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100145': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100146': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100147': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100140': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100141': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100142': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100143': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100225': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100224': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100227': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100226': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100148': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100149': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100223': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100222': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100122': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100123': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100120': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100121': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100126': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100127': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100124': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100125': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100283': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100282': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100128': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100129': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100287': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100286': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100285': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100284': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100247': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100206': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100327': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100316': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100252': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100324': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100253': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100288': {'standard':'2', 'summer':'3', \
        'summer_start':'2014-3-30T3:00:00', 'summer_end':'2014-10-26T4:00:00'},
    'stt100218': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100219': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100038': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100039': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100238': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100239': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100030': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100031': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100032': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100033': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100034': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100035': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100036': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100037': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100117': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100116': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100115': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100114': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100113': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100112': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100111': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100110': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100294': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100281': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100296': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100297': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100290': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100291': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100119': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100118': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100323': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100319': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100199': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100198': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100197': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100196': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100195': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100194': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100193': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100192': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100191': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100190': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100326': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100309': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100295': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100321': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100203': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100202': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100201': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100200': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100049': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100048': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100205': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100204': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100045': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100044': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100047': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100046': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100041': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100040': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100043': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100042': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100261': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100260': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100263': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100262': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100265': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100264': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100267': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100266': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100269': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100268': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100180': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100181': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100182': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100183': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100184': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100185': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100186': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100187': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100188': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100189': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100209': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100212': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100208': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100231': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100214': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100215': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100216': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100217': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100210': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100211': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100058': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100059': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100056': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100057': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100054': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100055': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100052': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100053': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100050': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100051': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100272': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100273': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100270': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100271': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100276': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100277': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100274': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100275': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100258': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100278': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100279': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100310': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100229': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100236': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100207': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100228': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100325': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100063': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100062': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100061': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100060': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100067': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100066': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100065': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100064': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100100': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100101': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100069': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100068': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100104': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100105': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100106': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100107': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100001': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100246': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100003': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100002': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100005': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100004': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100007': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100006': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100009': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100008': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100313': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100312': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100315': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100314': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100249': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100248': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100089': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100088': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100318': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100280': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100237': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100081': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100080': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100083': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100082': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100085': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100084': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100087': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100086': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100317': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100235': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100171': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100300': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100170': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100074': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100075': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100076': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100077': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100070': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100071': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100072': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100073': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100175': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100174': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100177': {'standard':'3', 'summer':'3', \
        'summer_start':'2014-1-01T0:00:00', 'summer_end':'2014-1-01T0:00:00'},
    'stt100176': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100078': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100079': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'},
    'stt100173': {'standard':'0', 'summer':'1', \
        'summer_start':'2014-3-30T1:00:00', 'summer_end':'2014-10-26T2:00:00'},
    'stt100172': {'standard':'1', 'summer':'2', \
        'summer_start':'2014-3-30T2:00:00', 'summer_end':'2014-10-26T3:00:00'}
    }


def get_time_zone(para_type, params, current_time):
    para_list = ['airport', 'station']
    failed_tag = -100

    para_type = para_type.lower()
    if para_type not in para_list:
        print para_type
        print 'Wrong para type (airport, city or station)'
        return failed_tag

    try:
        year_start_sec = int(time.mktime(time.strptime('2014-1-1T0:00:00','%Y-%m-%dT%H:%M:%S')))
        year_end_sec = int(time.mktime(time.strptime('2014-12-31T23:59:59','%Y-%m-%dT%H:%M:%S')))
        current_time_sec = int(time.mktime(time.strptime(current_time,'%Y-%m-%dT%H:%M:%S')))

        if para_type == 'airport':
            summer_start = Airport[params]['summer_start']
            summer_end = Airport[params]['summer_end']
            summer_start_sec = int(time.mktime(time.strptime(summer_start,'%Y-%m-%dT%H:%M:%S')))
            summer_end_sec = int(time.mktime(time.strptime(summer_end,'%Y-%m-%dT%H:%M:%S')))

            if current_time_sec > summer_start_sec and current_time_sec < summer_end_sec:
                timezone = int(Airport[params]['summer'])
            elif (current_time_sec > year_start_sec and current_time_sec < summer_start_sec) or \
                (current_time_sec > summer_end_sec and current_time_sec < year_end_sec):
                timezone = int(Airport[params]['standard'])
            else:
                timezone = failed_tag
            return timezone

        elif para_type == 'station':
            summer_start = Station[params]['summer_start']
            summer_end = Station[params]['summer_end']
            summer_start_sec = int(time.mktime(time.strptime(summer_start,'%Y-%m-%dT%H:%M:%S')))
            summer_end_sec = int(time.mktime(time.strptime(summer_end,'%Y-%m-%dT%H:%M:%S')))

            if current_time_sec > summer_start_sec and current_time_sec < summer_end_sec:
                timezone = int(Station[params]['summer'])
            elif (current_time_sec > year_start_sec and current_time_sec < summer_start_sec) or \
                (current_time_sec > summer_end_sec and current_time_sec < year_end_sec):
                timezone = int(Station[params]['standard'])
            else:
                timezone = failed_tag
            return timezone

        else:
            return failed_tag

    except Exception, e:
        print 'Wrong Time Format: ' + current_time
        #traceback.print_exc(e)
        return failed_tag

if __name__ == '__main__':
    print get_time_zone('station', 'stt100325', '2014-09-14T08:19:00')
    print get_time_zone('airport', 'ZRH', '2014-03-14T08:19:00')
