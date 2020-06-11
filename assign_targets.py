import os
import json

def add_to_intendedfor_fields(fmaps_and_targets):
    """
    Input is a dict for which keys are full paths to .json files, and values
    are lists of relative paths of niftis.
    Loops through jsons and adds the list of niftis to the "IntendedFor" field.
     - If there is no "IntendedFor" field in the json, it is added.
    TODO: If there is no json, need to make one or throw error or something.
          That part is no longer known by the caller.
    :param: fmaps_and_targets
    :return: none.
    """
    for fmap_json in fmaps_and_targets.keys():
        # Add targets to each json.
        add_to_intendedfor_field(fmap_json, fmaps_and_targets[fmap_json])

def add_to_intendedfor_field(fmap_json, func_paths):

    if isinstance(func_paths, list):

        print('Adding these funcs for IntendedFor field of %s:\n\t%s' % (fmap_json, func_paths))

        with open(fmap_json) as j:
            json_data = json.load(j)

        # Dictionary may or may not already have the field.
        prev_func_paths = json_data.get("IntendedFor", [])

        # Merge the 2 lists as a set (to keep only 1 copy of each value).
        new_paths = set(prev_func_paths)
        new_paths.update(func_paths)

        # json won't know about sets, so back to the list.
        json_data["IntendedFor"] = list(new_paths)

        with open(fmap_json, mode='w', encoding='UTF-8') as j:
            json.dump(json_data, j, indent=2)

    else:
        print('ERROR: func_paths must be a *list* of relative paths of functional files.')

