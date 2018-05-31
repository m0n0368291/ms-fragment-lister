# ms-fragment-lister

## What is it?

This script will take exported mass listings from wsearch32 (a free software for mass spectrometry) and format all values so that:
- the values are rounded
- only values above 4% relative intensity are listed (this can be adjusted as needed)
- the relative intensities appear in parentheses
- the output is a CSV file


## How to use

Put the exported mass listings in the same folder as ``fragment-lister.py`` and run the script.

Your Python installation must have pandas installed and the filename must end on ``.D.txt``. The script will work through **all** exported mass listings and produce one CSV output for every mass listing.
