import os
import glob
import datetime
import argparse
import json
import libconvert

#############################################
# USAGE: example: 
#    python convert.py taskcvt.json
#############################################
def main():
    # arg list:
    # 
    # Arguments setting read in config file
    parser = argparse.ArgumentParser()
    parser.add_argument("cfg", \
                        help="The path of candidates list in HDF format, accept WILDCARD", \
                        type=str)

    # Internalize arguments
    args = parser.parse_args()
    cfg = args.cfg
        
    # TODO: input safety check 
    s = None
    try:
        with open(cfg, 'r') as infile:
            s = json.load(infile)
    except Exception as e:
        print('Error! Message: {}'.format(str(e)))
    
    candslist = s["parameters"]["candslist"]
    hdf = s["parameters"]["hdf"]
    rej = s["parameters"]["rej"]
    
    print ("input: " + candslist + "\n" + "output: " + hdf)
    
    consumed_time = libconvert.prestocand_to_hdf(candslist, hdf, prelim_reject = rej, track = True)

    # WAHT TO DO
    print ("DONE within " + str(consumed_time.seconds) + " seconds")


if __name__ == "__main__":
    
    # Simple pickle is enough :P and no more performance warning ^_^
    import warnings
    warnings.filterwarnings("ignore")
    
    main()    
