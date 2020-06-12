# Intended For GUI
This gui exists to provide a user with a browsable interface to select fmaps
for use as intended for objects with other bids jsons.
# Requirements
- pysimplegui
- python3-tk

Note: At the time of this writing python3-tk must be installed via command line
```bash
sudo apt-get install python3-tk
```

Note: There may be issues with running this project on python > 3.6 according to 
the documentation for pysimpleGUI.

# Usage
Clone repository: `git clone git@gitlab.com:Fair_lab/intendedforgui.git`
Launch via `python3 intended_for_gui.py`

![folder_browser_window](images/folder_browser.png)

Next browse to the desired subject/session folder you wish to add fieldmaps to the intended for bids option.
Choose the desired scan and select `open`.
![browsing_folders](images/browsing_folders.png)

After you've selected the correct scan/session you can inspect the folder for your nifti images.  
Next, select the fmap(s) you wish to assign to your other mri scan types, then hold ctrl and click on the nifti's that you 
intend your field maps for.

![selecting_images](images/selecting_images.png)

And press the `Assign IntendedFor` button to assign the fieldmaps to the images you've selected.

That's it.
