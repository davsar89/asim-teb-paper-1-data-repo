The "data" folder contains simulated lightcurves of the event in the MATLAB .mat format (can be openned with MATLAB or python / scipy).
Each file is named " lightcurves_beaming_beam_AAA_sigmaT_BBB.mat " ,
 - where AAA is the sigma of the gaussian angular distribution of the source TGF (in degrees).
 - and BBB is the sigma of the gaussian time distribution of the source TGF (in milliseconds).

The folder "figures" contains the plots of the corresponding data. Data can also be extracted from ".fig" files using MATLAB.

Example on how to plot, using MATLAB: 
histogram('BinEdges',simu_lightcurves.time_bins,'BinCounts',simu_lightcurves.sum,...
'DisplayStyle','stairs','lineStyle','-','LineWidth',1.5,'DisplayName','simulation: sum');

lightcurve_opposite.mat : simulated lightcurve when the source TGF (producting the TEB) is assumed in the opposite (south) hemisphere
    
