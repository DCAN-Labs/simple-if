import pprint
import os

# pretty printing for dictionaries
pp = pprint.PrettyPrinter(indent=4)

def collect_fmaps_and_targets(paths):
    """
    Collects files with 'fmap' & '.json' in the file name along with any other 
    selected json existing in the PySimpleGUI tree object. Then creates a list
    of dictionaries with the 'fmap.json' full file paths as keys and a list of 
    the non-fmap.json jsons as a value.
    :param paths: a list of paths
    :return: a dictionary with fmap paths as keys and target scans as lists of paths
    """
    fmaps = {}
    targets = []
    pretty_json = {}  # collects only filenames
    pretty_paths = []  # collects only filenames
    for path in paths:
        if 'fmap' in path and path.endswith('.json'):
            fmaps[path] = []
            pretty_json[os.path.basename(path)] = []
        elif '.json' in path and not 'fmap' in path:
            targets.append(path)
            pretty_paths.append(os.path.basename(path))
    
    for key in fmaps.keys():
        fmaps[key] = targets

    for key in pretty_json.keys():
        pretty_json[key] = pretty_paths
    
    # TODO Remove print statements 
    print('#'*80)
    pp.pprint(pretty_json)
    return fmaps

def assign_intended_fors(fmaps_and_targets):
    """
    add call to mapping function here
    :param fmaps_and_targets: dictionary argument created via 'collect_fmaps_and_targets'
    not smart, simply maps a single intended for onto multiple target jsons. Keys are 
    intended for jsons, values are lists of target jsons.
    """
    print("Recieved:")
    pp.pprint(fmaps_and_targets)
    
    # TODO Call your intended for routine on fmaps and targets