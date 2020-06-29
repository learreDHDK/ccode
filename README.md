<h2>Introduction and scenario</h2>
<p>
	CCODe project has been carried out for the exam Open Access and Digital Ethics of Digital Humanities and Digital Knowledge course at the University of Bologna. The aim of the project is the analysis and the further re-use of open access datasets, in order to find some kind of new knowledge reachable through the mashup of the original data. The scenario object of our study is climate change. What interested us was to go deeper in showing:
	<li>The main factors of climate change;</li>
	<li>The impact of the countries on climate change and the commitments undertaken by them to fight it;</li>
	<li>The opinions of the European Union citizens on climate change.</li>
</p>

<p>
	In line with our purpose, we selected 15 datasets and we performed on them several analysis under different points of view, then we extracted the data which we were interested in and finally we created three new datasets based on the above-mentioned areas.
</p>

<p>
	The last step was the visualization of our datasets to facilitate the access and the understanding for the final user.
</p>

<h2>Original datasets</h2>
<p>
	In order to cope with our goals we chose 15 datasets related to our scenario. These were selected for their various proveniences, typologies, formats, metadata and licenses. Whenever in doubt, we considered the frequent citations of academic sources as proof of the reliability of the dataset. We selected the ones that at least at a first glance seemed free from cognitive biases, fair, legal valid, consistent and accurate.
</p>
<p>
	With the goal to depict climate change over time, we selected eight datasets, concerning the main factors to measure climate change (temperature and precipitation anomalies and sea ice extent) together with significant events caused by it (droughts, floods, hurricanes, wildfires and the threatening of species). The majority (6/8) comes from American-based institutions (e.g. NOAA), while the others are provided by supranational organizations, as OECD and UNEP. Five out of eight report data collected on a country-based scale. Sea Ice Extent, Precipitation and Temperature anomalies are available only globally. Overall the datasets span from 1980 to 2019. Nonetheless, Wildfires started and Droughts ended in 2003; Threatened Species refers to 2019 only. Precipitation and Temperature started from the end of the XIX century. 
</p>
<p>
	To understand the impact of the single countries on climate change and their commitment against it, we selected four datasets, regarding GHG emissions, ecological footprints, submissions to Paris Agreement and global funds concerning climate change. All datasets come from supranational institutions as OECD and WRI. They are all modeled on a country basis. Starting from the 60s, they have different beginning dates, but they all end in recent years (minimum 2016). Paris agreement is circumstricted to the year of the ratification (2015). 
</p>
<p>
	Aiming to include the human perception of the problem, we were able to find three datasets built from Eurobarometer surveys of 2009, 2013 and 2019, reporting the opinions of European citizens on climate change. Data were collected country by country in the EU and are directly provided by this body. 
</p>
<p>
	In some cases, we found the datasets on re-user websites, as specified below.
</p>
<p>
	In the following table, the preliminary analysis we performed on each dataset can be found.
</p>
<h3>General analysis</h3>
<table style="border: 1px solid black">
			<tr style="border: 1px solid black">
				<th>Subject</th>
				<th>Name</th>
				<th>Owner</th>
				<th>Owner URL</th>
				<th>Publisher</th>
				<th>Re-user</th>
				<th>Publisher or re-user URL</th>
				<th>Data Type</th>
				<th>Chosen format</th>
				<th>Metadata</th>
				<th>Licence</th>
				<th>Domain</th>
				<th>Spatial coverage</th>
				<th>Time range</th>
				<th>Upload date</th>
				<th>Last update</th>
				<th>Update Frequency</th>
				<th>Nature (description)</th>
			</tr>
			<tr>
				<td>Droughts</td>
				<td>Droughts events 1980-2001</td>
				<td>United Nations Environment Programme UNEP</td>
				<td>https://preview.grid.unep.ch/index.php?preview=data&events=droughts&evcat=1&lang=eng</td>
				<td></td>
				<td>Humanitarian Data Exchange HDX</td>
				<td>https://data.humdata.org/dataset/global-droughts-events-1980-2001</td>
				<td>Quantitative</td>
				<td>CSV</td>
				<td>Yes, ISO 19115:2003/19139</td>
				<td>Available for free for non commercial purpose, as explained at https://preview.grid.unep.ch/index.php?preview=about&cat=2&lang=eng</td>
				<td>Environment</td>
				<td>Global</td>
				<td>Jan 01, 1980 - Dec 31, 2001</td>
				<td>Not stated</td>
				<td>November 17, 2018</td>
				<td>Never</td>
				<td>This dataset includes an estimate of global drought annual repartition based on Standardized Precipitation Index.</td>
			</tr>
			<tr>
				<td>Floods</td>
				<td>Global Active Archive of Large Flood Events</td>
				<td>Dartmouth Flood Observatory, University of Colorado</td>
				<td>http://floodobservatory.colorado.edu/Archives/index.html</td>
				<td></td>
				<td>Humanitarian Data Exchange HDX</td>
				<td>https://data.humdata.org/dataset/global-active-archive-of-large-flood-events</td>
				<td>Direct Observational Data/Anecdotal Data</td>
				<td>XLSX</td>
				<td>Just HDX</td>
				<td>Creative Commons Attribution 4.0 International license (CC BY 4.0)</td>
				<td>Environment</td>
				<td>Global</td>
				<td>1985 - present</td>
				<td>Sep 02, 2019 (HDX)</td>
				<td>Last entry 01/2020 (dataset) / October 11, 2019 (HDX)</td>
				<td>Live</td>
				<td>This dataset contains an active archive of flood event records.</td>
			</tr>
			<tr>
				<td>Hurricanes</td>
				<td>International Best Track Archive for Climate Stewardship (IBTrACS) Project, Version 4</td>
				<td>NOAA National Centers for Environmental Information</td>
				<td>https://www.ncdc.noaa.gov/ibtracs/index.php?name=ib-v4-access</td>
				<td>NOAA National Centers for Environmental Information</td>
				<td></td>
				<td>https://www.ncdc.noaa.gov/ibtracs/index.php?name=ib-v4-access</td>
				<td>Quantitative</td>
				<td>CSV</td>
				<td>Yes
ISO 19115-2: https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C01552</td>
				<td>World Data Center for Meteorology policy and World Meteorological Organization's Resolution 40 policy: https://www.ncdc.noaa.gov/ibtracs/index.php?name=terms</td>
				<td>Environment</td>
				<td>Global</td>
				<td>1980 - present</td>
				<td>2019-02-15 (NOAA) / March 2019 (IBTrACS Project)</td>
				<td>Not stated</td>
				<td>Twice weekly - Weekly (IBTrACS Project) / Daily (NOAA) </td>
				<td>This dataset contains a complete set of historical tropical cyclones, obtained from the combination of information from numerous tropical cyclone datasets.</td>
			</tr>
			<tr>
				<td>Wildfires</td>
				<td>GFEDv4 (Global Fire Emissions Database, Version 4)</td>
				<td>Oak Ridge National Laboratory (ORNL) Distributed Active Archive Center (DAAC)</td>
				<td>http://www.globalfiredata.org/analysis.html</td>
				<td>Oak Ridge National Laboratory (ORNL) Distributed Active Archive Center (DAAC).</td>
				<td></td>
				<td>http://www.globalfiredata.org/analysis.html</td>
				<td>Quantitative</td>
				<td>CSV</td>
				<td>Yes https://daac.ornl.gov/VEGETATION/guides/fire_emissions_v4.html</td>
				<td>Data hosted by the ORNL DAAC is openly shared, without restriction, in accordance with NASA's Earth Science program Data and Information Polic</td>
				<td>Environment</td>
				<td>Global</td>
				<td>1995-06-01 to 2016-12-31 / 2003-2019</td>
				<td>September 2015</td>
				<td>2017-09-29</td>
				<td>Periodically</td>
				<td>This dataset is data on the global estimates of annual fires of different types.</td>
			</tr>
			<tr>
				<td>Temperature</td>
				<td>Climate at a Glance - Time Series Graphs of Temperature Anomalies</td>
				<td>NOAA National Centers for Environmental Information</td>
				<td>https://www.climate.gov/maps-data/dataset/global-temperature-anomalies-graphing-tool </td>
				<td>NOAA National Centers for Environmental Information</td>
				<td>https://www.ncdc.noaa.gov/cag/global/time-series</td>
				<td>https://www.climate.gov/maps-data/dataset/global-temperature-anomalies-graphing-tool</td>
				<td>Land-based station, Marine / Ocean</td>
				<td>CSV, XML, JSON</td>
				<td>Yes, https://www.ncdc.noaa.gov/cag/global/data-info / https://www.climate.gov/maps-data/dataset/global-temperature-anomalies-graphing-tool </td>
				<td>FOIA (5 USC 552)</td>
				<td>Environment</td>
				<td>Global</td>
				<td>1880-present</td>
				<td>February 2020 (it changes every month)</td>
				<td>Not stated</td>
				<td>Monthly (not stated)</td>
				<td>This dataset is the result of Comparing the average temperature of land, ocean, or land and ocean combined for any month or multi-month period to the average temperature for the same period over the 20th century showing if conditions are warmer or cooler than the past.</td>
			</tr>
			<tr>
				<td>Threatened species</td>
				<td>Threatened species</td>
				<td>OECD (Organisation for Economic Co-operation and Development)</td>
				<td>https://stats.oecd.org/Index.aspx?DataSetCode=WILD_LIFE</td>
				<td>OECD (Organisation for Economic Co-operation and Development)</td>
				<td></td>
				<td>https://stats.oecd.org/Index.aspx?DataSetCode=WILD_LIFE</td>
				<td>Quantitative</td>
				<td>Text file (CSV), Excel, SDMX(XML)</td>
				<td>Yes, https://stats.oecd.org/OECDStat_Metadata/ShowMetadata.ashx?Dataset=WILD_LIFE&Lang=en</td>
				<td>http://www.oecd.org/termsandconditions/  Except where additional restrictions apply as stated above, You can extract from, download, copy, adapt, print, distribute, share and embed Data for any purpose, even for commercial use. You must give appropriate credit to the OECD by using the citation associated with the relevant Data, or, if no specific citation is available, You must cite the source information using the following format: OECD (year), (dataset name),(data source) DOI or URL (accessed on (date)). When sharing or licensing work created using the Data, You agree to include the same acknowledgment requirement in any sub-licenses that You grant, along with the requirement that any further sub-licensees do the same.</td>
				<td>Environment</td>
				<td>Global</td>
				<td>2018-2019</td>
				<td>Not stated</td>
				<td>March 2019</td>
				<td>Not stated?</td>
				<td>This dataset is data on the state of threatened species build on country replies to the Annual Quality Assurance (AQA) of OECD environmental reference series.</td>
			</tr>
			<tr>
				<td>Sea ice</td>
				<td>Sea Ice and Snow Cover Extent</td>
				<td>NSIDC National Snow and Ice Data Center (https://nsidc.org/)</td>
				<td></td>
				<td></td>
				<td>NOAA National Centers for Environmental Information</td>
				<td>https://www.ncdc.noaa.gov/snow-and-ice/extent/</td>
				<td>Satellite</td>
				<td>CSV, XML, JSON</td>
				<td>Yes: https://www.climate.gov/maps-data/dataset/snow-or-ice-extent-graphing-tool</td>
				<td>FOIA (5 USC 552)</td>
				<td>Environment</td>
				<td>Global</td>
				<td>1979-2020</td>
				<td>Not stated</td>
				<td>Not stated</td>
				<td>Not stated</td>
				<td>This dataset shows how the sea ice extent has changed from 1979 to 2020. The available data cover the North America + Greenland, Northern Hemisphere, Eurasia, and North America.</td>
			</tr>
			<tr>
				<td>Precipitations</td>
				<td>Climate Change Indicators: U.S. and Global Precipitation</td>
				<td>NOAA National Centers for Environmental Information</td>
				<td>https://www.ncdc.noaa.gov/data-access/land-based-station-data/land-based-datasets/global-historical-climatology-network-monthly-version-2?fbclid=IwAR20WeoOz2fCxr0hPl_KgqkAIJKu2CY0eNTlPYu5CtH3osaDUSbFlQR26kM</td>
				<td></td>
				<td>EPA - US Environmental Protection Agency</td>
				<td>https://www.epa.gov/climate-indicators/climate-change-indicators-us-and-global-precipitation</td>
				<td>Quantitative</td>
				<td>CSV</td>
				<td>Yes 
EPA (https://www.epa.gov/climate-indicators/downloads-indicators-technical-documentation)       NOAA: ISO 19115-2 Metadata https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C00835#</td>
				<td>Not stated / Yes FOIA?</td>
				<td>Environment</td>
				<td>USA and Global</td>
				<td>1901-2015</td>
				<td>April 2010</td>
				<td>August 2016</td>
				<td>Not stated</td>
				<td>This dataset shows how the total annual amount of precipitation over land worldwide has changed since 1901.</td>
			</tr>
			<tr>
				<td>Ghg emissions by country</td>
				<td>Greenhouse Gas Emissions</td>
				<td>OECD</td>
				<td>https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG#</td>
				<td>https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG#</td>
				<td></td>
				<td>https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG#</td>
				<td>Quantitative</td>
				<td>CSV</td>
				<td>Yes</td>
				<td>http://www.oecd.org/termsandconditions/</td>
				<td>Environment</td>
				<td>Global</td>
				<td>1990-2017</td>
				<td>Not stated</td>
				<td>August 2019</td>
				<td>Not stated</td>
				<td>This dataset presents trends in man-made emissions of major greenhouse gases and emissions by gas.</td>
			</tr>
			<tr>
				<td>Footprint by country</td>
				<td>National Footprint and Biocapacity Accounts 2019 Public Data Package</td>
				<td>Global Footprint Network</td>
				<td>https://www.footprintnetwork.org/licenses/public-data-package-free/</td>
				<td>Global Footprint Network</td>
				<td></td>
				<td>https://www.footprintnetwork.org/licenses/public-data-package-free/</td>
				<td>Quantitative</td>
				<td>CSV</td>
				<td>Yes</td>
				<td>Creative Commons Attribution-ShareAlike 4.0 International License (CC-BY-SA 4.0)</td>
				<td>Environment</td>
				<td>Global</td>
				<td>1961-2016</td>
				<td>Not stated</td>
				<td>Not stated</td>
				<td>Not stated</td>
				<td>This dataset contains data related to the ecological footprint of the countries.</td>
			</tr>
			<tr>
				<td>Adhesion to Paris agreement</td>
				<td>CAIT Paris Contributions Data</td>
				<td>WRI - World Resource Institute</td>
				<td>https://www.wri.org/resources/data-sets/cait-paris-contributions-data</td>
				<td>WRI - World Resource Institute</td>
				<td></td>
				<td>https://www.wri.org/resources/data-sets/cait-paris-contributions-data</td>
				<td>Descriptive</td>
				<td>XLSX</td>
				<td>Yes</td>
				<td>Creative Commons Attribution 4.0 International License</td>
				<td>Environment, Politics</td>
				<td>Global</td>
				<td>2015-2016</td>
				<td>March 2015</td>
				<td>February 19, 2016</td>
				<td>Not stated</td>
				<td>This dataset collects information about all the countries which submitted the Paris Agreement. In particular the date of submission and the summary of the undertaken commitments.</td>
			</tr>
			<tr>
				<td>Investments for climate change</td>
				<td>Cumulative data on the contributors of climate finance</td>
				<td>Climate Funds Update</td>
				<td>https://climatefundsupdate.org/data-dashboard/#1541245664327-538690dc-b9a8</td>
				<td>Climate Funds Update</td>
				<td></td>
				<td>https://climatefundsupdate.org/data-dashboard/#1541245664327-538690dc-b9a8</td>
				<td>Quantitative</td>
				<td>CSV</td>
				<td>Yes: https://climatefundsupdate.org/about-us/notes-and-methodology/</td>
				<td>Not stated</td>
				<td>Economy, Environment </td>
				<td>Global</td>
				<td>2003-2019</td>
				<td>Not stated</td>
				<td>February 2019</td>
				<td>Not stated</td>
				<td>This dataset collects information about the funds invested by the countries at a global level in order to fight the climate change.</td>
			</tr>
			<tr>
				<td>Opinions on climate change EU 2009</td>
				<td>Special Eurobarometer 313: Europeans’ attitudes towards climate change</td>
				<td>Directorate-General for Communication of the European Commission</td>
				<td>https://data.europa.eu/euodp/it/data/dataset/S942_71_1_EBS313</td>
				<td>Directorate-General for Communication of the European Commission</td>
				<td></td>
				<td>https://data.europa.eu/euodp/it/data/dataset/S942_71_1_EBS313</td>
				<td>Qualitative and quantitative</td>
				<td>XLS</td>
				<td>Yes + https://europarl.europa.eu/at-your-service/files/be-heard/eurobarometer/2009/climate-change/report/it-report-climate-change-200907.pdf</td>
				<td>https://data.europa.eu/euodp/it/copyright</td>
				<td>Government and public sector</td>
				<td>Slovacchia, Slovenia, Svezia, Paesi Bassi, Polonia, Portogallo, Romania, Belgio, Austria, Cipro, Bulgaria, Germania, Cechia, Spagna, Danimarca, Finlandia, Estonia, Regno Unito, Francia, Ungheria, Grecia, Italia, Irlanda, Lussemburgo, Lituania, Malta, Lettonia</td>
				<td>January-February 2009</td>
				<td>2014-12-09</td>
				<td></td>
				<td></td>
				<td>This dataset is data on the public opinon of European citizens on the issue of climate change.</td>
			</tr>
			<tr>
				<td>Opinions on climate change EU 2019</td>
				<td>Special Eurobarometer 409: Climate change</td>
				<td>Directorate-General for Communication of the European Commission</td>
				<td>https://data.europa.eu/euodp/en/data/dataset/S2212_91_3_490_ENG</td>
				<td>Directorate-General for Communication of the European Commission</td>
				<td></td>
				<td>https://data.europa.eu/euodp/en/data/dataset/S2212_91_3_490_ENG</td>
				<td>Qualitative and quantitative</td>
				<td>XLS</td>
				<td>Yes</td>
				<td>https://data.europa.eu/euodp/it/copyright</td>
				<td>Government and public sector</td>
				<td>Romania, Slovacchia, Slovenia, Svezia, Malta, Paesi Bassi, Polonia, Portogallo, Belgio, Austria, Cipro, Bulgaria, Germania, Cechia, Spagna, Danimarca, Finlandia, Estonia, Regno Unito, Francia, Croazia, Grecia, Irlanda, Ungheria, Lituania, Italia, Lettonia, Lussemburgo</td>
				<td>From 2019-04-09 to 2019-04-26</td>
				<td>2019-09-11</td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>Opinions on climate change EU 2013</td>
				<td>Special Eurobarometer 409: Climate change</td>
				<td>Directorate-General for Communication of the European Commission</td>
				<td>https://data.europa.eu/euodp/it/data/dataset/S1084_80_2_409</td>
				<td>Directorate-General for Communication of the European Commission</td>
				<td></td>
				<td>https://data.europa.eu/euodp/it/data/dataset/S1084_80_2_409</td>
				<td>Qualitative and quantitative</td>
				<td>XLS</td>
				<td>Yes</td>
				<td>https://data.europa.eu/euodp/it/copyright</td>
				<td>Government and public sector</td>
				<td>Romania, Slovacchia, Slovenia, Svezia, Malta, Paesi Bassi, Polonia, Portogallo, Belgio, Austria, Cipro, Bulgaria, Germania, Cechia, Spagna, Danimarca, Finlandia, Estonia, Regno Unito, Francia, Croazia, Grecia, Irlanda, Ungheria, Lituania, Italia, Lettonia, Lussemburgo</td>
				<td>November-December 2013</td>
				<td>2014-12-03</td>
				<td></td>
				<td></td>
				<td>This dataset is data on the public opinon of European citizens on the issue of climate change.</td>
			</tr>
	</table>
<h2>Quality analysis</h2>
<p>We started the analysis of the original datasets by inspecting their quality and accuracy. As a reference, we used the <a href="https://www.europeandataportal.eu/sites/default/files/european_data_portal_-_open_data_goldbook.pdf">Open Data Goldbook for Data Managers and Data Holders</a>, provided by European Data Portal, which is meant to be a practical guidebook for organizations wanting to publish Open Data. The questions posed to examine the quality of the dataset mainly concern completeness, cleanness, accuracy, timeliness and consistency. In the following table we report the output of the analysis.</p>
<table style="border: 1px solid black">
			<tr style="border: 1px solid black">
				<th>DATA QUALITY</th>
				<th>Droughts events 1980-2001</th>
				<th>Global Active Archive of Large Flood Events</th>
				<th>International Best Track Archive for Climate Stewardship (IBTrACS) Project, Version 4</th>
				<th>GFEDv4 (Global Fire Emissions Database, Version 4)</th>
				<th>Climate at a Glance - Time Series Graphs of Temperature Anomalies</th>
				<th>Threatened species</th>
				<th>Sea Ice and Snow Cover Extent</th>
				<th>Climate Change Indicators: U.S. and Global Precipitation</th>
				<th>Greenhouse Gas Emissions</th>
				<th>National Footprint and Biocapacity Accounts 2019 Public Data Package</th>
				<th>CAIT Paris Contributions Data</th>
				<th>Global Investments</th>
				<th>Special Eurobarometer 313: Europeans’ attitudes towards climate change</th>
				<th>Special Eurobarometer 409: Climate change</th>
				<th>Special Eurobarometer 490: Climate change</th>
			</tr>
			<tr>
				<td><b>Other</b></td>
				<td>We wrote an email to the contributor of the dataset in order to ask if there exist a legend to codify the headers of the dataset, but we never received an answer.</td>
				<td></td>
				<td></td>
				<td>The API platform from which the data was download could not support mixed queries to retrive at once data of the world so we had to download the data in series and then created a united csv file for the dataset</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td>even if you set some conditions for your query e.g. include LULUFC it gives you also the data before where it is excluded</td>
				<td></td>
				<td>In order to process our dataset we need to modify the text, directly on the sheet, of one single cell (which contains some date information). We did this because the format of the date was not conformant to be processed, since it contained both xldate and string information.

Another change was made in the cells of the columns containing the ""Summary"". We decided to clean the information in these cells because in addition to the proper text they contained also html tags and entities.</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>Content quality</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>Is the dataset complete?</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>"Contain a header row with a single description of what is shown. This means that once a
dataset structure is in place, it should not change when sources are added. In the
metadata, the header should be described"</td>
				<td>Yes, but the key (legenda) for reading the columns is not provided</td>
				<td>Yes, but the header entries described on the website (http://www.dartmouth.edu/~floods/Archives/ArchiveNotes.html) don't correspond to the actual entries of the dataset.</td>
				<td>Yes, it is explained in a specific PDF document.</td>
				<td>Yes in the dataset</td>
				<td>Yes in the dataset</td>
				<td>Yes, from dataset and https://stats.oecd.org/Index.aspx?DataSetCode=WILD_LIFE</td>
				<td>Yes</td>
				<td>Yes from the dataset and from https://www.epa.gov/climate-indicators/climate-change-indicators-us-and-global-precipitation</td>
				<td>Yes, but the header has not been described anywhere.</td>
				<td>Yes, the header row is present and further explained in the PDF document about the work.</td>
				<td>Yes (description in natural language)</td>
				<td>Yes (easily understandable header row) </td>
				<td>Yes (in dataset)</td>
				<td>Yes, the questions contained in the dataset are explained in metadata pdf</td>
				<td>Yes, the questions contained in the dataset are explained in a PDF document about the survey.</td>
			</tr>
			<tr>
				<td>"Be labelled with a version number. Once an update is done the dataset should get a new
version number in order for the audience to keep track of changes"</td>
				<td>No</td>
				<td>No</td>
				<td>Yes, Version 4</td>
				<td>Yes Version 4 (GFEDv4)</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>Global Historical Climatology Network–Monthly (GHCN-M) Version 2</td>
				<td>No</td>
				<td>No, there is no version number, but the title contains the year of the account.</td>
				<td>No</td>
				<td>No</td>
				<td>Yes, v1.00 </td>
				<td>Yes, v1.00 </td>
				<td>Yes, v1.00 </td>
			</tr>
			<tr>
				<td>"Contain information about its origin. What is the data about, where does it come from
and for what purpose has it been published?"</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
			</tr>
			<tr>
				<td>Be given a status: Draft, validated, final</td>
				<td>Inferred: Final</td>
				<td>Validated ("Active")</td>
				<td>Version numbers are updated when processing changes cause changes to storms from previous years (for example, by adjustments to the merge routines)
Inferred: Validated</td>
				<td>This data is updated periodically and has no reasons for this. Could not access the previous versions because they are superseded by new versions so they say the old versions are accessible at the ORNL. Inferred: Validated</td>
				<td>Inferred validated bescause the data is updated yearly from a view of the dataset but not stated.</td>
				<td>Not stated and not inferable since data contains no information on years but just stated in the website that the data is on the latest year available</td>
				<td>Validated (updated every year since 1979)</td>
				<td>Inferred Validated since the data has a version and may change in the future</td>
				<td>Not stated and not inferable, since data contains no information on the years concerned and it is just stated on the website that it is referred to the latest year available.</td>
				<td>A new dataset is published every year. Inferred: Final</td>
				<td>Final (data from 2015 and 2016)</td>
				<td>Cumulative since 2003; up to date as of February 2019 (https://climatefundsupdate.org/about-us/notes-and-methodology/).

Inferred: Validated</td>
				<td>Final</td>
				<td>Final</td>
				<td>Final</td>
			</tr>
			<tr>
				<td>Is the data clean?</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>Empty fields</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>No</td>
				<td>No</td>
				<td>Yes</td>
				<td>No</td>
				<td>No</td>
				<td>Yes</td>
				<td>No</td>
				<td>No (if missing data "Not specified")</td>
				<td>Yes (345, 346)</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
			<tr>
				<td>Dummy data and default values: are they correct?</td>
				<td>Yes (e.g. 0)</td>
				<td>Yes: 0, default values in case of uncertain number of deads or displaced (http://www.dartmouth.edu/~floods/Archives/ArchiveNotes.html)</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>Yes, maybe the column of powercode</td>
				<td>Yes (e.g. -9999 probably missing data)</td>
				<td>No</td>
				<td>No</td>
				<td>Yes (0, NULL)</td>
				<td>No</td>
				<td>No dummy
"Not applicable" as default value</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
			<tr>
				<td>Wrong values</td>
				<td>No</td>
				<td>Same countries have occasionally been indicated with different names, e.g. United Kingdom and UK. Many countries' names have been mispelled</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>Yes: Côte d'Ivoire and Réunion have special characters instead of accented letters, probably for encoding issues.</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
			<tr>
				<td>Double entries</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
			<tr>
				<td>Privacy sensitive information</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
			<tr>
				<td>Is the data accurate?</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>"Is the data accurate enough
for its potential purpose?"</td>
				<td>No, because is only indicated the country and the year. We don't know the duration of the event, the severity, the exact place in the country, ...</td>
				<td>No, since the work of other archives is not taken into account and it is based mainly on news, so many events could have been left out.</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>v</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>v</td>
				<td>Yes</td>
				<td>Yes</td>
			</tr>
			<tr>
				<td>"Does its accuracy affect its reliability? (only if the answer to the previous question is "No")"</td>
				<td>No</td>
				<td>No</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>"Are the choices concerning
interval described?"</td>
				<td>No </td>
				<td>No </td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No since there is no information concerning years</td>
				<td>Not explained why the dataset starts from 1979.
No, but it's easily understendable (i.e. every year since 1979)</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>Under the U.N. Framework Convention on Climate Change (UNFCCC), countries committed to create a new international climate agreement by the conclusion of the Paris climate summit in December 2015.

The dataset was created after the above mentioned agreement.</td>
				<td>Yes
CFU data is cumulative since 2003. This is the first year in which one of the dedicated climate funds hat we monitor approved finance for a project. The start date for each fund individually is available on the relevant fund page through ‘The Funds’ (https://climatefundsupdate.org/the-funds/)</td>
				<td>No, just the context of the survey is explained in the introduction of the explanatory PDF.</td>
				<td>No, just the context of the survey is explained in the introduction of the explanatory PDF.</td>
				<td>No, just the context of the survey is explained in the introduction of the explanatory PDF.</td>
			</tr>
			<tr>
				<td>"Does the data need
aggregation or disaggregation?"</td>
				<td>No</td>
				<td>No</td>
				<td>Data would probably need aggregation, because the resulting dataset is too big and much information could probably be condensed. For instance the same hurricane is registered more than once even in the same country because all the steps of the passage are traced.</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
			<tr>
				<td><b>Timeliness</b></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>	
			<tr>
				<td>"Data changes over time. Historical data will remain stable, but recent data will be updated over time.
Therefore, it is important to check data with regard to its timeliness regularly. For consistency
purposes, it is wise to create an update process that keeps the data up-to-date. Be sure that the data
contains a notion of its timeliness. This topic is closely related to the maintenance of datasets."</td>
				<td>No (not updated since 2001).
Timeliness in data.</td>
				<td>The dataset is updated, but the frequency of the procedure is not stated. Data contains a notion of its timeliness.</td>
				<td>There is timeliness in data. It is clear that the dataset is updated, but the frequency is unclear: in "Status" section, it is said to be annual; in "Data access" section, twice weekly. Also the update frequency of the single sources is reported on the website.</td>
				<td>Yes, there is timeliness in the data. The data has no update machanism but since it has versions, it is said to be updated periodically.</td>
				<td>Yes, there is timeliness in the data. The data has no update machanism but since it has versions, it is inferred that it is updated yearly.</td>
				<td>Not updated but only stated that the data is from the latest year available</td>
				<td>Yes (inferred: every year)</td>
				<td>Not stated but inferred may be updated since it has a version. But it also stated in the website that the last update of the version of the data containing precipitation informtion was on 2011-01-01 and this version id considere as the latest available one.</td>
				<td>Update frequency isn't stated, but there is timeliness in data.</td>
				<td>Annually updated and timeliness is present in data.</td>
				<td>Not updated because contains info about an agreement which took place between 2015 and 2016</td>
				<td>The dataset is cumulative since 2003 and the last update was in february 2019. 
Probably every year the dataset is updated with new data, while maintaining the old ones.

No notion of timeliness in data</td>
				<td>Inferred: not needed. 
No notion of timeliness in the data and no update process because it is referred to a single year.</td>
				<td>Inferred: not needed. 
No notion of timeliness in the data and no update process because it is referred to a single year.</td>
				<td>Inferred: not needed. 
No notion of timeliness in the data and no update process because it is referred to a single year.</td>
			</tr>
			<tr>
				<td><b>Consistency</b></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>"Reading through the quality aspects of data, the consistency of the presentation of your data is of
major importance. Imagine re-users correlating data from various sources, but all datasets differ in
accuracy, use of terms and timeframe. As an example, if you change the field names of the data
collected for managing waste each year, the data cannot be compiled from one year to the next. This
makes it difficult to use datasets: it will require a large effort of manipulation. Therefore, make sure
you use the standards and be consistent in publishing datasets of equal quality."</td>
				<td>Not stated</td>
				<td>There seems to be no consistency w.r.t. the previous tables of 2007 and 2008, available on the website: the standard is different, as well as the field names.</td>
				<td>Consistency is stated among the fundamental principles of the project in two occasions on the website: 
https://www.ncdc.noaa.gov/ibtracs/index.php?name=status and
https://www.ncdc.noaa.gov/ibtracs/index.php?name=principle</td>
				<td>No, each version from the writtings is different and contains new information</td>
				<td>Not stated but inferable. Probably every year the same sheet is updated.</td>
				<td>Not stated, but it is inferred since the data is obdated often and the fields remain the same.</td>
				<td>Not stated but inferable. Probably every year the same sheet is updated.</td>
				<td>Not stated but inferable. Probably the same sheet was used for the previous version but can't have access to. Need  to call the archive to get this information.</td>
				<td>Not stated nor inferable.</td>
				<td>Yes: the methodology for the account of data is described in the explanatory PDF, also for what concerns the previous versions.</td>
				<td>Yes (only one version, data not updated)</td>
				<td>Not stated but inferable. 
Probably every year the same sheet is updated.</td>
				<td>No: wrt the other datasets of the eurobarometer series, questions change without explanation</td>
				<td>No: wrt the other datasets of the eurobarometer series, questions change without explanation</td>
				<td>No: w.r.t. the other datasets of the Eurobarometer series, questions have changed throughout the time, but the decision and the differences are not explained. </td>
			</tr>
		</table>
		
<h2>Legal analysis</h2>
<p>Having performed a quality analysis already on our original datasets, we continued our analysis step with the legal one. This analysis was performed mostly with the purpose of checking the legal correctness of the various datasets in terms of Privacy Issues, IPR of the dataset, Licenses, Limitation on Public Access, Economical condition and Temporal aspects according to the “Check list for Public Administration for the Open Data release”.</p>
<p>Here below you have a representation of the outcome of this analysis.</p>
<p>We used a Yes/No answering format but when necessary, we also provided broad information or links for clarifications on the choice of the answer.</p>
<table style="border: 1px solid black">
			<tr style="border: 1px solid black">
				<th>Legal Basis</th>
				<th>Droughts events 1980-2001</th>
				<th>Global Active Archive of Large Flood Events</th>
				<th>International Best Track Archive for Climate Stewardship (IBTrACS) Project, Version 4</th>
				<th>GFEDv4 (Global Fire Emissions Database, Version 4)</th>
				<th>Climate at a Glance - Time Series Graphs of Temperature Anomalies</th>
				<th>Threatened species</th>
				<th>Sea Ice and Snow Cover Extent</th>
				<th>Climate Change Indicators: U.S. and Global Precipitation</th>
				<th>Greenhouse Gas Emissions</th>
				<th>National Footprint and Biocapacity Accounts 2019 Public Data Package</th>
				<th>CAIT Paris Contributions Data</th>
				<th>Cumulative data on the contributors of climate finance</th>
				<th>Special Eurobarometer 313: Europeans’ attitudes towards climate change</th>
				<th>Special Eurobarometer 409: Climate change</th>
				<th>Special Eurobarometer 490: Climate change</th>
			</tr>
			<tr>
				<td><b>Privacy issues</b></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td><b>"1.1 Is the dataset free of any personal data as defined in the Regulation (EU) 2016/679?
https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=CELEX:32016R0679&from=IT"</b></td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
			</tr>
			<tr>
				<td>"1.2 Is the dataset free of any indirect personal data that could be used for identifying the natural person? If so, is there a law that authorize the PA to release them? Or any
other legal basis? Identify the legal basis."</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
			</tr>
			<tr>
				<td>"1.3 Is the dataset free of any particular personal data (art. 9
GDPR)?
If so is there a law that authorize the PA to release them ?"</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
			</tr>
			<tr>
				<td>1.4 Is the dataset free of any information that combined with common data available in the web, could identify the person? If so, is there a law that authorize the PA to release them?</td>
				<td>Yes</td>
				<td>No, for each event, the location and the date are stated, so tracing back the news source could lead to individuals' name.</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
			</tr>
			<tr>
				<td>1.5 Is the dataset free of any information related to human rights (e.g. refugees, witness protection, etc.)?</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
			</tr>
			<tr>
				<td>"1.6 Is a tool used for calculating the range of the risk of de-
anonymization?

Is the dataset anonymized? With which technique?
Is it compliant with the three mandatory parameters: singling out,
linking out, inference out?"</td>
				<td></td>
				<td>Not stated</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>1.7 Are you using geolocalization capabilities ? Do you check that the geolocalization process can’t identify single individuals in some circumstances?</td>
				<td>No</td>
				<td>Yes, identifiable</td>
				<td>Yes, not identifiable</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>1.8 Does the open data platform respect all the privacy regulations (registration of the end-user, profiling, cookies, analytics, etc.)? https://www.varonis.com/blog/us-privacy-laws/</td>
				<td>"HDX: terms for cookies and for mailing service: https://data.humdata.org/about/terms.

UNEP: No"</td>
				<td>No privacy policy on the original website. In HDX, there are terms for cookies and for mailing service: https://data.humdata.org/about/terms.</td>
				<td>Yes: https://www.noaa.gov/protecting-your-privacy</td>
				<td>No</td>
				<td>Yes: https://www.noaa.gov/protecting-your-privacy</td>
				<td>Yes http://www.oecd.org/privacy/</td>
				<td>Yes (vedi https://nsidc.org/about/privacy)</td>
				<td>Yes https://www.epa.gov/privacy/privacy-and-security-notice#rights</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes (https://www.wri.org/about/privacy-policy)</td>
				<td>Yes (https://climatefundsupdate.org/privacy-policy/)</td>
				<td>Yes: https://data.europa.eu/euodp/en/privacystatement</td>
				<td>Yes: https://data.europa.eu/euodp/en/privacystatement</td>
				<td>Yes: https://data.europa.eu/euodp/en/privacystatement</td>
			</tr>
			<tr>
				<td>"1.9 Do you know who are in your open data platform the Controller and Processor of the privacy data of the system? 
https://advisera.com/eugdpracademy/knowledgebase/eu-gdpr-controller-vs-processor-what-are-the-differences/ 

https://www.altalex.com/documents/news/2018/04/12/articolo-4-gdpr-definizioni"</td>
				<td>No</td>
				<td>OCHA, the system administrator of the HDX platform (inferred: it is the Controller, Google Analytics and Mixpanel are the Processors). </td>
				<td>No, inferred: NOAA is the Controller</td>
				<td>No, no</td>
				<td>Yes inferred Controller-NOAA and Processor-Google Analytics</td>
				<td>Not stated inferred Controller OECD</td>
				<td>No, Inferred: NOAA is the Controller</td>
				<td>No, inferred Controller EPA</td>
				<td>Not stated. Inferred: OECD is the Controller</td>
				<td>Not stated. Inferred: Global Footprint Network is the Controller</td>
				<td>Not stated. Inferred: WRI is the Controller</td>
				<td>Yes controller (Heinrich-Böll-Stiftung Washington, DC)</td>
				<td>"Unit C.4, ""EU Open Data and CORDIS"" of the Publications Office is the Controller

European Union Open Data Portal (EU ODP) is the Processor"</td>
				<td>"Unit C.4, ""EU Open Data and CORDIS"" of the Publications Office is the Controller

European Union Open Data Portal (EU ODP) is the Processor"</td>
				<td>"Unit C.4, ""EU Open Data and CORDIS"" of the Publications Office is the Controller

European Union Open Data Portal (EU ODP) is the Processor"</td>
			</tr>
			<tr>
				<td>1.10 Where the datasets are physically stored (country and jurisdiction)? Do you have a cloud computing platform? Do you have checked the privacy regulation of the country where the dataset are physically stored? (territoriality)</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.?Oak Ridge National Laboratory (ORNL) Distributed Active Archive Center (DAAC)</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
				<td>Not stated if they are physically stored or just online.</td>
			</tr>
			<tr>
				<td>"1.11 Do you have non-personal data?
Are you sure that are not “mixed data”?"</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
				<td>Yes. Yes.</td>
			</tr>
			<tr>
				<td>2. IPR of the dataset</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>2.1 Do you have created and generated the dataset ?</td>
				<td>Yes (UNEP)</td>
				<td>Yes. Dartmouth Flood Observatory.</td>
				<td>Yes. NOAA NCEI</td>
				<td>Yes, Oak Ridge National Laboratory (ORNL) Distributed Active Archive Center (DAAC)</td>
				<td>Yes. NOAA NCEI - NCDC</td>
				<td>Yes. OECD</td>
				<td>Yes (NSIDC)</td>
				<td>Yes NOAA NCEI</td>
				<td>Yes. OECD</td>
				<td>Yes. Global Footprint Network</td>
				<td>Yes (WRI)</td>
				<td>Yes (Climate Funds Update)</td>
				<td>Yes (Directorate-General for Communication of the European Commission)</td>
				<td>Yes (Directorate-General for Communication of the European Commission)</td>
				<td>Yes (Directorate-General for Communication of the European Commission)</td>
			</tr>
			<tr>
				<td>2.2 Are you the owner of the dataset? Who is the owner?</td>
				<td>Yes (UNEP)</td>
				<td>Yes. Dartmouth Flood Observatory.</td>
				<td>Yes. NOAA NCEI</td>
				<td>Yes, Oak Ridge National Laboratory (ORNL) Distributed Active Archive Center (DAAC)</td>
				<td>Yes. NOAA NCEI - NCDC</td>
				<td>Yes. OECD</td>
				<td>Yes (NSIDC)</td>
				<td>Yes NOAA NCEI</td>
				<td>Yes. OECD</td>
				<td>Yes. Global Footprint Network</td>
				<td>Yes (WRI)</td>
				<td>Yes (Climate Funds Update)</td>
				<td>Yes (Directorate-General for Communication of the European Commission)</td>
				<td>Yes (Directorate-General for Communication of the European Commission)</td>
				<td>Yes (Directorate-General for Communication of the European Commission)</td>
			</tr>
			<tr>
				<td>2.3 Are you using third party data with the proper authorization and license? Are the dataset free from third party licenses or patents?</td>
				<td>"Third party data are used. No licences provided.
https://preview.grid.unep.ch/index.php?preview=about&cat=3&lang=eng"</td>
				<td>Third party data are used. No licences provided.</td>
				<td>Yes: https://www.ncdc.noaa.gov/ibtracs/index.php?name=terms</td>
				<td>Third party data are used. No licences provided.</td>
				<td>Third party data are used. No licences provided.</td>
				<td>No third party data</td>
				<td>"NOAA use NSIDC data.
No licence provided."</td>
				<td>"Third party data are used. No licences provided.
https://www.ncdc.noaa.gov/data-access/land-based-station-data/land-based-datasets/global-historical-climatology-network-monthly-version-2 
"</td>
				<td>Third party data are used. No licences provided.</td>
				<td>Third party data are used. No licences provided.</td>
				<td>"Yes
The third party data used are those of the countries which provided their data."</td>
				<td>Third party data are used. No licences provided.</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
			<tr>
				<td>2.4 Are there some limitations in the national legal system of the dataset for releasing some kind of datasets with open license?</td>
				<td>"No

Geneva (Switzerland)
None or very limited activities are performed to monitor the
reuse of open data in the country
https://www.europeandataportal.eu/sites/default/files/open_data_maturity_report_2019.pdf
vedi p.71 ""Beginner"""</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td></td>
				<td>No</td>
				<td>No</td>
				<td></td>
				<td></td>
				<td></td>
				<td>No</td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>3. Licences</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td><b>3.1 Is the dataset released with an open data license ? In case of the use of CC0 have they all the right necessary for this particular kind of license (e.g., jurisdiction)?</b></td>
				<td>Available for free for non commercial purpose (https://preview.grid.unep.ch/index.php?preview=about&cat=2&lang=eng&fbclid=IwAR2swMOTGMxCFZKVptR1wGa7yY2HNz0mfYZMur_aGG3TZAfdg4IEz_qcjDs#datause)</td>
				<td>Creative Commons Attribution 4.0 International license - CC BY 4.0 (HDX)</td>
				<td>World Data Center for Meteorology policy and World Meteorological Organization's Resolution 40 policy https://www.ncdc.noaa.gov/ibtracs/index.php?name=terms</td>
				<td>Data hosted by the ORNL DAAC is openly shared, without restriction, in accordance with NASA's Earth Science program Data and Information Policy.</td>
				<td>Yes FOIA</td>
				<td>Except where additional restrictions apply as stated above, You can extract from, download, copy, adapt, print, distribute, share and embed Data for any purpose, even for commercial use. You must give appropriate credit to the OECD</td>
				<td>Yes FOIA</td>
				<td>Yes FOIA</td>
				<td>Except where additional restrictions apply as stated in the website, you can extract from, download, copy, adapt, print, distribute, share and embed data for any purpose, even for commercial use. You must give appropriate credit to the OECD.</td>
				<td>Creative Commons Attribution-ShareAlike 4.0 International License (CC-BY-SA 4.0)</td>
				<td>Creative Commons Attribution 4.0 International License (CC BY 4.0)</td>
				<td>Not stated</td>
				<td>Yes: reuse of data published on this website for commercial or non-commercial purposes is authorised provided the source is acknowledged.</td>
				<td>Yes: reuse of data published on this website for commercial or non-commercial purposes is authorised provided the source is acknowledged.</td>
				<td>Yes: reuse of data published on this website for commercial or non-commercial purposes is authorised provided the source is acknowledged.</td>
			</tr>
			<tr>
				<td>3.2 Is the clause included: "In any case the dataset can’t be used for re-identifying the person" ?</td>
				<td>No </td>
				<td>No </td>
				<td>No </td>
				<td>No </td>
				<td>No </td>
				<td>No </td>
				<td>No </td>
				<td>No </td>
				<td>No </td>
				<td></td>
				<td>No </td>
				<td>No </td>
				<td>No </td>
				<td>No </td>
				<td>No </td>
			</tr>
			<tr>
				<td><b>3.3 Is the API (in case there is) released with an open source license ?</b></td>
				<td>Yes API, no licence</td>
				<td>No API</td>
				<td>No API</td>
				<td>Yes API, no licence</td>
				<td>Yes API, no licence</td>
				<td>Yes API, no open source licence</td>
				<td>Yes API, no licence</td>
				<td>No API</td>
				<td>Yes API, no open source licence</td>
				<td>Yes API, no licence</td>
				<td>Yes API, no licence</td>
				<td>Yes API, no licence</td>
				<td>No API</td>
				<td>No API</td>
				<td>No API</td>
			</tr>
			<tr>
				<td>"3.4 Is the open data/API platform license regime compliant with your IPR policy? Do they have all the licences related to the open data platform/API software?

se non c'è l'api la domanda è riferita alla open data platform.
se non c'è licenza non si pone il problema
se c'è vedere se quello che dicono è in linea con il resto
se si risponde alla prima, la seconda va da sè"</td>
				<td>No license for the data platform</td>
				<td>No license for the data platform</td>
				<td>No license for the data platform</td>
				<td>Data platform license compliant to IPR policy but no licence for the API platform thus inferred data platform license, yes</td>
				<td>Data platform license compliant to IPR policy but no licence for the API platform thus inferred data platform license, yes</td>
				<td>Data platform/API license compliant to IPR policy , yes</td>
				<td>No, no</td>
				<td>Data platform license compliant to IPR policy and has no API, yes</td>
				<td>(API) Yes, yes</td>
				<td>No license for the data platform</td>
				<td>No license for the data platform</td>
				<td>No license for the data platform</td>
				<td>(data platform) Yes, yes: https://data.europa.eu/euodp/en/copyright</td>
				<td>(data platform) Yes, yes: https://data.europa.eu/euodp/en/copyright</td>
				<td>(data platform) Yes, yes: https://data.europa.eu/euodp/en/copyright</td>
			</tr>
			<tr>
				<td>4. Limitations on public access</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>4.1 Does the dataset concern your institutional competences, scope and finality? Does the dataset concern other public administration competences?</td>
				<td>Yes, no</td>
				<td>Yes, no</td>
				<td>Yes, no</td>
				<td>Yes, no</td>
				<td>Yes, no</td>
				<td>Yes, no</td>
				<td>Yes, no</td>
				<td>Yes, no</td>
				<td>Yes, yes: UNFCCC</td>
				<td>Yes, yes: UN</td>
				<td>"Yes 
(https://www.wri.org/about/values)
(https://www.wri.org/about/mission-goals)"</td>
				<td>"Yes
Yes (Overhead refers to expenditures from the Fund that are not directed to projects (such as administration fees))."</td>
				<td>Yes, no</td>
				<td>Yes, no</td>
				<td>Yes, no</td>
			</tr>
			<tr>
				<td>4.2 Does the dataset respect the limitations for the publication stated by your national legislation or by the EU directives ? https://project-open-data.cio.gov/policy-memo/ for USA</td>
				<td>Yes (penso di sì perchè ci sono poche limitazioni -> vedi risposta alla domanda 2.4)</td>
				<td>No open license on Dartmouth Observatory website</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td></td>
				<td>Yes</td>
				<td>Yes</td>
				<td></td>
				<td></td>
				<td></td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
			</tr>
			<tr>
				<td>4.3 Are there some limitations connected to the international relations, public security or national defence ?</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
			<tr>
				<td>4.4 Are there some limitations concerning the public interest ?</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
			<tr>
				<td>4.5 Does the dataset respect the international law limitations? https://opendatacharter.net/principles/ (?)</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes but Open data platform not linked to metadata</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
			</tr>
			<tr>
				<td>4.6 Does the dataset respect the INSPIRE law limitations for the spatial data? https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32007L0002</td>
				<td>"No
https://it.wikipedia.org/wiki/INSPIRE"</td>
				<td>Not EU dataset</td>
				<td>Not EU dataset</td>
				<td>Not EU dataset</td>
				<td>Not EU dataset</td>
				<td>Not EU dataset</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>5. Economical Conditions</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>5. Economical Conditions</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>5.1 Could the dataset be released for free ?</td>td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
				<td>Yes</td>
			</tr>
			<tr>
				<td>5.2 Are there some agreements with some other partners in order to release the dataset with a reasonable price ?</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>5.3 Does the open data platform terms of service include a clause of “non liability agreement” regarding the dataset and API provided ?</td>
				<td>Yes</td>
				<td>No</td>
				<td>No, just for links</td>
				<td>No</td>
				<td>No, just for links</td>
				<td>Yes for the dataset and API</td>
				<td>"No, just for links
NOAA.gov does not control or guarantee the accuracy, relevance, timeliness or completeness of information contained in a linked site."</td>
				<td>"Not stated in EPA 
NOAA just for links"</td>
				<td>Yes API, yes data</td>
				<td>No</td>
				<td>"Yes if (https://www.wri.org/about/open-data-commitment)

No (?)"</td>
				<td>No</td>
				<td>No</td>
				<td>Yes for the open data platform</td>
				<td>Yes</td>
			</tr>
			<tr>
				<td>5.4 In case you decide to release the dataset to a reasonable price are the limitation imposed by the new directive 2019/1024/EU respected ? Are you able to calculate the “marginal cost”? Are you able to justify the “reasonable return on investment” limited to cover the costs of collection, production, reproduction, dissemination, preservation and rights clearance? There is a national law that justify your public administration to apply the “reasonable return of investment”?</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>5.5 In case you decide to release the dataset to a reasonable price do you check the e-Commerce directive1 and regulation?</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>6. Temporary aspects</td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
				<td></td>
			</tr>
			<tr>
				<td>6.1 Do you have a temporary policy for updating the dataset ?</td>
				<td>Never (HDX)</td>
				<td>"active" =  current events are added immediately</td>
				<td>Twice weekly - Weekly (IBTrACS Project) / Daily (NOAA) </td>
				<td>Periodically</td>
				<td>No  </td>
				<td>No  </td>
				<td>No  </td>
				<td>No  </td>
				<td>No  </td>
				<td>Annually</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
			<tr>
				<td>6.2 Do you have some mechanism for informing the end-user that the dataset is updated at a given time to avoid mis-usage and so potential risk of damage ?</td>
				<td>"No
The United Nations periodically adds, changes, improves or updates the Materials on this Site without notice"</td>
				<td>No</td>
				<td>Yes, forum</td>
				<td>Yes, Email</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
			<tr>
				<td>6.3 Did you check if the dataset for some reason can’t be indexed by the research engines (e.g. Google, Yahoo, etc.) ?</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
				<td>Indexed</td>
			</tr>
			<tr>
				<td>6.4 In case of personal data, do you have a reasonable technical mechanism for collecting request of deletion (e.g. right to be forgotten)?</td>
				<td>No</td>
				<td>Yes, email (HDX)</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>Yes, email</td>
				<td>No</td>
				<td>No</td>
				<td>Yes, email</td>
				<td>No</td>
				<td>Yes (https://www.wri.org/about/privacy-policy > choices)</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
				<td>No</td>
			</tr>
		</table>
<h2>Ethical analysis</h2>
<p>In order to carry out the ethical analysis of the original datasets, we relied on the <a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/737137/Data_Ethics_Framework.pdf?fbclid=IwAR0Ebh7ZyY-PkNbfLKlATHL1VYDBHge9XLuYtX-MceYq_JZujpptendmwNA">Data Ethics Framework</a>. We organized our analysis of each dataset according to several points of view: transparency, accountability, discrimination, cognitive bias and prejudice.</p>
<p>
In particular, we tried to analyze each of these aspects organizing our analysis in four areas:
<li><b>The purpose</b>: what is the goal the dataset wants to achieve?</li>
<li><b>The process</b>: how were the data collected? </li>
<li><b>The output </b>: how was the dataset released? </li>
<li><b>Conclusion</b>: summary</li>
</p>

<h3>Droughts events 1980-2001</h3>
<p><b>Purpose</b>: this dataset is part of the wider “Global risk data platform” which also included data about other natural hazards. The purpose of the platform is to allow the visualisation of data on natural hazards.</p>
<p><b>Process</b>:  the data have been collected by merging data from different sources (that were cited on the website). In this case the sources were: a global monthly gridded precipitation dataset obtained from the Climatic Research Unit (University of East Anglia) and a GIS modeling of global Standardized Precipitation Index based on Brad Lyon (IRI, Columbia University) methodology. In this way the resulting dataset can be based on two different points of view. 
We don’t know anything from the platform about any prejudice or bias respect to the data collected, but we know that methodologies on hazards modeling were reviewed by a team of 24 independent experts selected by the World Meteorological Organization (WMO) and the United Nations Education and Scientific Cultural Organization (UNESCO).</p>
<p><b>Output</b>: the resulting dataset is not easily understandable because there is no legend to interpret the column headers (lack of guidelines). A version is not indicated and therefore consistency cannot be ascertained.
The platform provided a series of legal information about the license and the way the datasets can be used by the users (e.g. no commercial purpose). However beside this, there are no notions of discrimination and bias.</p>
<p><b>Conclusion</b>: the dataset can be considered good from an ethical point of view but we cannot say the same about its transparency, because of the lack of the legend.</p>

<h3>Global Active Archive of Large Flood Events</h3>
<p><b>Purpose</b>: The target is not declared, hence we could just infer that it is addressed to researchers. The benefit is explicitly said to be creating a unique source for large flood events. Nonetheless, since it doesn’t involve other archives, it could instead fragment the scenario. In the purpose, there is no trace of discrimination, prejudice or cognitive bias. It has a global basis.
</p>
<p><b>Process</b>: No transparency and accountability in the processing: even if sources are stated, the actual data they provided are not identifiable. Governmental sources they claim to have used are not distinguishable. No caveats nor documentation on what they have done have been provided.
</p>
<p><b>Output</b>: In the final dataset: 
<ul>
	<li>All countries have been recognised and no political discriminations have been made (e.g. Israel and Palestine). </li>
	<li>There are no personal data, but the number of deaths, when small, combined with other information as the location could lead to individuals’ names. The purpose in using deaths and displaced is to show the gravity of the flood. However, another index is also used, so this information may have been avoided.
</li>
	<li>Since it is mainly based on news, as they state, the dataset contains mainly data about major events and “first world” countries (http://floodobservatory.colorado.edu/Archives/ArchiveNotes.html). Stating just “news” as source without naming it makes impossible to check the validity of the reported datum. On the other hand, making easy to retrieve the news source could mean in some cases facilitating the identification of involved people.</li>
	</ul>
</p>
<p><b>Conclusion</b>: there aren’t prejudice and cognitive bias, but discrimination, since data focus on ‘first world’ countries and on limited sources (mainly news). Moreover, possible ethical problems arise about deaths and displaced. Nonetheless, the greatest ethical problems of the dataset are little openness (especially w.r.t. procedures) and accountability difficulties. If it wasn’t so cited in the academic world, it wouldn’t seem enough reliable.

</p>

<h3>International Best Track Archive for Climate Stewardship (IBTrACS) Project, Version 4
</h3>
<p>The dataset can be considered as perfect from an ethical point of view because it doesn’t contain prejudice, cognitive bias or discrimination and everything is well documented: purpose and user need, data provenance, caveats and usage information (available in the technical documentation), field names explanation, ways to provide feedback.</p>

<h3>GFEDv4 (Global Fire Emissions Database, Version 4)</h3>
<p><b>Purpose</b>: the data has a clear user need which is to provide global estimates of monthly burned area, monthly emissions and fractional contributions of different fire types, daily/3-hourly fields to scale the monthly emissions to higher temporal resolutions, and data for monthly biosphere fluxes which could be used for large-scale modeling studies. 
</p>
<p><b>Process</b>:  from a legal point of view the data is on point. The collection of the data used is done without any discrimination, cognitive bias or prejudice as inferred on the website (https://daac.ornl.gov/VEGETATION/guides/fire_emissions_v4.html) making use of the available data from other sources and theirs (Satellite information) to create a global view of the situation. The only note could be that they make no mention of licences for use of data from others.
</p>
<p><b>Output</b>: the data used serves exactly the need of the user they want to satisfy and is restricted to its purpose of creation. The dataset released at the end is available in an open format and free for reuse on an API platform. The dataset will in no way harm any individual person,community or country or public interest even with new events registered from the documentation. There is a clear description of the composition of the database again free from any discrimination,cognitive bias or prejudice.
</p>
<p><b>Conclusion</b>: we can in summary say that the dataset from an ethical point of view is clean to an extent.
</p>

<h3>Climate at a Glance - Time Series Graphs of Temperature Anomalies</h3>
<p><b>Purpose</b>: they don’t state clearly what is the purpose of the dataset created or the user need to which they are responding to but it is inferred that they want to make known to all what is the situation of the temperature anomalies in the world over the years</p>
<p><b>Process</b>:  for the creation of the final dataset, they combine data from two resources (Global Historical Climatology Network-Monthly (GHCN-M) data set and International Comprehensive Ocean-Atmosphere Data Set (ICOADS)) known for  carrying out quality controls on their data for good practice. Their choice of sources is understood which goes to rhyme with the purpose and helps answer strictly to the user's need identified. Therefore no discrimantion, prejudice or cognitive bias.
</p>
<p><b>Output</b>:  the dataset released from this combination is made available to all in an open format having all the information it had planned to deliver without any wrong ethical aspect. Good explanation of the basis of the results found in the dataset.
</p>
<p><b>Conclusion</b>: it can be therefore considered that the dataset is ethically correct.</p>


<h3>Threatened species</h3>
<p><b>Purpose</b>: the purpose of the dataset is clearly stated and it is to show the numbers of known species (or assessed) and threatened species with the aim of indicating the state of mammals, birds, freshwater fish, reptiles, amphibians, vascular plants, mosses, lichens and invertebrates. This purpose has no issue of discrimination, cognitive bias or prejudice because most especially it goes for world information and also consider information from the various national Delegates. 
</p>
<p><b>Process</b>:  the process of collection and analysis of the data to create the dataset is done by updating and revising certain information from the comments of national Delegates. The basis of this act is not well stated on the website. So, it could be inferred that  there may be some cognitive bias in the decision making.
</p>
<p><b>Output</b>: the released dataset is done through an API free to all but it is stated on the website that the interpretation should take in consideration the possibility of non exactness of the various values. Also they talk of the possibility of biased results due to overestimation of some of the incompletely evaluated groups of species likely to be threatened in certain countries.
</p>
<p><b>Conclusion</b>: the level of ethical correctness of this data set is not completely good because in the end we have a dataset of which some values may be wrong due to certain actions during its creation.
</p>

<h3>Sea Ice and Snow Cover Extent</h3>
<p><b>Purpose</b>: the purpose of providing a tool to see the sea ice extent over years is achieved: users can generate and examine graphs and statistics on ice and snow, or download the data to populate spreadsheets for further analysis.</p>
<p><b>Process</b>: the purpose of providing a tool to see the sea ice extent over years is achieved: users can generate and examine graphs and statistics on ice and snow, or download the data to populate spreadsheets for further analysis.</p>
<p><b>Output</b>: the result is a tool for browsing the sea ice extent from 1979 to 2020 for the Northern Hemisphere, Southern Hemisphere, and the Globe. Data can be observed monthly or annually. Very poor documentation, no information about restriction of use, bias and discrimination.
</p>
<p><b>Conclusion</b>: the dataset seems to be free from cognitive bias, however very few documentation is provided.
</p>

<h3>Climate Change Indicators: U.S. and Global Precipitation</h3>
<p><b>Purpose</b>:  the purpose of creation of the dataset is clear and has no ethical distortion for the precise user need which was to point out all the precipitation anomalies over the given period selected.
</p>
<p><b>Process</b>: during the creation of the dataset they make use of all possible resources to create a well informed database on the subject matter. The good aspect is the fact that during the creation they make use of bias correction software ( automated bias correction software) which helps identify and eliminate biases. Also the personal intervention of the staff, scientists and data quality tests are done in the light of excluding any ethical compromise. 
</p>
<p><b>Output</b>: the datasets released are well documented and are available without charge through NCEI's anonymous FTP service. The information it contains is of good quality and satisfies the user's need and purpose of creation.
</p>
<p><b>Conclusion</b>: this dataset can be consequently considered ethically correct.
</p>

<h3>Greenhouse Gas Emissions
</h3>
<p><b>Purpose</b>: Target and purpose are inferable but not explicitly stated. It is not clear if data is referred just to countries of OECD. In case, this could cause cognitive bias.

</p>
<p><b>Process</b>: The provenance of the single datum is not stated so there are no ways to compare the dataset with the original sources and detect possible errors. No caveats or technical documentation to make the procedure reproducible have been made public. 

</p>
<p><b>Output</b>: Even though apparently you are downloading the result of your specific query, the dataset could include unrequested data, e.g. downloading data including LULUFC leads anyway to a dataset that contains at the beginning data excluding LULUFC. Moreover, internal choices have not been clarified: in formats as CSV, values appear to be repeated in two columns; the codes for pollutants, variables, units and powercodes aren’t explained; reference and flags, despite the specific column, are overall unused. Finally, the fact that the countries are those of OECD is just inferable and has not been explicitly stated.

</p>
<p><b>Conclusion</b>: There is not properly discrimination or cognitive bias, but the vision is definitely partial because the set of countries is limited and in general the procedure and the output are not enough transparent and accountable.
</p>

<h3>National Footprint and Biocapacity Accounts 2019 Public Data Package
</h3>
<p><b>Purpose</b>: The target is as broad as possible, with the purpose of making available the data to the public. No discrimination, prejudice or cognitive bias can be detected at this stage.

</p>
<p><b>Process</b>: The methodology is accountable and transparent.
 
</p>
<p><b>Output</b>:  Everything is explained in the related paper. You are also given the possibility to access the paper of the previous versions to spot the differences. Their selection of countries could be said politically discriminant (e.g. Israel is present, while Palestine absent).
 
</p>
<p><b>Conclusion</b>: The peculiarity of the dataset is the purpose of making it available to everyone. Everything is accountable and transparent. There are no discrimination, prejudice or cognitive bias in any phase, except for the choice of the countries, which seems to take a political stand.
</p>

<h3>CAIT Paris Contributions Data</h3>
<p><b>Purpose</b>: the purpose of the dataset is to provide a collection of data about the countries which submitted the Paris Agreement in 2015-2016 and their commitments in the field of climate change. 
The  purpose is achieved because the structured data from the CAIT Paris Contributions Map enables users to explore, compare, and assess the greenhouse gas mitigation plans in each country's Intended Nationally Determined Contribution (INDC).
 </p>
<p><b>Process</b>: after the submission of the Paris Agreement, countries decided to release public outlines of actions they intended to take in order to achieve the goal. The data are structured according to a framework based on several protocols and standards listed on the website. 
The list of the adhesive countries and the license are provided on the first sheet of the dataset.
</p>
<p><b>Output</b>: the output of the process is an interactive map accessible through the platform. By clicking on almost every country (except for Libya for which we don’t have any document submitted), the user can see the information about the agreement for each country separately from the others (the same information provided in the dataset).
The data are about the commitments of each country against climate change, so we can infer that they do not contain prejudices, discriminations and biases.
What about Libya? This is the only case that can create a bias.
A second issue is that the downloadable version of the dataset is updated to 2016, while the user can find on the online platform the data updated to 2019.
</p>
<p><b>Conclusion</b>: the dataset is almost complete from an ethical point of view, except for information about Libya. The API is easily accessible and transparent, but there is a discrepancy between the downloadable version and the online one.
</p>

<h3>Cumulative data on the contributors of climate finance</h3>
<p><b>Purpose</b>: the purpose of the platform is to present cumulative data on the contributors of climate finance from the multilateral climate change funds monitored by the platform itself. The purpose is achieved.
</p>
<p><b>Process</b>: We don’t know who is the owner of the platform and it is not clear what does it mean that “the data are presented for each multilateral climate change funds it tracks”.
The platform collects the data in the following way: seeks information from different sources and then seeks correspondence with fund managers in order to verify the collected information. Despite this, it is stated that the platform receives verification for almost all funds and it is not indicated which are the authorities that verifies them. All these things can lead to an issue for what concerns reliability.
A positive point is that the platform tracked governed funds focused on climate change and based its dataset on that funds (reliability and transparency).
From the dataset we can infer that the analysed countries are mainly from Europe and Central Asia; no explanations about the choice of the countries (maybe chosen the ones that devoted a good part of the funds to climate change).
No further info about any kind of prejudice or discrimination provided by the platform.
</p>
<p><b>Output</b>: the resulting output is user friendly and easily accessible.
</p>
<p><b>Conclusion</b>: it is not very clear who verify the funds and how much accurate data are (not very reliable). We can notice that the greater amount of data come from Europe and Central Asia. The resulting API is easily accessible.
</p>


<h3>Special Eurobarometer 313: Europeans’ attitudes towards climate change
</h3>
<p><b>Purpose</b>: The purpose of the dataset is to understand what European citizens think about the climate change situation and what are their expectations for the future.
</p>
<p><b>Process</b>: to be able to accomplish their aim, the opinions of the citizen were collected carrying out surveys which results have been later analysed.
The survey method and questions are described and documented and it is understandable that there is no ethical distortion.
</p>
<p><b>Output</b>: the dataset released contains all the countries of the EU and all the questions and answers are reported without any change. The data collected was used strictly for the purpose of the dataset and there were possibilities of not answering certain questions. So, the possibility of prejudice is excluded and since everybody could take part in the survey we can say there is no discrimination. From the results there is no cognitive bias since there is no interpretation of the results of the dataset just a publication.
</p>
<p><b>Conclusion</b>: </p>

<h3>Special Eurobarometer 409: Climate change</h3>
<p><b>Purpose</b>: the purpose of the dataset is to understand what European citizens think of the climate change situations and what are their expectations.
</p>
<p><b>Process</b>: to be able to accomplish their aim, they carry out surveys to collect opinions of the citizens and analyse the results. The survey method and questions are described and documented and it is understandable that there is no ethical distortion.
</p>
<p><b>Output</b>: the dataset released contains all the countries of the EU and all the questions and answers are reported without any change. The data collected was used strictly for the purpose of the dataset and there were possibilities of not answering certain questions. So, the possibility of prejudice is excluded and since everybody could take part in the survey we can say there is no discrimination. From the results there is no cognitive bias since there is no interpretation of the results of the dataset just a publication.

</p>
<p><b>Conclusion</b>: it can be said that, some questions included in the dataset went to individuate certain aspects of the life of the citizens (like their economic status) without really giving a reason for this. So, we will say that the dataset to an extent is not ethically correct because data analists can nevertheless infer much information from the personality of European citizens and their reactions to climate change.

</p>


<h3>Special Eurobarometer 490: Climate change</h3>
<p><b>Purpose</b>: The purpose is explicitly expressed to be understanding European citizens opinions on climate change, in order to shape EU future climate and energy policies.
</p>
<p><b>Process</b>: The survey method and questions are documented and further described in a specific paper. The surveyed had the possibility to not answer.

</p>
<p><b>Output</b>: The final dataset is free from ethical distortion. However, it is unclear the purpose of questions related to the economical status or the level of instruction of the individual in such a context; hence, they don’t seem totally free of discriminatory aspects.
</p>
<p><b>Conclusion</b>: Everything is accountable and transparent. There are no discrimination, prejudice or cognitive bias, a part for the unclear purpose of some personal questions apparently unrelated to the context.
</p>

<h2>Technical analysis</h2>
<p>At this stage we analyzed our datasets under the technical point of view. We examined the available formats, the presence of metadata, the URIs and the provenance. Below the result:</p>
<table>
	<tr>
		<th></th>
		<th>Droughts events 1980-2001</th>
		<th>Global Active Archive of Large Flood Events</th>
		<th>International Best Track Archive for Climate Stewardship (IBTrACS) Project, Version 4</th>
		<th>GFEDv4 (Global Fire Emissions Database, Version 4)</th>
		<th>Climate at a Glance - Time Series Graphs of Temperature Anomalies</th>
		<th>Threatened species</th>
		<th>Sea Ice and Snow Cover Extent</th>
		<th>Climate Change Indicators: U.S. and Global Precipitation</th>
		<th>Greenhouse Gas Emissions</th>
		<th>National Footprint and Biocapacity Accounts 2019 Public Data Package</th>
		<th>CAIT Paris Contributions Data</th>
		<th>Cumulative data on the contributors of climate finance</th>
		<th>Special Eurobarometer 313: Europeans’ attitudes towards climate change</th>
		<th>Special Eurobarometer 409: Climate change</th>
		<th>Special Eurobarometer 490: Climate change</th>
	</tr>
	<tr>
		<td><b>Format</b></td>
		<td>dbf, shp, shx (UNEP)

CSV (HDX)</td>
		<td><b>XLSX</b>, XML, MapInfo TAB, shapefiles</td>
		<td>netCDF, <b>CSV</b>, shapefiles</td>
		<td>CSV (Comma-separated values),  HDF (Hierarchical Data Format)</td>
		<td>XMS (Microsoft eXtended Memory Specification),  CSV (Comma-separated values),  JSON (JavaScript Object Notation ), XML (Extensible Markup Language)</td>
		<td>XLS, CSV, SDMX(XML)</td>
		<td>CSV, XML, JSON</td>
		<td>XLS</td>
		<td>XLS, CSV, PX, <b>SDMX (XML)</b></td>
		<td><b>CSV</b></td>
		<td>XLSX</td>
		<td>XLSX</td>
		<td>XLSX</td>
		<td>XLS</td>
		<td><b>XLS</b></td>
	</tr>
	<tr>
		<td><b>Metadata</b></td>
		<td>UNEP
Metadata format: ISO19115
https://preview.grid.unep.ch/index.php?preview=data&events=droughts&evcat=1&lang=eng

Download
http://preview.grid.unep.ch/geonetwork/srv/en/csw?SERVICE=CSW&VERSION=2.0.2&outputSchema=http://www.isotc211.org/2005/gmd&outputFormat=application/xml&REQUEST=GetRecordById&ID=8a56e45c-e86d-4eb1-ae2e-6d46ebec81d3

HDX
https://data.humdata.org/dataset/global-droughts-events-1980-2001</td>
		<td>No</td>
		<td>ISO 19115-2/C01552: https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C01552;view=iso</td>
		<td>https://daac.ornl.gov/VEGETATION/guides/fire_emissions_v4.html</td>
		<td>https://www.climate.gov/maps-data/dataset/global-temperature-anomalies-graphing-tool</td>
		<td>https://stats.oecd.org/OECDStat_Metadata/ShowMetadata.ashx?Dataset=WILD_LIFE&Lang=en</td>
		<td></td>
		<td>EPA: https://www.epa.gov/climate-indicators/climate-change-indicators-us-and-global-precipitation     NOAA: ISO 19115-2 Metadata https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C00835#</td>
		<td>Yes: https://stats.oecd.org/OECDStat_Metadata/ShowMetadata.ashx?Dataset=AIR_GHG&Lang=en</td>
		<td>No ? paper</td>
		<td>https://www.wri.org/resources/data-sets/cait-paris-contributions-data</td>
		<td>https://climatefundsupdate.org/about-us/notes-and-methodology/</td>
		<td>https://data.europa.eu/euodp/it/data/dataset/S942_71_1_EBS313</td>
		<td>https://data.europa.eu/euodp/it/data/dataset/S1084_80_2_409</td>
		<td>https://data.europa.eu/euodp/en/data/dataset/S2212_91_3_490_ENG</td>
	</tr>
	<tr>
		<td><b>URI</b></td>
		<td>UNEP
link scaricabile alla cartella zip

HDX
https://data.humdata.org/dataset/f5e8b21e-bb71-40e3-8129-5378ebc42e33/resource/222389aa-9089-428d-8d60-1f6895df6618/download/dr-events.csv</td>
		<td>http://floodobservatory.colorado.edu/Version3/FloodArchive.xlsx ?</td>
		<td>https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r00/access/csv/ibtracs.since1980.list.v04r00.csv ?</td>
		<td>http://www.globalfiredata.org/downloads/chart_5e8dc22f20efd.txt  / http://www.globalfiredata.org/downloads/chart_5e8dbb6d0359e.txt  /  http://www.globalfiredata.org/downloads/chart_5e8dbd0940b57.txt</td>
		<td>https://www.ncdc.noaa.gov/cag/global/time-series/globe/land_ocean/1/2/1880-2020/data.json   </td>
		<td>https://stats.oecd.org/restsdmx/sdmx.ashx/GetData/WILD_LIFE/TOT_KNOWN+TOT_KNOWN_IND+CRITICAL+CRITICAL_IND+ENDANGERED+ENDANGERED_IND+VULNERABLE+VULNERABLE_IND+THREATENED+THREATENED_IND+THREAT_PERCENT+IND_PERCENT.MAMMAL+BIRD+REPTILE+AMPHIBIAN+FISH_TOT+MARINE_F+FRESHW_F+VASCULAR_PLANT+MOSS+LICHEN+INVERTEB.AUS+AUT+BEL+CAN+CHL+CZE+DNK+EST+FIN+FRA+DEU+GRC+HUN+ISL+IRL+ISR+ITA+JPN+KOR+LVA+LTU+LUX+MEX+NLD+NZL+NOR+POL+PRT+SVK+SVN+ESP+SWE+CHE+TUR+GBR+USA+NMEC+BRA+COL+CRI+RUS/all?</td>
		<td>https://www.ncdc.noaa.gov/snow-and-ice/extent/sea-ice/N/2.xml</td>
		<td>https://www.epa.gov/sites/production/files/2016-08/precipitation_fig-2.csv</td>
		<td>?</td>
		<td>Not available ?</td>
		<td>https://www.wri.org/resources/data-sets/cait-paris-contributions-data#
(mail requested)</td>
		<td>https://climatefundsupdate.org/wp-content/uploads/2019/04/CFU-Website-Master-27-Feb-2019.xlsx</td>
		<td>https://data.europa.eu/euodp/it/data/dataset/S942_71_1_EBS313

DOWNLOAD
http://data.europa.eu/88u/dataset/S942_71_1_EBS313</td>
		<td>http://data.europa.eu/88u/dataset/S1084_80_2_409  

DOWNLOAD
https://ec.europa.eu/commfrontoffice/downloadODP/?6F0F875774E39C6DC9BFA1FFAB49AE81</td>
		<td>http://data.europa.eu/88u/dataset/S2212_91_3_490_ENG</td>
	</tr>
	<tr>
		<td><b>Provenance</b></td>
		<td>UNEP
https://preview.grid.unep.ch/index.php?preview=data&events=droughts&evcat=1&lang=eng

HDX
https://data.humdata.org/dataset/global-droughts-events-1980-2001</td>
		<td>http://floodobservatory.colorado.edu/Archives/index.html</td>
		<td>https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/v04r00/access/csv/</td>
		<td>http://www.globalfiredata.org/analysis.html</td>
		<td>https://www.ncdc.noaa.gov/cag/global/time-series</td>
		<td>https://stats.oecd.org/Index.aspx?DataSetCode=WILD_LIFE</td>
		<td>NOAA
https://www.climate.gov/maps-data/dataset/snow-or-ice-extent-graphing-tool

il dataset è disponibile solo sul NOAA; non riusciamo a trovarlo su UNSIDC</td>
		<td>https://www.epa.gov/climate-indicators/climate-change-indicators-us-and-global-precipitation</td>
		<td>https://stats.oecd.org/Index.aspx?DataSetCode=AIR_GHG#</td>
		<td>https://www.footprintnetwork.org/licenses/public-data-package-free/</td>
		<td>https://www.wri.org/resources/data-sets/cait-paris-contributions-data#</td>
		<td>https://climatefundsupdate.org/data-dashboard/#1541245664327-538690dc-b9a8</td>
		<td>https://data.europa.eu/euodp/it/data/dataset/S942_71_1_EBS313</td>
		<td>https://data.europa.eu/euodp/it/data/dataset/S1084_80_2_409</td>
		<td>https://data.europa.eu/euodp/en/data/dataset/S2212_91_3_490_ENG ? or landing page?</td>
	</tr>
</table>
<h2>Mashup and output datasets</h2>
<p>From our original datasets, having performed all the analysis and verifications needed, we then created an overview of the various information we needed to retrieve from them based on questions we wish to answer to following our purpose and scenario. From this point we then moved to the extraction of data from the datasets using Python as our programming language. The various codes we used in this process can be found in the “code” folder. In this folder there are three folders: 
<ol>
	<li>1-data-extraction: in this folder you will find the python file <code>base-file.py</code> which is a condesé of our 15 functions we used to extract data from our original datasets. There is also the file <code>countries.py</code> which contains the python function used to extract the various countries and their ISO codes present in our original datasets, in order to manage the mistakes and the exceptions.</li>
	<li>2-py-to-xml: in this folder you have the three functions we used to create our output XML datasets.</li>
	<li>3-xml-to-json: in this folder you find the python files we used to create the json files useful for the visualizations, starting from our XML datasets.</li>
</ol> 	
</p>
<p>
Through the extraction and creation processes we produced three new datasets in XML format, which contain also their metadata. These datasets were used for the future points of our project and are collected in the “xml” folder. These datasets are: 
<ol>
	<li>natural_events.xml</li>
	<li>impact_and_commitments.xml</li>
	<li>eu_opinions-xml</li>
</ol> 
</p>
<p>Here below you have a table of the output datasets and the original datasets used to create each of them.</p>
<table>
	<tr>
		<th>Output Dataset</th>
		<th>Origin Datasets</th>
	</tr>
	<tr>
		<td>natural_events.xml</td>
		<td>Droughts events 1980-2001,
Global Active Archive of Large Flood Events, 
International Best Track Archive for Climate Stewardship (IBTrACS) Project, Version 4, 
GFEDv4 (Global Fire Emissions Database, Version 4)
Climate at a Glance - Time Series Graphs of Temperature Anomalies, 
Climate Change Indicators: U.S. and Global Precipitation, 
Sea Ice and Snow Cover Extent.</td>
	<tr>
		<td>impact_and_commitments.xml</td>
		<td>Greenhouse Gas Emissions, 
National Footprint and Biocapacity Accounts 2019 Public Data Package, 
CAIT Paris Contributions Data, 
Cumulative data on the contributors of climate finance.</td>
	</tr>
	<tr>
		<td>eu_opinions.xml</td>
		<td>Special Eurobarometer 313: Europeans’ attitudes towards climate change, 
Special Eurobarometer 409: Climate change, 
Special Eurobarometer 490: Climate change.</td>
	</tr>
</table>
<p>The datasets have been created according to the “FAIR Principles”, so we would say that they are free of any quality, legal, technical and ethical problems.</p>
<p>We decided to release our datasets under the license CC-BY-SA 4.0.</p>

<h3>Processing Issues</h3>
<p>During the extraction of data from our original datasets, we encountered certain difficulties which we wish to make mention of for each dataset.</p>
<ul>
	<li>Droughts events 1980-2001</li> 
	<li>Global Active Archive of Large Flood Events</li> 
	<li>International Best Track Archive for Climate Stewardship (IBTrACS) Project, Version 4</li> 
	<li>GFEDv4 (Global Fire Emissions Database, Version 4)</li>
	<li>Climate at a Glance - Time Series Graphs of Temperature Anomalies</li> 
	<li>Climate Change Indicators: U.S. and Global Precipitation</li> 
	<li>Sea Ice and Snow Cover Extent</li>
	<li>Greenhouse Gas Emissions</li> 
	<li>National Footprint and Biocapacity Accounts 2019 Public Data Package</li> 
	<li>CAIT Paris Contributions Data</li> 
	<li>Cumulative data on the contributors of climate finance</li>
	<li>Special Eurobarometer 313: Europeans’ attitudes towards climate change</li> 
	<li>Special Eurobarometer 409: Climate change</li> 
	<li>Special Eurobarometer 490: Climate change</li>
</ul>
<h2>Sustainability of the datasets over time</h2>
<p>The CCODe project is the outcome of an academic project at the University of Bologna. Thus, it won’t be maintained. Nonetheless the resulting datasets are based on other datasets that were originally collected by larger organizations and many of them are actively updated. We provided the links in the “General analysis” section, so that anyone can compare our datasets with the original ones.</p>
<p>We invite you to notify us in case you find errors or ways to improve our work; we provided the email contact in the metadata of the datasets.</p>
<p>In order to make our datasets easily reusable, we have indeed completed them with their metadata following DCAT_AP (v 2.0.0).</p>
<p>Moreover we provided the python codes that we used to extract the data of our interest and to produce the final xml and json files. They are freely available for further reuse, as long as the license is respected.</p>
<p>Everything is protected by the CC-BY-SA 4.0 license, which allows many uses of the work, provided that the creator is cited and the same license is maintained for the derivative works. See the specification for the use, on <a href=”https://creativecommons.org/licenses/by-sa/4.0/”>Creative Commons website</a>. Please cite us as “Del Bene R., Hamvegam M. L. S., Pizzicori A. (2020) CCODe”.</p>
<p>If the project was financed, for a further implementation it would be useful to maintain the current datasets and enlarge them with data related to the missing years. It could also be desirable to cross-check in new ways our datasets, to make unexpected knowledge emerge.</p>

<h2>Visualizations</h2>
<p>At the beginning of our work, we formulated some hypotheses, starting from various questions with the final aim to decide how to intersect data.</p>
<p>We tried to reproduce this mind map in the final visualization section, organizing it in three categories, one for each dataset. Our purpose was to guide the user in the exploration of our data.</p>
<p>Since a part of the data was collected on a global scale and another on a country-base scale, we diversify our charts following the same approach.</p>
<p><a href=”https://www.highcharts.com/demo”>Highchart</a> is the JavaScript library we used to create the charts. This required the implementation of JSON files specifically formatted for the purpose.</p>
<p>Only the visualization of the map was created using another library, <a href=”https://datamaps.github.io/”>DataMaps</a>, which allows us to create a choropleth map, to explore the evolution of the events over time.</p>

<h2>Metadata and RDF assertion</h2>

<h2>Conclusion</h2>
<p>Brainstorming ideas for the project, we all found ourselves concerned about climate change and hopeful that data could be an answer in representing it. Therefore, our initial question was: how evident is the problem of climate change?</p>
<p>This initial doubt lead to asking ourselves: how do countries behave in terms of emissions, one of the main causes of the phenomenon, and how do they commit against it? What is the perception of the problem from the citizens’ side?</p>
<p>Of course, the different time spans of the datasets and, in the case of the opinions, of a global spatial coverage influenced the output, which lacks for this reason of precision. Moreover, we discovered there could be external factors that condition data, as for example w.r.t. emissions, for which a country can balance its accounts investing to fight climate change.</p>
<p>Nonetheless, some phenomena are evident:
<ul>
<li>Extreme natural events as droughts and wildfires have been increasing, even though not impressively, given the limited time span;</li>
<li>With a larger range of years, the climb is highly evident, as it happens with temperature and sea ice extent anomalies. Clearly their trends are inversely proportional;</li>
<li>During the latest years, footprint and emissions are overall decreasing and biocapacity is growing, even though still on a small scale. Could it be interpreted as a sign of the current awareness?</li>
<li>There is a marked distinction between first-world and third-world countries, which is evident by the magnitude of their emissions and by the amount of deposited funds;</li>
<li>The perception and the reaction of European citizens to climate change saw a negative trend from 2009 and 2013, while in 2019 the awareness is more spread, probable result of the highlighting of the problem in the past years.</li>
</ul></p>
<p>Some of these outcomes proved our hypothesis; some others were unexpected, as for example the high amount of each natural event, China’s official “low” account of emissions and the citizens’ perception's negative change in 2013. Overall, we thought that data could make emerge a knowledge that is still to much ignored and we were proved in this sense right.</p>

