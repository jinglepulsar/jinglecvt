import pandas as pd
import sifting
import os
import glob
import datetime
import argparse
import tables
import json

def prestocand_to_hdf(cand_path, hdf_path, prelim_reject = False, track = True):
    # This module require presto sifting module to run.

    # Timing starts
    start = datetime.datetime.now()
    # Do the job
    candlist = sifting.read_candidates(glob.glob(cand_path), prelim_reject, track)
    # Timeing
    end = datetime.datetime.now()
    time_consummed = end-start

    df = pd.DataFrame([[x.path, x.filename, x.candnum, x.sigma, x.numharm, x.ipow_det, x.cpow, \
                        x.r, x.f, x.z, x.T, x.p, x.DMstr, x.DM, x.harm_pows, x.harm_amps, x.snr, \
                        x.hits, x.note] for x in candlist], \
                    columns = ['path', 'filename', 'candnum', 'sigma', 'numharm', 'ipow_det', \
                            'cpow', 'r', 'f', 'z', 'T', 'p', 'DMstr', 'DM', 'harm_pows', 'harm_amps', \
                            'snr', 'hits', 'note'])
    # ImportError if no PyTables
    df.to_hdf(hdf_path, key='df', mode='w')
    
    return time_consummed # TODO: return conv_status #tuple (total_cand_num, file_num, cand_num etc) 