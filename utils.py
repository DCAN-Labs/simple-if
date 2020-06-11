import pprint
import os

# pretty printing for dictionaries
pp = pprint.PrettyPrinter(indent=4)

def collect_fmaps_and_targets(paths):
    """
    Collects files with 'fmap' & '.json' in the file name along with any other
    selected json existing in the PySimpleGUI tree object. Then creates a list
    of dictionaries with the 'fmap.json' full file paths as keys and a list of
    relative paths to non-fmap niftis as a value.
    :param paths: a list of paths
    :return: a dictionary with fmap paths as keys and target scans as lists of paths
    """
    fmaps = {}         # Must have full paths to jsons.
    targets = []       # Must (per BIDS) have relative paths to nifti.
    pretty_json = {}   # collects only filenames
    pretty_paths = []  # collects only filenames
    for path in paths:
        if 'fmap' in path:
            if (path.endswith('.nii') or path.endswith('.gz')):
                json = switch_from_nifti_to_json(path)
            elif path.endswith('.json'):
                json = path
            else:
                print('Error: unknown file extenion for path: %s' % path)
                continue

            fmaps[json] = []
            pretty_json[os.path.basename(json)] = []

        elif ('.nii' in path or '.gz' in path) and not 'fmap' in path:
            mode_path = os.path.dirname(path)
            mode = os.path.basename(mode_path)
            if mode in [ 'func', 'anat' ]:
                session_path = os.path.dirname(mode_path)
            else:
                print('Error: unrecognized mode, %s, in path %s' % (mode, path))
                continue

            if 'ses-' in session_path:
                subject_path = os.path.dirname(session_path)
            else:
                subject_path = session_path

            targets.append(os.path.relpath(path, subject_path))
            pretty_paths.append(os.path.basename(path))

    for key in fmaps.keys():
        fmaps[key] = targets

    for key in pretty_json.keys():
        pretty_json[key] = pretty_paths

    # TODO Remove print statements
    print('#'*80)
    #pp.pprint(pretty_json)
    pp.pprint(fmaps)
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

def switch_from_nifti_to_json(nifti):
    return nifti.replace('.nii', '.json').replace('.gz', '')

