
# The Golf Courses of Wrath:  
## Modeling Water Usage Under Drought Conditions

Author: Chris Lyons, October 2022

![Mead](/images/Drought-before-after.jpg?raw=true)
## Badges  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)  


### Repo Contents
- [The Golf Courses of Wrath Notebook](https://github.com/lychrst/The_Golf_Courses_of_Wrath/blob/main/The_Golf_Courses_of_Wrath.ipynb)
- [Up-to-Date Reservoir Forecasting](https://github.com/lychrst/The_Golf_Courses_of_Wrath/blob/main/Up-to-Date_Reservoir_Forecasting.ipynb)
- [Definitions](https://github.com/lychrst/The_Golf_Courses_of_Wrath/blob/main/Definitions.ipynb)
- [Data Loading, Exploration, and Cleaning](https://github.com/lychrst/The_Golf_Courses_of_Wrath/blob/main/Data_Loading_Exploration_and_Cleaning.ipynb)
- [Model Development](https://github.com/lychrst/The_Golf_Courses_of_Wrath/blob/main/Water_Withdraw_and_Consumption_Model_Development.ipynb)
- [Functions](https://github.com/lychrst/The_Golf_Courses_of_Wrath/blob/main/src/functions.py)
- [References](https://github.com/lychrst/The_Golf_Courses_of_Wrath/tree/main/references)
- [Video Presentation](https://vimeo.com/756490938)



### Table of Contents  
- [Introduction](#introduction)
- [Data](#data)
- [Linear Regression Analyses](#linear-regression-analyses)    
     -  [Golf Water Consumption](#golf-water-consumption)
     -  [Net Domestic Withdraw](#net-domestic-withdraw)
     - [Per Capita Withdraw](#per-capita-withdraw)
- [Facebook Prophet Forecasting](#facebook-prophet-forecasting)
- [2015 Colorado River Basin Water Usage Versus Reservoir and Aquifer Depletion](#2015-colorado-river-basin-water-usage-versus-reservoir-and-aquifer-depletion)
- [Conclusions](#conclusions)
- [Next Steps](#next-steps)

##  Introduction

The reappearance of [hunger stones in European rivers](https://www.businessinsider.com/centuries-old-hunger-stones-reappear-as-european-rivers-run-dry-2022-8?op=1), [human remains dumped in Lake Mead](https://abcnews.go.com/US/5th-set-human-remains-found-receding-lake-mead/story?id=88512428), [a sunken Nazi fleet](https://www.businessinsider.com/photos-europes-drought-exposes-nazi-fleet-sunk-world-war-ii-2022-8), and [the submerged 14th century Mesta bridge](https://www.reuters.com/world/europe/hitting-rock-bottom-drought-heat-drain-spanish-reservoirs-2022-08-10/) are a few of the stories that have appeared in 2022.  The factor common to them all is the depletion of water reserves, a situation that has huge implications for both industry and quality / existence of life.  

In one of his daily press conferences, Mexican president Andres Manuel Lopez Obrador (AMLO) announced ["...it's to say that we won’t produce beer in the north -- that’s over.  If they want to keep producing beer, increasing production, then all the support for the south or southeast.”](https://www.bloomberg.com/news/articles/2022-08-08/mexico-should-stop-making-beer-in-north-on-drought-amlo-says). One of the companies that may have to stop production in Mexico is [Heineken, NV.](https://www.theheinekencompany.com/investors) which has facilities in Monterrey.  Other examples of industries directly impacted by the depletion of water reserves include [lithium mining](https://eandt.theiet.org/content/articles/2019/08/lithium-firms-are-depleting-vital-water-supplies-in-chile-according-to-et-analysis/), [agriculture](https://news.sky.com/story/italy-looming-agricultural-catastrophe-as-saltwater-from-adriatic-damages-crops-12642432), [livestock](https://thehill.com/policy/equilibrium-sustainability/3602717-dried-up-texas-cattle-industry-faces-existential-crisis-from-historic-drought/), and even [chemical refining](https://www.reuters.com/business/energy/shell-cuts-capacity-german-rhineland-refinery-2022-08-18/). Local residents are also negatively impacted. [In the case of more than 100 towns in France](https://www.euronews.com/my-europe/2022/08/05/more-than-100-french-towns-without-drinking-water-amid-historic-drought), residents are forced to use water trucked in from other regions as "there is nothing left in the pipes".  If sustained, such conditions are likely to greatly reduce an individual's home equity as people tend to avoid buying homes that [don't have access to central plumbing](https://www.euronews.com/green/2022/08/04/heres-what-its-like-living-through-europes-driest-summer-in-memory). This, in turn, is likely to have negative impacts on the real estate and retail industries of the affected regions. Tourism may also be adversely impacted.

The economic consequences due to a lack of water availability can be considerable.  As of [August 30, 2022](https://drought.unl.edu/archive/AgInDrought/AgInDrought_20220830.pdf), the USDA reports that 51% of barley, 28% of corn, 47% of cotton, 41% of rice, 75% of sorghum, 21% of soybean, 20% of sunflower, 40% of durum wheat, 20% of spring wheat, 53% of winter wheat, 41% of hay, 44% of alfalfa, 26% of hogs, 56% of cattle, 44% of milk cows, and 57% of sheep are grown in areas affected by drought. The [costs are in the billions](https://www.ncei.noaa.gov/access/billions/mapping) and this is during a year when water remains in US reservoirs.  It is not just agriculture and livestock that faces problems with water shortages.  According to a 2013 survey conducted by Standard & Poors, businesses in the energy, utility, consumer staples, consumer discretionary, materials, industrial, health care and information technology sectors [all reported at least some concerns about water-related risk](https://www.brookings.edu/research/in-times-of-drought-nine-economic-facts-about-water-in-the-united-states/).  In short, water use is one of the most pressing issues the US and the world faces. 

In the case of the United Sates, one of the regions grappling with drought is the [Colorado River Basin](https://www.drought.gov/node/2075).  Lake Mead and Lake Powell have been operating under [guidelines designed for drought conditions since 2008](https://www.usbr.gov/lc/region/programs/strategies/RecordofDecision.pdf) and yet water levels have steadily declined since their enaction. California and Texas have also been particularly hard-hit. [While the problem is openly acknoweledged](https://www.ncei.noaa.gov/access/monitoring/dyk/colorado-basin-drought) and there is some public awareness, a detailed analysis of water consumption in regions impacted by drought is difficult to find and such analyses are often limited in scope. Without an honest and informed discussion about the inherent problem, the response to it is likely to be chaotic, ad hoc, and inequitable.  Golf courses may be watered while other people don't have access to running water.  The same people who complain about not being able to shower or use flush toilets may have watered their lawn two weeks prior.  

This project aims to help address the issue of water consumption by doing the following actions:
1.  Compile data about water consumption, weather information, and other factors such as demographics from reliable sources.   
2.  Model and analyze said data in order to determine what county or state-level cofactors have an impact on water consumption. National-level data will be used in the linear regression analysis in order to provide more reliable statistics.
3.  Tabulate the amount of water withdrawn and consumed from the Colorado River Basin for domestic and commercial purposes and compare that number with measures of water availability such as reservoir volumes and ground water estimates.
4.  Attempt to involve other people capable of being objective data analysts to help improve the models and expand the analysis to other river basins.

## Data
Five sources of data have been used for this analysis.  [Estimated Use of Water in the United States County-Level Data for 2015 (version 2.0)](https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8), a part of U.S. Geological Survey's (USGS's) National Water Use Science Project, was used as a source for water withdraw and consumption.     The data is released every 5 years and, as of Aug 2022, the [2015 dataset was the most recent one published](https://water.usgs.gov/watuse/data/).  It contained information about domestic, irrigation, thermoelectric power, industrial, mining, livestock, and aquaculture water-use. 
 [National Oceanic and Atmospheric Administration (NOAA)](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/) was used as a source for 2015 weather data, including precipitation, cooling and heating degree days, drought indexes such as the Palmer Hydrological Drought Index, and temperature values such as maximum temperature.  [OpenIntro.org](https://www.openintro.org/), an educational nonprofit, was used as a source for [census data](https://www.openintro.org/data/index.php?data=county) including poverty, homeownership, multi-unit housing percentage, unemployment rate, and metro area.  The non-profit Lincoln Institute of Land Policy [provided access to a csv](https://coloradoriverbasin-lincolninstitute.hub.arcgis.com/) that contained the counties which use water from the Colorado River as well as the reservoirs that are a part of the basin.  The fifth source was the [U. S. Bureau of Reclamation](https://www.usbr.gov/uc/water/hydrodata/).  They provided access to reservoir water storage data.
    
## Linear Regression Analyses  
The two USGS categories analyzed were golf course consumption and domestic withdraw.  Due to the strength of the correlation between population and water use, domestic was bifurcated into net and per capita withdraw categories.
    
### Golf Water Consumption 
 The persistence of non-normal residuals had an impact on the analysis which led to the log-scaling of acreage and consumptive use of water.    None of the weather variables required log scaling as they were already close to normal distributions.  Precipitation didn't have much impact on the model and was dropped.  For each increase of 1% in acreage, an associated increase of about 0.95% in water consumption was seen.  A one degree change in max temperature was associated with a 2.36% increase in the consumptive use of water and a one unit increase in PHDI was associated with 12% decrease in consumptive use.   The probability of Jarque Bera was 3.71e-27 which was a significant improvement from where the model had been.  R-squared was .747. Standardization indicated that acreage was the most important variable, followed by PHDI and maximum temperature.

![Golf Acreage](/images/golf_regression_plots_log(IG-IrTot).png?raw=true)
![Golf PHDI](/images/golf_regression_plots_PHDI.png?raw=true)
![Golf Maximum Temperature](/images/golf_regression_plots_Maximum_Temperature.png?raw=true)

###  Net Domestic Withdraw   
Population was the only factor that appeared to matter in the net domestic model. The high correlation between total population and total water withdraw was already seen in the correlation table (.959%) and linear regression only reconfirmed its importance.  Maricopa County was dropped from the chosen model.  While Maricopa County didn't have the highest per capita water consumption, the fact that it had a high per capita water consumption *and* a high population meant that it had a large impact and was an outlier.   R-squared was 94.7% and the expected amount of domestic water withdraw per person was 79.9 gallons per day.  Both results were statistically significant.  The model's Jarque-Bera probability was 0.00 which meant that the residuals did not belong to a normal distribution.  Log scaling did not solve the problem. The Mean Absolute Error was 1.82 and the Mean Squared Error was 6.21.


![Net Domestic](/images/Net_domestic_regression_TP-TotPop_without_outlier.png?raw=true)

### Per Capita Withdraw

The variables chosen for the per capita model were irrigation with surface water (IR-WSWFr), maximum temperature, PHDI, precipitation, unemployment rate, multi-unit percentage, and metro.  These were chosen because they didn't result in multicollinearity, they contributed to the R-squared of the model, and they were statistically significant.  The coefficient of determination (R-squared) of the chosen model was at 25.8%, which was a significant improvement from where the model started at (15.1% without outliers), but was still low-powered.  Non-normal residuals remained an issue throughout the models development and could not be solved by log scaling. The mean absolute error was at 17.6 gallons per person and the mean squared error was 27.3.   

The Y-intercept for the multiple linear regression model when standardized was 83.7 gallons. One standard deviation of each of the following variables was associated with its corresponding amount of gallon per person domestic water withdraw:


* IR-WSWFr       ................................................     9.58
* Max_temp           ................................................        8.01
* PHDI                  .........................................................      -6.04
* Precip                  .......................................................      -5.68
* unemployment_rate         ............................   -4.13    
* multi_unit             .................................................   -2.59
* metro_yes          ................................................   -2.49

Positive values indicate more water withdraw and negative values indicate less water withdraw.  With the exception of irrigation with surface water, all of the most important variables were weather related.  Unemployment was next.  Multi-unit and metro living were significantly less important than weather in this model. 


![Per Capita Parial Regression](/images/Per_capita_Domestic_Partial_Regression_multiple.png?raw=true)

![Per Capita Parial CCPR](/images/Per_capita_Domestic_CCPR_multiple.png?raw=true)

## Facebook Prophet Forecasting
 
 According to a csv downloaded from the Lincoln Institute of Land Policy, the sources of water for the Colorado River Basin were the lakes Havasu, Mohave, Mead, Powell, Vallecito, and Nighthourse, the reservoirs Navajo, McPhee, Ridgway, Crystal, Morrow Point, Blue Mesa, Taylor Park, Flaming Gorge, Fontenelle, Starvation, Strawberry, and Scofield, the Morelos Dam Diversion, Imperial Diversion Dam, Granby Dam, Heron Dam, Headgate Rock Diversion, Laguna Diversion, Palo Verde, Senator Wash, Jordanelle, Wilard Bay, and Pineview. The US Bureau of Reclamation (USBR) had storage data for every location except for Senator Wash, Palo Verde, Headgate Rock Diversion, Imperial Diversion Dam, and Morelos Dam Diversion. Data for the rest of the reservoirs were downloaded and compiled into a dataset.    Null values existed because some of the reservoirs were older than others and the nulls were converted to zeros.  The data for the reservoirs were downloaded on September 21, of 2022 and therefore was the last date contained within the dataset. At that time, the combined total of all of the reservoirs was 7,081,513 Mgal of water.
    
The program Facebook Prophet is an open-source data forecasting tool used to analyze time series data.  It is sensitive to the data given to it so if only data from 2000 onward was given, the forecast would have a sharper downward slope than if all of the data since 1937 were given.  In order to be conservative and avoid any accusations of cherry-picking, one of the forecasts used all of the available data.  That forecast had a yearly decline of -152,800 Mgal.  While the r-squared of the train portion of the forecast was high at .976, it failed when it was tested against all of the values since 2021.  It had forecasted a value of 8,324,972 Mgal by 2030 and the Colorado River Basin was already well below that number.  In short, the forecast was too conservative.  The second forecast performed better.  It forecasted a yearly decline of -790,832 Mgal, had a .95 r-squared in the train portion, which dropped to .44 once it was tested with the data from 2021 onwards, and had a mean absolute error of 291,264 Mgal in the train portion and a 563,561 Mgal error in the test portion.  It too erred by being too conservative in its Sep 21, 2022 forecast. 7,872,734 Mgals had been forecasted.  In both models, the lower bound crossed the zero mark by 2030.  In the second one, the lower bound crossed the zero mark in 2025.  If the forecast using data from 2000 onward is accurate, all of the water in Colorado River Basin reservoirs will be gone in ten years - (10)* (-790,832) + 7,081,513 = -826,707. 


![Facebook Prophet](/images/Reservoir_Forecast2000_raw.png?raw=true)

## 2015 Colorado River Basin Water Usage Versus Reservoir and Aquifer Depletion 
In order to provide an overall picture of the hydrologica cycle for the Colorado River Basin, estimates for groundwater and reservoir depletion and USGS water use categories were compiled and compared to one another.  When available, consumption was used for the USGS categories.  Otherwise withdraw was used.  Agriculture, golf courses, and power plants all had consumption as a categorical option.   Water withdraw had to be used for all other categories.  The 2000 forecast slope was used for reservoir depletion as it was more accurate than the 1937 version. [Groundwater depletion during drought threatens future water security of the Colorado River Basin](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014GL061055) (Castle, Stephanie L. et. al., *Geophysical Research Letters*, July 2014) was used as a source for the depletion of groundwater.
    
    
The combined total of reservoir and groundwater depletion was 2,270,195 Mgal.  The only USGS category that had more water use than that was agriculture at 3,491,549 Mgal.  Domestic was comparible at 1,617,990 Mgal, hence both agriculture and domestic use categories have to be areas of focus when it comes to discussing how to reduce overall water demand.  If one ignored groundwater, the amount needed to be reduced was still well beyond the capacity of any other category to make up for the shortfall.


![Water_Depletion_Use](/images/Water_Use_Compared_to_Water_Depletion.png?raw=true)

## Conclusions

* Population growth in regions impacted by declining water reserves could be beneficial to homeowners in the short-term by providing housing demand that could drive up prices and giving people who want to exit the market people to sell to, but in the long term it is likely detrimental to home equity.  92% of domestic water withdraw can be explained by population alone (or 94% if one excludes Maricopa County).  Hence, any actions or policies that result in greater levels of population in drought-prone regions are likely to accelerate the depletion of already over-utilized water resources.  The data suggests that this will happen at a rate of about 80 gallons per person per day.  How much of that is consumption and how much of it is just withdraw is unknown at this time.  For long term stakeholders, the lack of water availability should be a primary concern as many household appliances are dependent upon water access.

* The irrigation of lawns may be beneficial in the short-term by providing the illusion that nothing is wrong with water access which could help in the selling of a house(s), but the long-term consequences of such actions are likely to be detrimental to home equity.  While the model for per capita domestic water withdraw is weak considering it only explains 25.8% of the variation seen in the data, the p-values for the weather variables are all statistically significant and are among the most important, second only to non-domestic irrigation with fresh surface-water.  The most likely explanation for these correlations is watering lawns or gardens as other domestic uses of water are less likely to be greatly impacted by weather or have an association with other forms of irrigation.  If dry states could reduce their withdraw levels to that of other states, the potential water savings would be considerable.  (Rough estimate for the other states category - 1399 Mgal per day) 

* Long-term, it is best for owners and investors in golf courses to have smaller acreage in regions where water availability is an issue as acreage is the most important variable when it comes to predicting water consumption.  Maximum temperature was the next biggest factor so increases in temperature will probably result in more water being used for golf courses.  A one degree change in maximum temperature was associated with a 0.0236 MGal increase in daily irrigation. There was not much data to go on as almost all golf courses use sprinklers, but what data exists suggests micro-irrigation should be used in drought-prone regions.  It is debatable whether such changes are feasible in the short term given that it could be expensive, the changes may run counter to the expectations of one's customer base, and the impact of a single golf course will only delay the end result if other golf courses and other industries/consumers are not also applying water conservation strategies.  In short, golf courses may encounter tragedy of the commons problems.  

* Residents and people who purchase products made from raw materials produced in drought-prone regions should be cognizant of reservoir forecasts. A conservative forecast that included all of the reservoir storage data since 1937 for the Colorado River Basin had water declining at yearly rate of -152,800 Mgal and the lower bound crossing the zero mark by 2030.  A more pessimistic (and accurate) forecast that included all of the reservoir storage data since 2000 had water declining at yearly rate of -790.83 Mgal and the lower bound crossing the zero mark in 2025.  In short, it is entirely possible for all of the reservoirs in the Colorado River Basin to be out of water in less than ten years.  While it is also possible for water reserves to increase in volume, this would run counter to the trendline seen since 2000.  For people who work and live in the region, it is advisable to have a plan in place about what to do should the trendline continue to persist in its downward trajectory.  A lack of water availability is likely to be highly disruptive to the region's economy and living conditions. For those people who buy products made from raw materials produced in the region such as food and clothes, it may be advisable to buy some products in advance as scarcity brought about by a lack of water is likely to create shortages and drive-up prices.


## Next Steps

*  Agriculture has to be modeled.  It was left out of this analysis because it was a very complex topic given the various crops and regions, but it is the biggest consumer of water in areas where water availability is a concern.  There are a couple of ways water consumption for agriculture can be reduced. Micro-irrigation is one possibility.  Another is reducing the number of things grown.  According to the [Lincoln Institute](https://storymaps.arcgis.com/stories/2efeafc8613440dba5b56cb83cd790ba), alfalfa, which is used as feedstock for cows, is one of the primary crops grown in the Colorado River Basin.  Hence, less meat consumption should result in lower levels of water consumption.  Another major crop is corn.  There have been a number of papers that have concluded that corn costs more energy to produce than the caloric value of the corn itself (such as [Thermodynamics of the Corn-Ethanol Biofuel Cycle by Tad W. Patzek](http://alpha.chem.umb.edu/chemistry/ch471/evans%20files/Patzek.pdf)). If the net energy is indeed negative (or even slightly positive), and the production of corn depletes both water and phosphorous resources, one must seriously question the logic supporting the continued government subsidies for corn-based biofuel.  

* There are a number of steps that can be taken by governments, businesses, and individuals to reduce one's water consumption, but I don't feel it appropriate to lecture people on what they should or shouldn't do... with one exception.  Discuss this topic with others.  If one has a family member or a friend who is a physicist or a chemist, ask them what they know about the thermodynamics of biofuels.  Talk to a spouse or possibly children about what one should do if the worst should occur.  Insist that politicians whom support biofuel subsidies explain their positions not with sophistry, but with logic and physics.  Also insist that they explain what they plan to do if the reservoirs run dry.  If one happens to know a data analyst, have them question my results.  Please question me.  I am not someone with a messianic belief that I am infallible and those who dare challenge my conclusions are heretics unworthy of being debated.  Science (and data analysis) is a deliberative process, not an authoritarian one, and water consumption is a topic that desperately needs to be debated both among scientists and the layman alike. 

On the note of questioning me, there are several things that should be done that would help improve the quality of the models.

*  The modeling would likely benefit from the inclusion of humidity but this factor wasn't a part of the NOAA data and consequently wasn't included.  There might be a source somewhere that has the data.
*  USGS has data from prior years and the 2020 data should be coming out at some point in the near future.  The model would benefit from data from other years to see if similar results were obtained and to see if certain counties remain outliers.
* Outliers should be examined to see if one can come to understand why they are outliers. 
* Domestic water consumption had been a category in prior USGS reports but not in this one.  If one had data for both the water withdraw of homes and the water returned to sewage treatment plants, then consumption may be able to be calculated by subtracting the two values.  The wastewater returned would probably need its own category though as it is both consumption (in that it needs to be treated) and not consumption (as the water is still in its liquid phase and available to be reused).  Having such data would be useful, particularly given the considerable amount of water withdrawn for domestic purposes.
* The USGS data was based on calculations made by humans and there are assumptions made within those calculations.  More accurate models might be able to be created by using the raw data the USGS used rather than the calculations made by them.
* All other categories of water consumption should be analyzed.
* An updated version of groundwater analysis using NASA data should be done by someone who is an expert in the field. 
* All river basins and/or the regions listed on drought.gov should be invested specifically.
* More comprehensive analyses on potential water savings from things like micro-irrigation or not watering lawns should be conducted or incorporated. 

This is just a partial list.  There are likely many other improvements that can be made.  Everything in this notebook is open-source and it is hoped other people will want to make their own contributions and the models can improve through the processes of collaboration and debate.

## License  

[MIT](https://choosealicense.com/licenses/mit/)