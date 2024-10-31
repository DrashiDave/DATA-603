# Chicago Crime Data Analysis

This project analyzes crime patterns in Chicago using Apache Spark to manage and process the data efficiently, alongside Python libraries like Pandas and Matplotlib for visualization. By exploring Chicago’s public crime dataset from the last ten years, the project aims to identify significant trends in crime frequency, peak hours, and prevalent crime types, helping to better understand public safety concerns.

## Data Source

The crime data is sourced from the [Chicago Data Portal API](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/data), with records available from 2001 to the present. Data is retrieved directly from the API and then loaded into Spark for distributed processing.

## Requirements

To run this project, the following are needed:
- **Software**: 
  - Apache Spark
  - Python 3.x
- **Python Libraries**: 
  - `pandas`
  - `requests`
  - `pyspark`
  - `matplotlib`

Install the required Python libraries with:
```bash
pip install pandas requests pyspark matplotlib
```

## Project Structure
- **notebooks/**: Contains the main Jupyter Notebook, crime_analysis.ipynb, which holds all the code and explanations for each analysis step.
- **README.md**: Project documentation.
  
## Steps to Run the Project
- **Data Loading:** Data is fetched from the API and initially loaded into a Pandas DataFrame for quick inspection, then saved as a CSV file if needed.
- **Spark DataFrame Processing:** The saved CSV file is loaded into a Spark DataFrame, enabling efficient handling of large volumes of data.
- **Data Cleaning:** Using Spark transformations, the data is cleaned by removing null values, converting date columns to the appropriate type, filtering for data from the last ten years, and removing non-criminal offenses. Similar crime types are merged to standardize categories.
- **Analysis and Visualization:** Key insights are derived by examining yearly trends, identifying the peak hours for crimes, and finding the most frequent crime types. Spark DataFrames are converted to Pandas for final visualizations, and Matplotlib is used to create line and bar charts.

## Results
The analysis reveals an overall trend in Chicago’s crime frequency over the last decade, with a detailed year-by-year examination showing fluctuations likely due to various social factors. The peak crime hours indicate specific times when law enforcement presence might be most needed, while the top ten crime types, visualized in a bar chart, provide a snapshot of the city’s most common criminal activities, underscoring key areas for public safety initiatives.

## License
This project is licensed under the MIT License.
