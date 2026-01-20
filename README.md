Uploaded on Render: https://census-api-wgyi.onrender.com/

Note: If using a mobile device, try landscape mode. 

This Census API project allows users to enter a zipcode and a year, or a range of years, and visualize various statistics related to human geography. A single year is rendered as a bar graph, while ranges of years are rendered as time-series line graphs. Additionally, users may download a .csv file with the tabulated data. This API is more user-friendly than manually pulling and aligning Census numbers. 

INSTRUCTIONS:

1. Enter a zipcode and set a year or range of years using the slider.
2. Click "Pull Data" and wait for the page to finish loading. This step may take some time when querying large ranges due to the structure of the Census API, but should not exceed 30 seconds.
3. Select a statistic, then click "Visualize" to open a new page containing the relevant graph. The URL should be consistent for future use (untested). 
4. Repeat step 3 with the same zipcode and range of years to instantly view other statistic.
5. Click "Export CSV" to download a spreadsheet of the requested data, including all visualizable statistics plus some extras.

The data is pulled from the U.S. Census Bureau's 5-year ACS Surveys. All numbers are estimates - the exact methodology and margins of error can be found at census.gov/programs-surveys/acs/methodology.html.

Although this project was primarily intended as a portfolio showcase and educational venture, if this tool ends up being useful to you in some way, I am open to adding additional statistic based on demand - there are many more available in the survey. 

Inquiries welcome at:

harrisonabramsohn@gmail.com 

Future updates:

- Error handling
- Update bar graph color scales to color-blind friendly 
- Group busier line graphs into easier-to-parse sets
- Add variables as needed
- Fix UI on mobile portrait 