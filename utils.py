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
        if 'fmap' in path and (path.endswith('.nii') or path.endswith('.gz')):
            fmaps[path] = []
            pretty_json[os.path.basename(path)] = []
        elif ('.nii' in path or '.gz' in path) and not 'fmap' in path:
            targets.append(path)
            pretty_paths.append(os.path.basename(path))
    
    # now we hand over the paths to the json's not the .nii or .nii.gz files by simply replacing all
    # file extensions w/ .json
    for key in fmaps.keys():
        fmaps[key] = targets

    for key in pretty_json.keys():
        pretty_json[key] = pretty_paths
    
    # TODO Remove print statements 
    print('#'*80)
    pp.pprint(pretty_json)
    return switch_from_nifti_to_json(fmaps)

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

def switch_from_nifti_to_json(dictionary_object):
    new_json_dict = {}
    for k, v in dictionary_object.items():
        new_target_jsons = []
        for nifti in v:
            new_target_jsons.append(nifti.replace('.nii', '.json').replace('.gz', ''))
        new_json_dict[k.replace('.nii', '.json').replace('.gz', '')] = new_target_jsons
    return new_json_dict