# romclean
An incredibly naïve set of scripts to tidy up romsets -- attempts to convert a Goodset/TOSEC/No-intro romset to a 1G1R set.

## Installation
  - Clone the scripts into your homedir/bin
  - Make sure that ${HOME}/bin is in your $PATH.
  - You may remove the file extensions if you wish to make the command names cleaner.
  
## Usage
  - cd to the rom directory you want to clean -- this should be a directory containing only roms.
  - **back up this directory** -- these scripts are destructive by design and do not create backups.
  - run "romclean-pass1.sh" -- this indiscriminately deletes all roms containing specific Goodtools tags in their filenames:
    - (PD), [a], [b], [f], [h], (Hack), [o], [p], [t], [T]
  - run "romclean-pass2.py" -- this does not delete anything, as it most likely requires user intervention:
    - This script creates three files: 
      - keep.lis, a file of all the roms to keep based on the heuristics (purely informational)
      - kill.lis, a file of all the roms to kill based on the heuristics
      - error.lis, a file of all the roms that the script couldn't figure out what to do with.
    - Before running pass3, you'll need to edit the error.lis file to ensure it only contains roms you want to delete.
    - You may wish to double check kill.lis to make sure it's not overzealous -- again, make sure it only contains roms you want to delete.
    - The heuristics are:
      - Tier 1: prefer U > UE/EU > UJ/JU > W > E > J.
      - Tier 2: prefer [!] over non-[!].
      - If tiers 1 and 2 provided a list with more than one entry, add all to the error.lis file for the user to figure out.
    - The script is fairly stupid on filename matching -- it splits on the first ., [, or ( encountered in the filename and uses that a a key -- so that "M.A.S.H." and "M.U.L.E" and "M.U.S.C.L.E." all end up matching the key "M", adding them all to the error.lis.  A minor hiccup that I'm not going to fix. 
  - Finally, run "romclean-pass3.sh", which deletes all roms listed in both kill.lis and error.lis.
  - You can then delete the .lis files.

## Support
I will provide no support or bugfixes for these scripts.  They're ugly and fragile and destructive.  Use them at your own risk.

## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
