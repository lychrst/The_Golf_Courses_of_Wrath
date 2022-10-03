
# The Golf Courses of Wrath:  
Modeling Water Usage Under Drought Conditions

Author: Chris Lyons, October 2022

![Mead](/hydro2/Drought-before-after.jpg?raw=true)
## Badges  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)  


# Table of contents  
1. [Introduction](#introduction)  
The reappearance of [hunger stones in European rivers](https://www.businessinsider.com/centuries-old-hunger-stones-reappear-as-european-rivers-run-dry-2022-8?op=1), [human remains dumped in Lake Mead](https://abcnews.go.com/US/5th-set-human-remains-found-receding-lake-mead/story?id=88512428), [a sunken Nazi fleet](https://www.businessinsider.com/photos-europes-drought-exposes-nazi-fleet-sunk-world-war-ii-2022-8), and [the submerged 14th century Mesta bridge](https://www.reuters.com/world/europe/hitting-rock-bottom-drought-heat-drain-spanish-reservoirs-2022-08-10/) are a few of the stories that have appeared in 2022.  The factor common to them all is the depletion of water reserves, a situation that has huge implications for both industry and quality / existence of life. 

   
   
    The economic consequences due to a lack of water availability can be considerable.  As of [August 30, 2022](https://drought.unl.edu/archive/AgInDrought/AgInDrought_20220830.pdf), the USDA reports that 51% of barley, 28% of corn, 47% of cotton, 41% of rice, 75% of sorghum, 21% of soybean, 20% of sunflower, 40% of durum wheat, 20% of spring wheat, 53% of winter wheat, 41% of hay, 44% of alfalfa, 26% of hogs, 56% of cattle, 44% of milk cows, and 57% of sheep are grown in areas affected by drought. The [costs are in the billions](https://www.ncei.noaa.gov/access/billions/mapping) and this is during a year when water remains in US reservoirs.  It is not just agriculture and livestock that faces problems with water shortages.  According to a 2013 survey conducted by Standard & Poors, buisinesses in the energy, utility, consumer staples, consumer discretionary, materials, industrial, health care and information technology sectors [all reported at least some concerns about water-related risk](https://www.brookings.edu/research/in-times-of-drought-nine-economic-facts-about-water-in-the-united-states/).  In short, water use is one of the most pressing issues the US and the world faces. 
    
    This project aims to help address the issue of water consumption by doing the following actions:
    *  Compile data about water consumption, weather information, and other factors such as demographics from reliable sources.   
    *    Model and analyze said data in order to determine what county or state-level cofactors have an impact on water consumption. National-level data will be used in the linear regression analysis in order to provide more reliable statistics.
    *  Tabulate the amount of water withdrawn and consumed from the Colorado River Basin for domestic and comercial purposes and compare that number with measures of water availability such as reservoir volumes and ground water estimates.
    * Attempt to involve other people capable of being objective data analysts to help improve the models and expand the analysis to other river basins.

2. [The Data](#paragraph1)  
Five sources of data have been used for this analysis.  [Estimated Use of Water in the United States County-Level Data for 2015 (version 2.0)](https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8), a part of U.S. Geological Survey's (USGS's) National Water Use Science Project, was used as a source for water withdraw and consumption.     The data is released every 5 years and, as of Aug 2022, the [2015 dataset was the most recent one published](https://water.usgs.gov/watuse/data/).  It contained information about domestic, irrigation, thermoelectric power, industrial, mining, livestock, and aquaculture water-use. 
 [National Oceanic and Atmospheric Administration (NOAA)](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/) was used as a source for 2015 weather data, including precipitation, cooling and heating degree days, drought indexes such as the Palmer Hydrological Drought Index, and temperature values such as maximum temperature.  [OpenIntro.org](https://www.openintro.org/), an educational nonprofit, was used as a source for [census data](https://www.openintro.org/data/index.php?data=county) including poverty, homeownership, multi-unit housing percentage, unemployment rate, and metro area.  The non-profit Lincoln Institute of Land Policy [provided acess to a csv](https://coloradoriverbasin-lincolninstitute.hub.arcgis.com/) that contained the counties which use water from the Colorado River as well as the reservoirs that are a part of the basin.  The fifth source was the [U. S. Bureau of Reclamation](https://www.usbr.gov/uc/water/hydrodata/).  They provided access to reservoir water storage data.
    
3. [Linear Regression Analyses](#paragraph2)  
The two USGS categories analyzed were golf course consumption and domestic withdraw.  Due to the strength of the correlation between population and water use, domestic was bifurcated into net and per capita withdraw categories.
    1. [Golf Water Consumption](#subparagraph1)  
    The persistence of non-normal residuals had an impact on the analysis which led to the log-scaling of acreage and consumptive use of water.    None of the weather variables required log scalling as they were already close to normal distributions.  Precipitation didn't have much impact on the model and was dropped.  For each increase of 1% in acreage, an associated increase of about 0.95% in water consumption was seen.  A one degree change in max temperature was associated with a 2.36% increase in the consumptive use of water and a one unit increase in PHDI was associated with 12% decrease in consumptive use.   The probablity of Jarque Bera was 3.71e-27 which was a significant improvement from where the model had been.  R-squared was .747. Standardization indicated that acreage was the most important variable, followed by PHDI and maximum temperature.
    ![Golf Fitted](/hydro2/Fitted_Golf.png?raw=true)
    1.   [Net Domestic Withdraw](#subparagraph1)    
    Population was the only factor that appeared to matter in the net domestic model. The high correlation between total population and total water withdraw was aleady seen in the correlation table (.959%) and linear regression only reconfirmed its importance.  Maricopa County was dropped from the chosen model.  While Maricopa County didn't have the highest per capita water consumption, the fact that it had a high per capita water consumption *and* a high population meant that it had a large impact and was an outlier.   R-squared was 94.7% which meant 94.7% and the expected amount of domestic water withdraw per person was 79.9 gallons per day.  Both results were statistically significant.  The model's Jarque-Bera probability was 0.00 which meant that the residuals did not belong to a normal distribution.  Log scaling did not solve the problem. The Mean Absolute Error was 1.82 and the Mean Squared Error was 6.21.
    ![Net Domestic](/hydro2/Net_Domestic_Regression_Line.png?raw=true)
    1. [Per Capita Withdraw](#subparagraph1)
    The variables chosen for the per capita model were irrigation with surface water (IR-WSWFr), maximum temperature, PHDI, precipitation, unemployment rate, multi-unit percentage, and metro.  These were chosen because they didn't result in multicollinearity, they contributed to the R-squared of the model, and they were statistically significant.  The coefficient of determination (R-squared) of the chosen model was at 25.8%, which was a significant improvement from where the model started at (15.1% without outliers), but was still low-powered.  Non-normal residuals remained an issue throughout the models development and could not be solved by log scaling. The mean absolute error was at 17.6 gallons per person and the mean sqaured error was 27.3.   
The Y-intercept for the mulitple linear regression model when standardized was 83.7 gallons. One standard deviation of each of the following variables was associated with its corresponding amount of gallon per person domestic water withdraw:


        * IR-WSWFr       ................................................     9.58
        * Max_temp           ................................................        8.01
        * PHDI                  .........................................................      -6.04
        * Precip                  .......................................................      -5.68
        * unemployment_rate         ............................   -4.13    
        * multi_unit             .................................................   -2.59
        * metro_yes          ................................................   -2.49

        Positive values indicate more water withdraw and negative values indicate less water withdraw.  With the exception of irrigation with surface water, all of the most important varaibles were weather related.  Unemployment was next.  Multi-unit and metro living were significantly less important than weather in this model. 

        ![Per Capita](/hydro2/2000_Facebook_Prophet_Forecast.png?raw=true)

4. [Facebook Prophet Forcasting](#paragraph2)
 
    According to a csv downloaded from the Lincoln Institute of Land Policy, the sources of water for the Colorado River Basin were the lakes Havasu, Mohave, Mead, Powell, Vallecito, and Nighthourse, the reservoirs Navajo, McPhee, Ridgway, Crystal, Morrow Point, Blue Mesa, Taylor Park, Flaming Gorge, Fontenelle, Starvation, Strawberry, and Scofield, the Morelos Dam Diversion, Imperial Diversion Dam, Granby Dam, Heron Dam, Headgate Rock Diversion, Laguna Diversion, Palo Verde, Senator Wash, Jordanelle, Wilard Bay, and Pineview. The US Bureau of Reclamaition (USBR) had storage data for every location except for Senator Wash, Palo Verde, Headgate Rock Diversion, Imperial Diversion Dam, and Morelos Dam Diversion. Data for the rest of the reservoirs were downloaded and compiled into a dataset.    Null values existed because some of the reservoirs were older than others and the nulls were converted to zeros.  The data for the reservoirs were downloaded on September 21, of 2022 and therefore was the last date contained within the dataset. At that time, the combined total of all of the reservoirs was 7,081,513 Mgal of water.
    
    The program Facebook Prophet is an open source data forecasting tool used to analyze time series data.  It is sensitive to the data given to it so if only data from 2000 onward was given, the forecast would have a sharper downward slope than if all of the data since 1937 were given.  In order to be conservative and avoid any accusations of cherry-picking, one of the forecasts used all of the available data.  That forecast had a yearly decline of -152,800 Mgal.  While the r-squared of the train portion of the forecast was high at .976, it failed when it was tested against all of the values since 2021.  It had forecasted a value of 8,324,972 Mgal by 2030 and the Colorado River Basin was already well below that number.  In short, the forecast was too conservative.  The second forecast performed better.  It forecasted a yearly decline of -790,832 Mgal, had a .95 r-squared in the train portion, which dropped to .44 once it was tested with the data from 2021 onwards, and had a mean absolute error of 291,264 Mgal in the train portion and a 563,561 Mgal error in the test portion.  It too erred by being too conservative in its Sep 21, 2022 forecast. 7,872,734 Mgals had been forecasted.  In both models, the lower bound crossed the zero mark by 2030.  In the second one, the lower bound crossed the zero mark in 2025.  If the forecast using data from 2000 onward is accurate, all of the water in Colorado River Basin reservoirs will be gone in ten years - (10)* (-790,832) + 7,081,513 = -826,707. 
    ![Facebook Prophet](/hydro2/2000_Facebook_Prophet_Forecast.png?raw=true)

5. [2015  Colorado River Basin Water Usage Versus Reservoir and Aquifer Depletion](#subparagraph1)  
 In order to provide an overall picture of the hyrdologocial cycle for the Colorado River Basin, estimates for groundwater and reservoir depletion and USGS water use categories were compiled and compared to one another.  When available, consumption was used for the USGS categories.  Otherwise withdraw was used.  Agriculture, golf courses, and power plants all had consumption as a categorical option.   Water withdraw had to be used for all other categories.  The 2000 forecast slope was used for reservoir depletion as it was more accurate than the 1937 version. [Groundwater depletion during drought threatens future water security of the Colorado River Basin](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014GL061055) (Castle, Stephanie L. et. al., *Geophysical Research Letters*, July 2014) was used as a source for the depletion of groundwater.
    
    
    The combined total of reservoir and groundwater depletion was 2,270,195 Mgal.  The only USGS category that had more water use than that was agriculture at 3,491,549 Mgal.  Domestic was comparible at 1,617,990 Mgal, hence both agriculture and domestic use categories have to be areas of focus when it comes to discussing how to reduce overall water demand.  If one ignored groundwater, the amount needed to be reduced was still well beyond the capacity of any other category to make up for the shortfall.
    ![Water_Depletion_Use](/hydro2/Water_Depletion_versus_Water_Use.png?raw=true)

## License  

[MIT](https://choosealicense.com/licenses/mit/)
