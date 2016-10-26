#!/bin/bash

echo "removing public domain roms (PD)"
rm *\(PD\)*

echo "removing alternate dumps [a]"
rm *\[a*

echo "removing bad dumps [b]"
rm *\[b*

echo "removing fixed dumps [f]"
rm *\[f*

echo "removing hacked roms [h]/(Hack)"
rm *\[h*
rm *Hack\)*

echo "removing overdumped roms [o]"
rm *\[o*

echo "removing pirate roms [p]"
rm *\[p*

echo "removing trained roms [t]"
rm *\[t*

echo "removing translated roms [T]"
rm *\[T*
