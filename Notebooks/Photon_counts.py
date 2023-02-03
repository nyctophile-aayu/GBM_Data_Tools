# This notebook is useful to calculate the photon counts for a selected time bin
# and for a selected time bin. For each time bin, 128 energy channels are distributed
# for a selected .pha or .fits or .pha2 file. 


# Import modules
from astropy.io import fits, pha, pha2

# Import .pha or .pha2 or .fits file
a = fits.open('file_name')
a.info()

counts = a['spectrum'].data['counts']
len(counts)

counts[0]
len(counts[0])

a['spectrum'].data['time']
a['ebounds'].data

time = a['spectrum'].data['time']
a['primary'].header

TT = a['primary'].header['TRIGTIME']

time -= TT

time

mask - t = (time > 0) & (time < 10)
counts.[mask - t]
mask[]

