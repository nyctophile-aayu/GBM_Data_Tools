SUCCESS CODES TO INSTALL GBM_DATA_TOOLS WITH BASEMAP


1. Download Conda from "https://www.anaconda.com/products/distribution"
2. Install Conda from "https://docs.anaconda.com/anaconda/install/index.html"
3. Download GBM_Data_Tools from "https://fermi.gsfc.nasa.gov/ssc/data/analysis/gbm/gbm_data_tools/gdt-docs/install.html"
4. Follow instructions of installation before GBM_Data_Tools[Basemap] & activate GBM environment using conda \
	python3 -m venv gbm \
	source gbm/bin/activate \
	source ~/.bashrc \
	conda create --name gbm python=3.9 numpy=1.20 \
	source activate gbm \
	source ~/.bashrc \
	conda activate gbm \
	pip3 install --upgrade pip \
	pip3 install /home/ubuntu/gbm_data_tools-1.1.1.tar.gz \
	export GEOS_DIR=/usr/local (Use following location for geos directory) \
(If you already have it on your system, just set the environment variable GEOS_DIR to point to the location of libgeos_c and geos_c.h (if libgeos_c is in /usr/local/lib and geos_c.h is in /usr/local/include, set GEOS_DIR to /usr/local). )

5. Install Dependencies of Basemap as mentioned in the link "https://matplotlib.org/basemap/users/installing.html#installation"
6. Follow below commands & install these dependencies first: \
	conda install astropy matplotlib numpy pandas scipy\
	conda install python3 \
	conda install astroid \
	conda install coverage cmake cycler cython \
	conda install flake8 netCDF4 owslib \
	conda install -c conda-forge doxygen \
	conda install proj \
	conda install proj-bin \
	conda install pillow pyparsing pyproj pyshp pytest pylint \
	conda install sphinx typing \
	conda install unittest2 \
	pip3 install pyopenssl \
	pip3 install requests[security] \
	conda install -c conda-forge basemap-data-hires \
	sudo apt-get install python-software-properties (If error comes, proceed) \
	sudo add-apt-repository ppa:ubuntugis/ppa \
	conda install geos 
7. Now, extract basemap-1.3.6 and geos-3.11.1 by following below procedure only \
	cd (Go to home) \
	tar xvzf basemap-1.3.6.tar.gz \
	cd basemap-1.3.6 \
	tar xvjf geos-3.11.2.tar.bz2 (Or, manually extract geos-3.11.1 in basemap-1.3.6) \
	cd geos-3.11.1 \
	mkdir _build \
	cd _build \
	cmake \ \
    	&nbsp;&nbsp;&nbsp;-DCMAKE_BUILD_TYPE=Release \ \
    	&nbsp;&nbsp;&nbsp;-DCMAKE_INSTALL_PREFIX=/usr/local \ \
    	&nbsp;&nbsp;&nbsp;.. \
	make \
	ctest (check success must be 100%) \
	sudo make install \
	cd - (Now, you are in basemap-1.3.6 directory) \
	cd packages \
	cd basemap_data \
	sudo apt-get install python \
	python3 -m pip install basemap-data \
	cd - (Now, you are in packages directory) \
	cd basemap_data_hires \
	python3 -m pip install basemap-data-hires \
	cd - (Now, you are in packages directory) \
	cd basemap \
	python3 -m pip install basemap-data \
	python3 -m pip install basemap-data-hires \
	python3 -m pip install basemap \
	cd (Now, you are at home)
8. Just to be sure, run following commands in the Home directory \
	python -m pip install basemap-data \
	python -m pip install basemap-data-hires \
	python -m pip install basemap \
	python \
	&nbsp;&nbsp;&nbsp;>>> from mpl_toolkits.basemap import Basemap (It shouldn't give error now, if comes then recheck the installation) \
	&nbsp;&nbsp;&nbsp;>>> exit()
9. Run examples in basemap-1.3.6 directory to test the installation of basemap \
	cd basemap-1.3.6/ \
	cd examples/ \
	python simpletest.py (It will plot single graph) \
	python run_all.py (It will plot 61 graphs to confirm the plot. Now to proceed to next graph, please close the earlier opened graphs and proceed further. In between, it may ask for Long, Lat and Location and Degree. So choose your lat, long, location and give any degree of your preference to plot the graph.)
10. Now, finally give the last shot with the Basemap \
	conda update wheel \
	sudo apt-get install git \
	pip3 install /home/ubuntu/gbm_data_tools-1.1.1.tar.gz[basemap] 
12. With this installation of GBM Data Tools is finished.

Enjoy GBM Analysis!
