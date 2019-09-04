import apexpy
import datetime
from geopy.distance import geodesic
import numpy as np
import scipy.io as sio


# using apexpy to get the magnetic footpoints
teb_time = datetime.datetime(2018, 9, 16, 13, 14, 45)
A = apexpy.Apex(teb_time, refh = 0)

teb_escape_alt = 45.0 # km
sat_alt = 402.5 # km
sat_lat, sat_lon = 6.281, -95.709

mlat, mlon = A.geo2apex(sat_lat, sat_lon, sat_alt) # magnetic latitude and longitude of the ISS

foot1 = A.map_to_height(sat_lat, sat_lon, sat_alt, teb_escape_alt, conjugate=False, precision=1e-10)
foot2 = A.map_to_height(sat_lat, sat_lon, sat_alt, teb_escape_alt, conjugate=True, precision=1e-10)

print('footpoint #1 (lat lon error): ', foot1)
print('footpoint #2 (lat lon error): ', foot2)

traj_lat=[]
traj_long=[]
traj_alt = []
traj_lat_2=[]
traj_long_2=[]

apex_altitude = A.get_apex(mlat) # km

print('apex altitude =', apex_altitude,' km')

# loop to get the "trajectory" (track, path) of the field line
alt_list = np.linspace(50.0,apex_altitude,2048)

for alt in alt_list:

    foot1_traj = A.map_to_height(sat_lat, sat_lon, sat_alt, teb_escape_alt, conjugate=False, precision=1e-10)
    foot2_traj = A.map_to_height(sat_lat, sat_lon, sat_alt, teb_escape_alt, conjugate=True, precision=1e-10)
    
    traj_lat.append(foot1_traj[0])
    traj_long.append(foot1_traj[1])
    traj_alt.append(alt)
    
    traj_lat_2.append(foot2_traj[0])
    traj_long_2.append(foot2_traj[1])
    
    #print(foot1_traj)


## distance to WWLLM matches
sio.savemat('trajectory.mat', {'traj_lat': traj_lat, 'traj_long': traj_long, 'traj_lat_2': traj_lat_2, 'traj_long_2': traj_long_2, 'traj_alt': traj_alt})

WWLLN_1 = (11.0844,-95.5054)
WWLLN_2 = (11.0275,-95.2907)

print('distance to WWLLN match #1 :', geodesic(foot1, WWLLN_1).km,' km')
print('distance to WWLLN match #2 :', geodesic(foot1, WWLLN_2).km,' km')
