The file AE20180916_subset.txt contains a subset of WWLLN events around the time of the ASIM TGF TEB event 180916 
(2018/9/16 13:14:44.733601 UTC)

The format for the file is:
YYYY/MM/DD, hh:mm:ss, lat, lon, res, N, Energy (Joules), Energy uncertainty (Joules)
(2018/9/16,13:14:44.136429,  18.1105,  112.7061, 06.3, 5,  246.15,  0.00)

  where :
  - Date-time is UTC
  - Lat, lon : Fractional Degrees
  - Res : the residual fit error in us (always < 30 us)
  - N : the number of stations which detected the stroke (alway >=5)
  - Energy (Joules) : RMS energy from 7 to 18 kHz in 1.3 ms sample time