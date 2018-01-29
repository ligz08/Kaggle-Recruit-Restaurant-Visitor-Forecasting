# Install XGBoost on Windows
Official guide form XGboost:
https://xgboost.readthedocs.io/en/latest/build.html#building-on-windows
(which is not very detailed)

To build XGBoost on Windows, you need:
- A Python installation such as Anaconda
- [Git for Windows](http://gitforwindows.org/)
- MinGW

Here are step-by-step guides:

## Install Anaconda
Refer to Conda's guide here: https://conda.io/docs/user-guide/install/windows.html

## Install Git for Windows
Go here: http://gitforwindows.org/

## Install MinGW
Note: MinGW and MinGW-W64 are different things.
Since my Windows is 64-bit, it needs to run MinGW-W64.

For MinGW, go to http://www.mingw.org/ or refer to [this video](https://www.youtube.com/watch?v=xuQL_BZydS0).

The instructions below works for installing MinGW-W64.

### Install MinGW-W64 for 64-bit Windows 10
1. Go to https://mingw-w64.org/, then `Downloads` page.
2. Follow the `MingW-W64-builds` link
to download [the installer from Sourceforge](http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe/download)
3. Run the installer. It should look like this: 
![](https://blog.kitware.com/wp-content/uploads/2016/05/Fig_Mingw-w64_PopUP_2-1024x746.png)
4. In 'Settings', choose `Architecture` to be `x86_64`
![](https://waterprogramming.files.wordpress.com/2015/02/mingw-64-installation.png)  
5. Locate the `bin` folder in your MinGW-W64 installation. It should look like this:
```
C:\Program Files\mingw-w64\x86_64-5.3.0-posix-seh-rt_v4-rev0\mingw64\bin
```
Add this path to your `Path` environment variable.

6. Open Git Bash

7. Double check the location of `mingw32-make` by
```bash
$ which mingw32-make
```
Expect
```bash
/c/Program Files/mingw-w64/x86_64-5.3.0-posix-seh-rt_v4-rev0/mingw64/bin/mingw32-make
```
If not correct,
check other `mingw32-make` executables you might have on the computer,
and if `Path` environment variable has been updated.

8. (Optional) Make an alias for `mingw32-make`: `make`
```bash
$ alias make='mingw32-make'
```


## Install XGBoost
### Clone XGBoost source code
Open Git Bash,
go to a path you want the `xgboost` directory to be cloned,
and run:
```bash
$ git clone --recursive https://github.com/dmlc/xgboost
```
Then
```bash
$ git submodule init
$ git submodule update
```

### Build with MinGW-W64
```bash
$ cd xgboost
$ cp make/mingw64.mk config.mk
$ make -j4
```
Note: if you haven't set `make` as alias of `mingw32-make`,
use `mingw32-make` instead of `make` above.

### Install Python package `xgboost`
(Ref [here](https://xgboost.readthedocs.io/en/latest/build.html#python-package-installation))
Go to the `python-package` directory under cloned `xgboost`
```bash
$ cd python-package
$ sudo python setup.py install
```

## Build XGBoost with GPU Support
### Install Visual Studio
VS is needed before installing CUDA. Go to https://www.visualstudio.com/.
Visual Studio Community (the free one) should be fine.

### Install CUDA
Refer to [CUDA Installation Guide for Windows](http://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html#compiling-examples__valid-results-from-sample-cuda-bandwidthtest-program)
1. Verify CUDA-capable graphics card at http://developer.nvidia.com/cuda-gpus

2. Download CUDA installer at http://developer.nvidia.com/cuda-downloads

3. Follow guide