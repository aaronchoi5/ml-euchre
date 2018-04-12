#!/usr/bin/env python

import argparse
import os.path
import pandas as pd
import numpy as np
import time
import datetime


def run():

    pa = argparse.ArgumentParser()
    pa.add_argument('-f', '--file', action='store', nargs=1, dest='FILENAME',
                    help='Euchre.py overview log CSV filename',
                    metavar='*.csv', required=True)
    args = pa.parse_args()

    raw_csv = args.FILENAME[0]

    if not (os.path.isfile(raw_csv) and os.access(raw_csv, os.R_OK)):
        print 'ERROR - File Does Not Exist / Is Not Readable'
        exit()

    df = pd.read_csv(raw_csv)

    print '\nNUMBER OF ROUNDS: %s' % len(df)

    print '\nDATAFRAME COLUMNS: \n%s' % df.columns

    df = df.drop(df[(df.CALLER_TEAM != df.WINNER_TEAM)].index)

    print '\nNUMBER OF ROUNDS AFTER FILTERING: %s' % len(df)

    print "\nMERGING PLAYERS..."

    df['P1_1'] = np.NaN
    df['P1_2'] = np.NaN
    df['P1_3'] = np.NaN
    df['P1_4'] = np.NaN
    df['P1_5'] = np.NaN
    df['P2_1'] = np.NaN
    df['P2_2'] = np.NaN
    df['P2_3'] = np.NaN
    df['P2_4'] = np.NaN
    df['P2_5'] = np.NaN

    count = 0

    for idx, row in df.iterrows():
        if df.loc[idx, 'CALLER_TEAM'] == 'A':
            df.loc[idx, 'P1_1'] = df.loc[idx, 'PA1_C1']
            df.loc[idx, 'P1_2'] = df.loc[idx, 'PA1_C2']
            df.loc[idx, 'P1_3'] = df.loc[idx, 'PA1_C3']
            df.loc[idx, 'P1_4'] = df.loc[idx, 'PA1_C4']
            df.loc[idx, 'P1_5'] = df.loc[idx, 'PA1_C5']
            df.loc[idx, 'P2_1'] = df.loc[idx, 'PA2_C1']
            df.loc[idx, 'P2_2'] = df.loc[idx, 'PA2_C2']
            df.loc[idx, 'P2_3'] = df.loc[idx, 'PA2_C3']
            df.loc[idx, 'P2_4'] = df.loc[idx, 'PA2_C4']
            df.loc[idx, 'P2_5'] = df.loc[idx, 'PA2_C5']
        else:
            df.loc[idx, 'P1_1'] = df.loc[idx, 'PB1_C1']
            df.loc[idx, 'P1_2'] = df.loc[idx, 'PB1_C2']
            df.loc[idx, 'P1_3'] = df.loc[idx, 'PB1_C3']
            df.loc[idx, 'P1_4'] = df.loc[idx, 'PB1_C4']
            df.loc[idx, 'P1_5'] = df.loc[idx, 'PB1_C5']
            df.loc[idx, 'P2_1'] = df.loc[idx, 'PB2_C1']
            df.loc[idx, 'P2_2'] = df.loc[idx, 'PB2_C2']
            df.loc[idx, 'P2_3'] = df.loc[idx, 'PB2_C3']
            df.loc[idx, 'P2_4'] = df.loc[idx, 'PB2_C4']
            df.loc[idx, 'P2_5'] = df.loc[idx, 'PB2_C5']
        count = count + 1
        if count % 1500 == 0:
            print count
    print count
    print "...DONE"

    print "\nDROPPING COLUMNS..."

    columns = ['GAME', 'CALLER_TEAM', 'CALLER', 'WINNER_TEAM',
               'PA1_C1', 'PA1_C2', 'PA1_C3', 'PA1_C4', 'PA1_C5',
               'PA2_C1', 'PA2_C2', 'PA2_C3', 'PA2_C4', 'PA2_C5',
               'PB1_C1', 'PB1_C2', 'PB1_C3', 'PB1_C4', 'PB1_C5',
               'PB2_C1', 'PB2_C2', 'PB2_C3', 'PB2_C4', 'PB2_C5']
    df.drop(columns, inplace=True, axis=1)

    count = 0

    print '\nDATAFRAME COLUMNS: \n%s' % df.columns

    print "\nSTARTING FILE GENERATION..."

    for idx, row in df.iterrows():
        if df.loc[idx, 'P1_1'] == '09D':
            df.loc[idx, '09D'] = 1
        elif df.loc[idx, 'P1_2'] == '09D':
            df.loc[idx, '09D'] = 1
        elif df.loc[idx, 'P1_3'] == '09D':
            df.loc[idx, '09D'] = 1
        elif df.loc[idx, 'P1_4'] == '09D':
            df.loc[idx, '09D'] = 1
        elif df.loc[idx, 'P1_5'] == '09D':
            df.loc[idx, '09D'] = 1
        elif df.loc[idx, 'P2_1'] == '09D':
            df.loc[idx, '09D'] = 1
        elif df.loc[idx, 'P2_2'] == '09D':
            df.loc[idx, '09D'] = 1
        elif df.loc[idx, 'P2_3'] == '09D':
            df.loc[idx, '09D'] = 1
        elif df.loc[idx, 'P2_4'] == '09D':
            df.loc[idx, '09D'] = 1
        elif df.loc[idx, 'P2_5'] == '09D':
            df.loc[idx, '09D'] = 1
        else:
            df.loc[idx, '09D'] = 0

        if df.loc[idx, 'P1_1'] == '10D':
            df.loc[idx, '10D'] = 1
        elif df.loc[idx, 'P1_2'] == '10D':
            df.loc[idx, '10D'] = 1
        elif df.loc[idx, 'P1_3'] == '10D':
            df.loc[idx, '10D'] = 1
        elif df.loc[idx, 'P1_4'] == '10D':
            df.loc[idx, '10D'] = 1
        elif df.loc[idx, 'P1_5'] == '10D':
            df.loc[idx, '10D'] = 1
        elif df.loc[idx, 'P2_1'] == '10D':
            df.loc[idx, '10D'] = 1
        elif df.loc[idx, 'P2_2'] == '10D':
            df.loc[idx, '10D'] = 1
        elif df.loc[idx, 'P2_3'] == '10D':
            df.loc[idx, '10D'] = 1
        elif df.loc[idx, 'P2_4'] == '10D':
            df.loc[idx, '10D'] = 1
        elif df.loc[idx, 'P2_5'] == '10D':
            df.loc[idx, '10D'] = 1
        else:
            df.loc[idx, '10D'] = 0

        if df.loc[idx, 'P1_1'] == '11D':
            df.loc[idx, '11D'] = 1
        elif df.loc[idx, 'P1_2'] == '11D':
            df.loc[idx, '11D'] = 1
        elif df.loc[idx, 'P1_3'] == '11D':
            df.loc[idx, '11D'] = 1
        elif df.loc[idx, 'P1_4'] == '11D':
            df.loc[idx, '11D'] = 1
        elif df.loc[idx, 'P1_5'] == '11D':
            df.loc[idx, '11D'] = 1
        elif df.loc[idx, 'P2_1'] == '11D':
            df.loc[idx, '11D'] = 1
        elif df.loc[idx, 'P2_2'] == '11D':
            df.loc[idx, '11D'] = 1
        elif df.loc[idx, 'P2_3'] == '11D':
            df.loc[idx, '11D'] = 1
        elif df.loc[idx, 'P2_4'] == '11D':
            df.loc[idx, '11D'] = 1
        elif df.loc[idx, 'P2_5'] == '11D':
            df.loc[idx, '11D'] = 1
        else:
            df.loc[idx, '11D'] = 0

        if df.loc[idx, 'P1_1'] == '12D':
            df.loc[idx, '12D'] = 1
        elif df.loc[idx, 'P1_2'] == '12D':
            df.loc[idx, '12D'] = 1
        elif df.loc[idx, 'P1_3'] == '12D':
            df.loc[idx, '12D'] = 1
        elif df.loc[idx, 'P1_4'] == '12D':
            df.loc[idx, '12D'] = 1
        elif df.loc[idx, 'P1_5'] == '12D':
            df.loc[idx, '12D'] = 1
        elif df.loc[idx, 'P2_1'] == '12D':
            df.loc[idx, '12D'] = 1
        elif df.loc[idx, 'P2_2'] == '12D':
            df.loc[idx, '12D'] = 1
        elif df.loc[idx, 'P2_3'] == '12D':
            df.loc[idx, '12D'] = 1
        elif df.loc[idx, 'P2_4'] == '12D':
            df.loc[idx, '12D'] = 1
        elif df.loc[idx, 'P2_5'] == '12D':
            df.loc[idx, '12D'] = 1
        else:
            df.loc[idx, '12D'] = 0

        if df.loc[idx, 'P1_1'] == '13D':
            df.loc[idx, '13D'] = 1
        elif df.loc[idx, 'P1_2'] == '13D':
            df.loc[idx, '13D'] = 1
        elif df.loc[idx, 'P1_3'] == '13D':
            df.loc[idx, '13D'] = 1
        elif df.loc[idx, 'P1_4'] == '13D':
            df.loc[idx, '13D'] = 1
        elif df.loc[idx, 'P1_5'] == '13D':
            df.loc[idx, '13D'] = 1
        elif df.loc[idx, 'P2_1'] == '13D':
            df.loc[idx, '13D'] = 1
        elif df.loc[idx, 'P2_2'] == '13D':
            df.loc[idx, '13D'] = 1
        elif df.loc[idx, 'P2_3'] == '13D':
            df.loc[idx, '13D'] = 1
        elif df.loc[idx, 'P2_4'] == '13D':
            df.loc[idx, '13D'] = 1
        elif df.loc[idx, 'P2_5'] == '13D':
            df.loc[idx, '13D'] = 1
        else:
            df.loc[idx, '13D'] = 0

        if df.loc[idx, 'P1_1'] == '14D':
            df.loc[idx, '14D'] = 1
        elif df.loc[idx, 'P1_2'] == '14D':
            df.loc[idx, '14D'] = 1
        elif df.loc[idx, 'P1_3'] == '14D':
            df.loc[idx, '14D'] = 1
        elif df.loc[idx, 'P1_4'] == '14D':
            df.loc[idx, '14D'] = 1
        elif df.loc[idx, 'P1_5'] == '14D':
            df.loc[idx, '14D'] = 1
        elif df.loc[idx, 'P2_1'] == '14D':
            df.loc[idx, '14D'] = 1
        elif df.loc[idx, 'P2_2'] == '14D':
            df.loc[idx, '14D'] = 1
        elif df.loc[idx, 'P2_3'] == '14D':
            df.loc[idx, '14D'] = 1
        elif df.loc[idx, 'P2_4'] == '14D':
            df.loc[idx, '14D'] = 1
        elif df.loc[idx, 'P2_5'] == '14D':
            df.loc[idx, '14D'] = 1
        else:
            df.loc[idx, '14D'] = 0

        if df.loc[idx, 'P1_1'] == '09H':
            df.loc[idx, '09H'] = 1
        elif df.loc[idx, 'P1_2'] == '09H':
            df.loc[idx, '09H'] = 1
        elif df.loc[idx, 'P1_3'] == '09H':
            df.loc[idx, '09H'] = 1
        elif df.loc[idx, 'P1_4'] == '09H':
            df.loc[idx, '09H'] = 1
        elif df.loc[idx, 'P1_5'] == '09H':
            df.loc[idx, '09H'] = 1
        elif df.loc[idx, 'P2_1'] == '09H':
            df.loc[idx, '09H'] = 1
        elif df.loc[idx, 'P2_2'] == '09H':
            df.loc[idx, '09H'] = 1
        elif df.loc[idx, 'P2_3'] == '09H':
            df.loc[idx, '09H'] = 1
        elif df.loc[idx, 'P2_4'] == '09H':
            df.loc[idx, '09H'] = 1
        elif df.loc[idx, 'P2_5'] == '09H':
            df.loc[idx, '09H'] = 1
        else:
            df.loc[idx, '09H'] = 0

        if df.loc[idx, 'P1_1'] == '10H':
            df.loc[idx, '10H'] = 1
        elif df.loc[idx, 'P1_2'] == '10H':
            df.loc[idx, '10H'] = 1
        elif df.loc[idx, 'P1_3'] == '10H':
            df.loc[idx, '10H'] = 1
        elif df.loc[idx, 'P1_4'] == '10H':
            df.loc[idx, '10H'] = 1
        elif df.loc[idx, 'P1_5'] == '10H':
            df.loc[idx, '10H'] = 1
        elif df.loc[idx, 'P2_1'] == '10H':
            df.loc[idx, '10H'] = 1
        elif df.loc[idx, 'P2_2'] == '10H':
            df.loc[idx, '10H'] = 1
        elif df.loc[idx, 'P2_3'] == '10H':
            df.loc[idx, '10H'] = 1
        elif df.loc[idx, 'P2_4'] == '10H':
            df.loc[idx, '10H'] = 1
        elif df.loc[idx, 'P2_5'] == '10H':
            df.loc[idx, '10H'] = 1
        else:
            df.loc[idx, '10H'] = 0

        if df.loc[idx, 'P1_1'] == '11H':
            df.loc[idx, '11H'] = 1
        elif df.loc[idx, 'P1_2'] == '11H':
            df.loc[idx, '11H'] = 1
        elif df.loc[idx, 'P1_3'] == '11H':
            df.loc[idx, '11H'] = 1
        elif df.loc[idx, 'P1_4'] == '11H':
            df.loc[idx, '11H'] = 1
        elif df.loc[idx, 'P1_5'] == '11H':
            df.loc[idx, '11H'] = 1
        elif df.loc[idx, 'P2_1'] == '11H':
            df.loc[idx, '11H'] = 1
        elif df.loc[idx, 'P2_2'] == '11H':
            df.loc[idx, '11H'] = 1
        elif df.loc[idx, 'P2_3'] == '11H':
            df.loc[idx, '11H'] = 1
        elif df.loc[idx, 'P2_4'] == '11H':
            df.loc[idx, '11H'] = 1
        elif df.loc[idx, 'P2_5'] == '11H':
            df.loc[idx, '11H'] = 1
        else:
            df.loc[idx, '11H'] = 0

        if df.loc[idx, 'P1_1'] == '12H':
            df.loc[idx, '12H'] = 1
        elif df.loc[idx, 'P1_2'] == '12H':
            df.loc[idx, '12H'] = 1
        elif df.loc[idx, 'P1_3'] == '12H':
            df.loc[idx, '12H'] = 1
        elif df.loc[idx, 'P1_4'] == '12H':
            df.loc[idx, '12H'] = 1
        elif df.loc[idx, 'P1_5'] == '12H':
            df.loc[idx, '12H'] = 1
        elif df.loc[idx, 'P2_1'] == '12H':
            df.loc[idx, '12H'] = 1
        elif df.loc[idx, 'P2_2'] == '12H':
            df.loc[idx, '12H'] = 1
        elif df.loc[idx, 'P2_3'] == '12H':
            df.loc[idx, '12H'] = 1
        elif df.loc[idx, 'P2_4'] == '12H':
            df.loc[idx, '12H'] = 1
        elif df.loc[idx, 'P2_5'] == '12H':
            df.loc[idx, '12H'] = 1
        else:
            df.loc[idx, '12H'] = 0

        if df.loc[idx, 'P1_1'] == '13H':
            df.loc[idx, '13H'] = 1
        elif df.loc[idx, 'P1_2'] == '13H':
            df.loc[idx, '13H'] = 1
        elif df.loc[idx, 'P1_3'] == '13H':
            df.loc[idx, '13H'] = 1
        elif df.loc[idx, 'P1_4'] == '13H':
            df.loc[idx, '13H'] = 1
        elif df.loc[idx, 'P1_5'] == '13H':
            df.loc[idx, '13H'] = 1
        elif df.loc[idx, 'P2_1'] == '13H':
            df.loc[idx, '13H'] = 1
        elif df.loc[idx, 'P2_2'] == '13H':
            df.loc[idx, '13H'] = 1
        elif df.loc[idx, 'P2_3'] == '13H':
            df.loc[idx, '13H'] = 1
        elif df.loc[idx, 'P2_4'] == '13H':
            df.loc[idx, '13H'] = 1
        elif df.loc[idx, 'P2_5'] == '13H':
            df.loc[idx, '13H'] = 1
        else:
            df.loc[idx, '13H'] = 0

        if df.loc[idx, 'P1_1'] == '14H':
            df.loc[idx, '14H'] = 1
        elif df.loc[idx, 'P1_2'] == '14H':
            df.loc[idx, '14H'] = 1
        elif df.loc[idx, 'P1_3'] == '14H':
            df.loc[idx, '14H'] = 1
        elif df.loc[idx, 'P1_4'] == '14H':
            df.loc[idx, '14H'] = 1
        elif df.loc[idx, 'P1_5'] == '14H':
            df.loc[idx, '14H'] = 1
        elif df.loc[idx, 'P2_1'] == '14H':
            df.loc[idx, '14H'] = 1
        elif df.loc[idx, 'P2_2'] == '14H':
            df.loc[idx, '14H'] = 1
        elif df.loc[idx, 'P2_3'] == '14H':
            df.loc[idx, '14H'] = 1
        elif df.loc[idx, 'P2_4'] == '14H':
            df.loc[idx, '14H'] = 1
        elif df.loc[idx, 'P2_5'] == '14H':
            df.loc[idx, '14H'] = 1
        else:
            df.loc[idx, '14H'] = 0

        if df.loc[idx, 'P1_1'] == '09C':
            df.loc[idx, '09C'] = 1
        elif df.loc[idx, 'P1_2'] == '09C':
            df.loc[idx, '09C'] = 1
        elif df.loc[idx, 'P1_3'] == '09C':
            df.loc[idx, '09C'] = 1
        elif df.loc[idx, 'P1_4'] == '09C':
            df.loc[idx, '09C'] = 1
        elif df.loc[idx, 'P1_5'] == '09C':
            df.loc[idx, '09C'] = 1
        elif df.loc[idx, 'P2_1'] == '09C':
            df.loc[idx, '09C'] = 1
        elif df.loc[idx, 'P2_2'] == '09C':
            df.loc[idx, '09C'] = 1
        elif df.loc[idx, 'P2_3'] == '09C':
            df.loc[idx, '09C'] = 1
        elif df.loc[idx, 'P2_4'] == '09C':
            df.loc[idx, '09C'] = 1
        elif df.loc[idx, 'P2_5'] == '09C':
            df.loc[idx, '09C'] = 1
        else:
            df.loc[idx, '09C'] = 0

        if df.loc[idx, 'P1_1'] == '10C':
            df.loc[idx, '10C'] = 1
        elif df.loc[idx, 'P1_2'] == '10C':
            df.loc[idx, '10C'] = 1
        elif df.loc[idx, 'P1_3'] == '10C':
            df.loc[idx, '10C'] = 1
        elif df.loc[idx, 'P1_4'] == '10C':
            df.loc[idx, '10C'] = 1
        elif df.loc[idx, 'P1_5'] == '10C':
            df.loc[idx, '10C'] = 1
        elif df.loc[idx, 'P2_1'] == '10C':
            df.loc[idx, '10C'] = 1
        elif df.loc[idx, 'P2_2'] == '10C':
            df.loc[idx, '10C'] = 1
        elif df.loc[idx, 'P2_3'] == '10C':
            df.loc[idx, '10C'] = 1
        elif df.loc[idx, 'P2_4'] == '10C':
            df.loc[idx, '10C'] = 1
        elif df.loc[idx, 'P2_5'] == '10C':
            df.loc[idx, '10C'] = 1
        else:
            df.loc[idx, '10C'] = 0

        if df.loc[idx, 'P1_1'] == '11C':
            df.loc[idx, '11C'] = 1
        elif df.loc[idx, 'P1_2'] == '11C':
            df.loc[idx, '11C'] = 1
        elif df.loc[idx, 'P1_3'] == '11C':
            df.loc[idx, '11C'] = 1
        elif df.loc[idx, 'P1_4'] == '11C':
            df.loc[idx, '11C'] = 1
        elif df.loc[idx, 'P1_5'] == '11C':
            df.loc[idx, '11C'] = 1
        elif df.loc[idx, 'P2_1'] == '11C':
            df.loc[idx, '11C'] = 1
        elif df.loc[idx, 'P2_2'] == '11C':
            df.loc[idx, '11C'] = 1
        elif df.loc[idx, 'P2_3'] == '11C':
            df.loc[idx, '11C'] = 1
        elif df.loc[idx, 'P2_4'] == '11C':
            df.loc[idx, '11C'] = 1
        elif df.loc[idx, 'P2_5'] == '11C':
            df.loc[idx, '11C'] = 1
        else:
            df.loc[idx, '11C'] = 0

        if df.loc[idx, 'P1_1'] == '12C':
            df.loc[idx, '12C'] = 1
        elif df.loc[idx, 'P1_2'] == '12C':
            df.loc[idx, '12C'] = 1
        elif df.loc[idx, 'P1_3'] == '12C':
            df.loc[idx, '12C'] = 1
        elif df.loc[idx, 'P1_4'] == '12C':
            df.loc[idx, '12C'] = 1
        elif df.loc[idx, 'P1_5'] == '12C':
            df.loc[idx, '12C'] = 1
        elif df.loc[idx, 'P2_1'] == '12C':
            df.loc[idx, '12C'] = 1
        elif df.loc[idx, 'P2_2'] == '12C':
            df.loc[idx, '12C'] = 1
        elif df.loc[idx, 'P2_3'] == '12C':
            df.loc[idx, '12C'] = 1
        elif df.loc[idx, 'P2_4'] == '12C':
            df.loc[idx, '12C'] = 1
        elif df.loc[idx, 'P2_5'] == '12C':
            df.loc[idx, '12C'] = 1
        else:
            df.loc[idx, '12C'] = 0

        if df.loc[idx, 'P1_1'] == '13C':
            df.loc[idx, '13C'] = 1
        elif df.loc[idx, 'P1_2'] == '13C':
            df.loc[idx, '13C'] = 1
        elif df.loc[idx, 'P1_3'] == '13C':
            df.loc[idx, '13C'] = 1
        elif df.loc[idx, 'P1_4'] == '13C':
            df.loc[idx, '13C'] = 1
        elif df.loc[idx, 'P1_5'] == '13C':
            df.loc[idx, '13C'] = 1
        elif df.loc[idx, 'P2_1'] == '13C':
            df.loc[idx, '13C'] = 1
        elif df.loc[idx, 'P2_2'] == '13C':
            df.loc[idx, '13C'] = 1
        elif df.loc[idx, 'P2_3'] == '13C':
            df.loc[idx, '13C'] = 1
        elif df.loc[idx, 'P2_4'] == '13C':
            df.loc[idx, '13C'] = 1
        elif df.loc[idx, 'P2_5'] == '13C':
            df.loc[idx, '13C'] = 1
        else:
            df.loc[idx, '13C'] = 0

        if df.loc[idx, 'P1_1'] == '14C':
            df.loc[idx, '14C'] = 1
        elif df.loc[idx, 'P1_2'] == '14C':
            df.loc[idx, '14C'] = 1
        elif df.loc[idx, 'P1_3'] == '14C':
            df.loc[idx, '14C'] = 1
        elif df.loc[idx, 'P1_4'] == '14C':
            df.loc[idx, '14C'] = 1
        elif df.loc[idx, 'P1_5'] == '14C':
            df.loc[idx, '14C'] = 1
        elif df.loc[idx, 'P2_1'] == '14C':
            df.loc[idx, '14C'] = 1
        elif df.loc[idx, 'P2_2'] == '14C':
            df.loc[idx, '14C'] = 1
        elif df.loc[idx, 'P2_3'] == '14C':
            df.loc[idx, '14C'] = 1
        elif df.loc[idx, 'P2_4'] == '14C':
            df.loc[idx, '14C'] = 1
        elif df.loc[idx, 'P2_5'] == '14C':
            df.loc[idx, '14C'] = 1
        else:
            df.loc[idx, '14C'] = 0

        if df.loc[idx, 'P1_1'] == '09S':
            df.loc[idx, '09S'] = 1
        elif df.loc[idx, 'P1_2'] == '09S':
            df.loc[idx, '09S'] = 1
        elif df.loc[idx, 'P1_3'] == '09S':
            df.loc[idx, '09S'] = 1
        elif df.loc[idx, 'P1_4'] == '09S':
            df.loc[idx, '09S'] = 1
        elif df.loc[idx, 'P1_5'] == '09S':
            df.loc[idx, '09S'] = 1
        elif df.loc[idx, 'P2_1'] == '09S':
            df.loc[idx, '09S'] = 1
        elif df.loc[idx, 'P2_2'] == '09S':
            df.loc[idx, '09S'] = 1
        elif df.loc[idx, 'P2_3'] == '09S':
            df.loc[idx, '09S'] = 1
        elif df.loc[idx, 'P2_4'] == '09S':
            df.loc[idx, '09S'] = 1
        elif df.loc[idx, 'P2_5'] == '09S':
            df.loc[idx, '09S'] = 1
        else:
            df.loc[idx, '09S'] = 0

        if df.loc[idx, 'P1_1'] == '10S':
            df.loc[idx, '10S'] = 1
        elif df.loc[idx, 'P1_2'] == '10S':
            df.loc[idx, '10S'] = 1
        elif df.loc[idx, 'P1_3'] == '10S':
            df.loc[idx, '10S'] = 1
        elif df.loc[idx, 'P1_4'] == '10S':
            df.loc[idx, '10S'] = 1
        elif df.loc[idx, 'P1_5'] == '10S':
            df.loc[idx, '10S'] = 1
        elif df.loc[idx, 'P2_1'] == '10S':
            df.loc[idx, '10S'] = 1
        elif df.loc[idx, 'P2_2'] == '10S':
            df.loc[idx, '10S'] = 1
        elif df.loc[idx, 'P2_3'] == '10S':
            df.loc[idx, '10S'] = 1
        elif df.loc[idx, 'P2_4'] == '10S':
            df.loc[idx, '10S'] = 1
        elif df.loc[idx, 'P2_5'] == '10S':
            df.loc[idx, '10S'] = 1
        else:
            df.loc[idx, '10S'] = 0

        if df.loc[idx, 'P1_1'] == '11S':
            df.loc[idx, '11S'] = 1
        elif df.loc[idx, 'P1_2'] == '11S':
            df.loc[idx, '11S'] = 1
        elif df.loc[idx, 'P1_3'] == '11S':
            df.loc[idx, '11S'] = 1
        elif df.loc[idx, 'P1_4'] == '11S':
            df.loc[idx, '11S'] = 1
        elif df.loc[idx, 'P1_5'] == '11S':
            df.loc[idx, '11S'] = 1
        elif df.loc[idx, 'P2_1'] == '11S':
            df.loc[idx, '11S'] = 1
        elif df.loc[idx, 'P2_2'] == '11S':
            df.loc[idx, '11S'] = 1
        elif df.loc[idx, 'P2_3'] == '11S':
            df.loc[idx, '11S'] = 1
        elif df.loc[idx, 'P2_4'] == '11S':
            df.loc[idx, '11S'] = 1
        elif df.loc[idx, 'P2_5'] == '11S':
            df.loc[idx, '11S'] = 1
        else:
            df.loc[idx, '11S'] = 0

        if df.loc[idx, 'P1_1'] == '12S':
            df.loc[idx, '12S'] = 1
        elif df.loc[idx, 'P1_2'] == '12S':
            df.loc[idx, '12S'] = 1
        elif df.loc[idx, 'P1_3'] == '12S':
            df.loc[idx, '12S'] = 1
        elif df.loc[idx, 'P1_4'] == '12S':
            df.loc[idx, '12S'] = 1
        elif df.loc[idx, 'P1_5'] == '12S':
            df.loc[idx, '12S'] = 1
        elif df.loc[idx, 'P2_1'] == '12S':
            df.loc[idx, '12S'] = 1
        elif df.loc[idx, 'P2_2'] == '12S':
            df.loc[idx, '12S'] = 1
        elif df.loc[idx, 'P2_3'] == '12S':
            df.loc[idx, '12S'] = 1
        elif df.loc[idx, 'P2_4'] == '12S':
            df.loc[idx, '12S'] = 1
        elif df.loc[idx, 'P2_5'] == '12S':
            df.loc[idx, '12S'] = 1
        else:
            df.loc[idx, '12S'] = 0

        if df.loc[idx, 'P1_1'] == '13S':
            df.loc[idx, '13S'] = 1
        elif df.loc[idx, 'P1_2'] == '13S':
            df.loc[idx, '13S'] = 1
        elif df.loc[idx, 'P1_3'] == '13S':
            df.loc[idx, '13S'] = 1
        elif df.loc[idx, 'P1_4'] == '13S':
            df.loc[idx, '13S'] = 1
        elif df.loc[idx, 'P1_5'] == '13S':
            df.loc[idx, '13S'] = 1
        elif df.loc[idx, 'P2_1'] == '13S':
            df.loc[idx, '13S'] = 1
        elif df.loc[idx, 'P2_2'] == '13S':
            df.loc[idx, '13S'] = 1
        elif df.loc[idx, 'P2_3'] == '13S':
            df.loc[idx, '13S'] = 1
        elif df.loc[idx, 'P2_4'] == '13S':
            df.loc[idx, '13S'] = 1
        elif df.loc[idx, 'P2_5'] == '13S':
            df.loc[idx, '13S'] = 1
        else:
            df.loc[idx, '13S'] = 0

        if df.loc[idx, 'P1_1'] == '14S':
            df.loc[idx, '14S'] = 1
        elif df.loc[idx, 'P1_2'] == '14S':
            df.loc[idx, '14S'] = 1
        elif df.loc[idx, 'P1_3'] == '14S':
            df.loc[idx, '14S'] = 1
        elif df.loc[idx, 'P1_4'] == '14S':
            df.loc[idx, '14S'] = 1
        elif df.loc[idx, 'P1_5'] == '14S':
            df.loc[idx, '14S'] = 1
        elif df.loc[idx, 'P2_1'] == '14S':
            df.loc[idx, '14S'] = 1
        elif df.loc[idx, 'P2_2'] == '14S':
            df.loc[idx, '14S'] = 1
        elif df.loc[idx, 'P2_3'] == '14S':
            df.loc[idx, '14S'] = 1
        elif df.loc[idx, 'P2_4'] == '14S':
            df.loc[idx, '14S'] = 1
        elif df.loc[idx, 'P2_5'] == '14S':
            df.loc[idx, '14S'] = 1
        else:
            df.loc[idx, '14S'] = 0

        count = count + 1

    columns = ['P1_1', 'P1_2', 'P1_3', 'P1_4', 'P1_5',
               'P2_1', 'P2_2', 'P2_3', 'P2_4', 'P2_5']
    df.drop(columns, inplace=True, axis=1)

    now = datetime.datetime.now().strftime('%y%m%d_%H%M')
    filename = 'logs/training_data_%s.csv' % now
    print "\nEXPORTING %s..." % filename
    df.to_csv(filename, encoding='utf-8', index=False)

if __name__ == '__main__':
    run()
