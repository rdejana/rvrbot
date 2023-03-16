# rvrbot
Taking some Jetbot ideas to the Sphero RVR+

## Setup
I'm currently using a Raspberry Pi 3 with the RVR+.  

In order to leverage some features of the juypter ipywidgets, specially the Controller widge, a particular
install is required.  While using Anaconda worked for my Mac, it was not suppored on my pi3.  I ended up mixing conda-forge and anacoda
sourced packages until I had a working version of the Controller widget.

I'm planning on creating a dockerfile, but until then, this is the basic approach.  

Download and install the pypy Miniforge installer (see https://github.com/conda-forge/miniforge).
Once installed, create a 3.9 environment; I named mine `rvr2`.

```
# packages in environment at ~/miniforge-pypy3/envs/rvr2:
#
# Name                    Version                   Build  Channel
_openmp_mutex             4.5                       2_gnu    conda-forge
alsa-lib                  1.2.8                h4e544f5_0    conda-forge
anyio                     3.5.0            py39hd43f75c_0    anaconda
argon2-cffi               21.3.0             pyhd3eb1b0_0    anaconda
argon2-cffi-bindings      21.2.0           py39h2f4d8fa_0    anaconda
attr                      2.5.1                h4e544f5_1    conda-forge
attrs                     22.1.0           py39hd43f75c_0    anaconda
babel                     2.11.0           py39hd43f75c_0    anaconda
backcall                  0.2.0              pyhd3eb1b0_0    anaconda
beautifulsoup4            4.11.1           py39hd43f75c_0    anaconda
bleach                    4.1.0              pyhd3eb1b0_0    anaconda
brotlipy                  0.7.0           py39hfd63f10_1002    anaconda
bzip2                     1.0.8                hf897c2e_4    conda-forge
ca-certificates           2022.12.7            h4fd8a4c_0    conda-forge
certifi                   2022.12.7          pyhd8ed1ab_0    conda-forge
cffi                      1.15.1           py39h998d150_3    anaconda
charset-normalizer        2.0.4              pyhd3eb1b0_0    anaconda
cryptography              38.0.4           py39h3d58568_0    anaconda
dbus                      1.13.18              h821dc26_0    anaconda
debugpy                   1.5.1            py39h22f4aa5_0    anaconda
decorator                 5.1.1              pyhd3eb1b0_0    anaconda
defusedxml                0.7.1              pyhd3eb1b0_0    anaconda
entrypoints               0.4              py39hd43f75c_0    anaconda
expat                     2.5.0                ha18d298_0    conda-forge
fftw                      3.3.10          nompi_ha1d0423_106    conda-forge
flit-core                 3.6.0              pyhd3eb1b0_0    anaconda
font-ttf-dejavu-sans-mono 2.37                 hd3eb1b0_0    anaconda
font-ttf-inconsolata      2.001                hcb22688_0    anaconda
font-ttf-source-code-pro  2.030                hd3eb1b0_0    anaconda
font-ttf-ubuntu           0.83                 h8b1ccd4_0    anaconda
fontconfig                2.14.2               ha9a116f_0    conda-forge
fonts-anaconda            1                    h8fa9717_0    anaconda
fonts-conda-ecosystem     1                    hd3eb1b0_0    anaconda
freetype                  2.12.1               h6df46f4_0    anaconda
gettext                   0.21.1               ha18d298_0    conda-forge
glib                      2.74.1               h7866ba4_0    conda-forge
glib-tools                2.74.1               h7866ba4_0    conda-forge
gst-plugins-base          1.21.3               h8a62080_1    conda-forge
gstreamer                 1.21.3               h1f26242_1    conda-forge
icu                       70.1                 ha18d298_0    conda-forge
idna                      3.4              py39hd43f75c_0    anaconda
ipykernel                 6.15.2           py39hd43f75c_0    anaconda
ipython                   7.31.1           py39hd43f75c_1    anaconda
ipython_genutils          0.2.0                      py_1    conda-forge
ipywidgets                7.6.5              pyhd3eb1b0_1    anaconda
jack                      1.9.22               hf8b18a5_0    conda-forge
jedi                      0.18.1           py39hd43f75c_1    anaconda
jinja2                    3.1.2            py39hd43f75c_0    anaconda
jpeg                      9e                   h2f4d8fa_0    anaconda
json5                     0.9.6              pyhd3eb1b0_0    anaconda
jsonschema                4.16.0           py39hd43f75c_0    anaconda
jupyter                   1.0.0            py39h4420490_8    conda-forge
jupyter_client            7.3.4              pyhd8ed1ab_0    conda-forge
jupyter_console           6.4.3              pyhd3eb1b0_0    anaconda
jupyter_core              4.11.1           py39hd43f75c_0    anaconda
jupyter_server            1.18.1           py39hd43f75c_0    anaconda
jupyterlab                3.4.4            py39hd43f75c_0    anaconda
jupyterlab_pygments       0.1.2                      py_0    anaconda
jupyterlab_server         2.10.3             pyhd3eb1b0_1    anaconda
jupyterlab_widgets        1.0.0              pyhd3eb1b0_1    anaconda
keyutils                  1.6.1                h4e544f5_0    conda-forge
krb5                      1.19.3               h750e270_0    conda-forge
lame                      3.100                hfd63f10_0    anaconda
ld_impl_linux-aarch64     2.40                 h2d8c526_0    conda-forge
libcap                    2.66                 hbb70f59_0    conda-forge
libclang                  15.0.7          default_h3fabc39_1    conda-forge
libclang13                15.0.7          default_haf32b04_1    conda-forge
libcups                   2.3.3                h0c1ea75_2    conda-forge
libdb                     6.2.32               h419075a_1    anaconda
libedit                   3.1.20221030         h998d150_0    anaconda
libevent                  2.1.10               h4f30969_4    conda-forge
libffi                    3.4.2                h3557bc0_5    conda-forge
libflac                   1.4.2                h4de3ea5_0    conda-forge
libgcc-ng                 12.2.0              h607ecd0_19    conda-forge
libgfortran-ng            11.2.0               h6e398d7_1    anaconda
libgfortran5              11.2.0               h1234567_1    anaconda
libglib                   2.74.1               h58953e2_0    conda-forge
libgomp                   12.2.0              h607ecd0_19    conda-forge
libiconv                  1.17                 h9cdd2b7_0    conda-forge
libllvm15                 15.0.7               h87099f9_0    conda-forge
libnsl                    2.0.0                hf897c2e_0    conda-forge
libogg                    1.3.5                h2f4d8fa_1    anaconda
libopus                   1.3.1                h2f4d8fa_0    anaconda
libpng                    1.6.39               hf9034f9_0    conda-forge
libpq                     14.5                 h9991ba5_3    conda-forge
libsndfile                1.1.0                hd600fc2_1    conda-forge
libsodium                 1.0.18               hfd63f10_0    anaconda
libsqlite                 3.40.0               hf9034f9_0    conda-forge
libstdcxx-ng              12.2.0              hc13a102_19    conda-forge
libtool                   2.4.6             h419075a_1009    anaconda
libudev1                  253                  hb4cce97_0    conda-forge
libuuid                   2.32.1            hf897c2e_1000    conda-forge
libvorbis                 1.3.7                hfd63f10_0    anaconda
libxcb                    1.13              h3557bc0_1004    conda-forge
libxkbcommon              1.5.0                h4f22d97_1    conda-forge
libxml2                   2.10.3               h249b6dd_0    conda-forge
libzlib                   1.2.13               h4e544f5_4    conda-forge
lz4-c                     1.9.4                h419075a_0    anaconda
markupsafe                2.1.1            py39h2f4d8fa_0    anaconda
matplotlib-inline         0.1.6            py39hd43f75c_0    anaconda
mistune                   0.8.4           py39hfd63f10_1000    anaconda
mpg123                    1.31.2               hd600fc2_0    conda-forge
mysql-common              8.0.32               hed3ad84_0    conda-forge
mysql-libs                8.0.32               h42d7160_0    conda-forge
nbclassic                 0.4.8            py39hd43f75c_0    anaconda
nbclient                  0.5.13             pyhd8ed1ab_0    conda-forge
nbconvert                 6.4.4            py39hd43f75c_0    anaconda
nbformat                  5.5.0            py39hd43f75c_0    anaconda
ncurses                   6.3                  headf329_1    conda-forge
nest-asyncio              1.5.6            py39hd43f75c_0    anaconda
notebook                  6.4.12           py39hd43f75c_0    anaconda
notebook-shim             0.2.2            py39hd43f75c_0    anaconda
nspr                      4.35                 h4de3ea5_0    conda-forge
nss                       3.89                 hf608148_0    conda-forge
openssl                   3.1.0                hb4cce97_0    conda-forge
packaging                 22.0             py39hd43f75c_0    anaconda
pandocfilters             1.5.0              pyhd3eb1b0_0    anaconda
parso                     0.8.3              pyhd3eb1b0_0    anaconda
pcre2                     10.37                ha6b7f17_1    anaconda
pexpect                   4.8.0              pyhd3eb1b0_3    anaconda
pickleshare               0.7.5           pyhd3eb1b0_1003    anaconda
pip                       23.0.1             pyhd8ed1ab_0    conda-forge
ply                       3.11             py39hd43f75c_0    anaconda
prometheus_client         0.14.1           py39hd43f75c_0    anaconda
prompt-toolkit            3.0.20             pyhd3eb1b0_0    anaconda
prompt_toolkit            3.0.20               hd3eb1b0_0    anaconda
psutil                    5.9.0            py39h998d150_0    anaconda
pthread-stubs             0.3                  hfd63f10_1    anaconda
ptyprocess                0.7.0              pyhd3eb1b0_2    anaconda
pulseaudio                14.0                hb80cb52_11    conda-forge
pycparser                 2.21               pyhd3eb1b0_0    anaconda
pygments                  2.11.2             pyhd3eb1b0_0    anaconda
pyopenssl                 22.0.0             pyhd3eb1b0_0    anaconda
pyqt                      5.15.7           py39hd020858_3    conda-forge
pyqt5-sip                 12.11.0          py39hdcdd789_3    conda-forge
pyrsistent                0.18.0           py39h2f4d8fa_0    anaconda
pysocks                   1.7.1            py39hd43f75c_0    anaconda
python                    3.9.16          hb363c5e_0_cpython    conda-forge
python-dateutil           2.8.2              pyhd3eb1b0_0    anaconda
python-fastjsonschema     2.16.2           py39hd43f75c_0    anaconda
python_abi                3.9                      3_cp39    conda-forge
pytz                      2022.7           py39hd43f75c_0    anaconda
pyzmq                     23.2.0           py39h419075a_0    anaconda
qt-main                   5.15.6               hbd5891e_2    conda-forge
qtconsole                 5.3.2            py39hd43f75c_0    anaconda
qtpy                      2.2.0            py39hd43f75c_0    anaconda
readline                  8.1.2                h38e3740_0    conda-forge
requests                  2.28.1           py39hd43f75c_0    anaconda
send2trash                1.8.0              pyhd3eb1b0_1    anaconda
setuptools                67.6.0             pyhd8ed1ab_0    conda-forge
sip                       6.6.2            py39h419075a_0    anaconda
six                       1.16.0             pyhd3eb1b0_1    anaconda
sniffio                   1.2.0            py39hd43f75c_1    anaconda
soupsieve                 2.3.2.post1      py39hd43f75c_0    anaconda
terminado                 0.17.1           py39hd43f75c_0    anaconda
testpath                  0.6.0            py39hd43f75c_0    anaconda
tk                        8.6.12               hd8af866_0    conda-forge
toml                      0.10.2             pyhd3eb1b0_0    anaconda
tornado                   6.2              py39h998d150_0    anaconda
traitlets                 5.1.1              pyhd8ed1ab_0    conda-forge
typing-extensions         4.4.0            py39hd43f75c_0    anaconda
typing_extensions         4.4.0            py39hd43f75c_0    anaconda
tzdata                    2022g                h191b570_0    conda-forge
urllib3                   1.26.14          py39hd43f75c_0    anaconda
wcwidth                   0.2.5              pyhd3eb1b0_0    anaconda
webencodings              0.5.1            py39hd43f75c_1    anaconda
websocket-client          0.58.0           py39hd43f75c_4    anaconda
wheel                     0.40.0             pyhd8ed1ab_0    conda-forge
widgetsnbextension        3.5.2            py39hd43f75c_0    anaconda
xcb-util                  0.4.0                h4e544f5_0    conda-forge
xcb-util-image            0.4.0                h4e544f5_0    conda-forge
xcb-util-keysyms          0.4.0                h4e544f5_0    conda-forge
xcb-util-renderutil       0.3.9                h4e544f5_0    conda-forge
xcb-util-wm               0.4.1                h4e544f5_0    conda-forge
xkeyboard-config          2.38                 hb4cce97_0    conda-forge
xorg-libxau               1.0.9                h3557bc0_0    conda-forge
xorg-libxdmcp             1.1.3                h3557bc0_0    conda-forge
xz                        5.2.6                h9cdd2b7_0    conda-forge
zeromq                    4.3.4                h01db608_1    conda-forge
zlib                      1.2.13               h4e544f5_4    conda-forge
zstd                      1.5.2                hfcb3217_0    anaconda
```
sudo apt install libzmq3-dev 

pip3 install pyzmq

sudo pip3 install install PyGObject