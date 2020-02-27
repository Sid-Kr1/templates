#!/usr/bin/env python3

__script_name__ = "NAME ME"
__version__ = "0.0.1"
__maintainer__ = "Sid Krishnan"
__email__ = ""
__status__ = "Development"

import argparse
# import concurrent.futures  # for concurrent.futures.ProcessPoolExecutor()
# import errno
import sys
# from pathlib import Path  # Python3 libs for os.path
# from shutil import rmtree
from subprocess import PIPE, Popen

# import dask.dataframe as dd
# import numpy as np
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# np.seterr(all='raise')


def run_command(cmd):
    """Run a command and take care of stdout

    expects 'cmd' to be a string like "foo -b ar"

    returns (stdout, stderr)
    """
    p = Popen(cmd.split(" "), stdout=PIPE)
    return p.communicate()


def do_work(args):
    """ Main wrapper"""

    """
    # run something external using a thread pool
    pool = Pool(6)
    cmds = ['ls -l', 'ls -alh', 'ps -ef']
    print(pool.map(run_command, cmds))


    Need to be updated to use concurrent.futures.processpoolexectutor
    """

    """
    # parse a file
    try:
        with open(args.filename, "r") as fh:
            for line in fh:
                print(line)
    except:
        print(f"Error opening file:\" {args.filename} \" {sys.exc_info()[0]}")
        raise
    """

    """
    fig = plt.figure()
    # Needs to be updated for ploty
    
    #-----
    # make a 3d plot
    # Needs to be updated for ploty

    #-----
    # make a 2d plot
    # Needs to be updated for ploty

    #-----
    # show figure
    # Needs to be updated for ploty
    # or save figure
    # Needs to be updated for ploty

    #-----
    # clean up!
    # Needs to be updated for ploty
    """

    return 0


###############################################################################

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Input file to parse")
    # parser.add_argument('positional_arg', help="Required")
    # parser.add_argument('positional_arg2', type=int, help="Integer argument")
    # parser.add_argument('positional_arg3', nargs='+', help="Multiple values")
    # parser.add_argument('-X', '--optional_X', action="store_true", default=False, help="flag")

    # -------------------------------------------------
    # get and check options

    #### not sure if the below section is required?

    #### I think it can be handled with just arg parser

    args = None
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    elif (
        sys.argv[1] == "-v"
        or sys.argv[1] == "--v"
        or sys.argv[1] == "-version"
        or sys.argv[1] == "--version"
    ):
        print(f"{__script_name__}: version: {__version__}")
        sys.exit(0)
    elif (
        sys.argv[1] == "-h"
        or sys.argv[1] == "--h"
        or sys.argv[1] == "-help"
        or sys.argv[1] == "--help"
    ):
        parser.print_help()
        sys.exit(0)
    else:
        args = parser.parse_args()

    try:
        if __profiling__:
            import cProfile

            cProfile.run("do_work(args)", "prof")
            ##########################################
            ##########################################
            # Use this in python console!
            # import pstats
            # p = pstats.Stats('prof')
            # p.sort_stats('cumulative').print_stats(10)
            # p.sort_stats('time').print_stats(10)
            ##########################################
            ##########################################
        else:
            do_work(args)
    except:
        print(f"Unexpected error: {sys.exc_info()[0]}")
        raise
