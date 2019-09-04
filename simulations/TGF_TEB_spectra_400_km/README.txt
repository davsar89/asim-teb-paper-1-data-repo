The "data" folder contains simulated spectra of the event in the MATLAB .mat format (can be openned with MATLAB or python / scipy).

The folder "figures" contains the plots of the corresponding data.
Data can also be extracted from ".fig" files using MATLAB.

Example on how to plot, using MATLAB: 
histogram('BinEdges',data.photon.ener_grid,'BinCounts',data.photon.dnde,...
'DisplayStyle','stairs','lineStyle','-','LineWidth',1.5,'DisplayName','photons');
    
