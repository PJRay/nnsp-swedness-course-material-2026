# NNSP-Sweness course material 2026
Course materials for the NNSP-Swedness neutron scattering school held in Lund in September-October 2026.

This repository will mostly hold the simulation exercise materials, that will be used during the e-learning segments of the course. 
The students will be told to run specific `git clone` commands to fetch folders with content to their VISA instances during the exercises. 
For example, to use the simple powder diffractometer in a folder called `workdir`, run the following commands: 

```bash
cd
mkdir -p workdir
cd workdir
git clone --no-checkout https://github.com/PJRay/nnsp-sweness-course-material-2026.git
cd nnsp-sweness-course-material-2026
git sparse-checkout set sim-exercises/SimplePowderDiffractometer
git checkout master
cd sim-exercises/SimplePowderDiffractometer
```
