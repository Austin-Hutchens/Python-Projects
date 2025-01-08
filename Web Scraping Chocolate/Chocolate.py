# Importing required libraries
from bs4 import BeautifulSoup  # For parsing the HTML content
import requests  # For making HTTP requests to fetch the webpage
import pandas as pd  # For creating and manipulating DataFrames
import matplotlib.pyplot as plt  # For creating visualizations like histograms and scatterplots
import numpy as np  # For numerical operations like fitting a line of best fit

# URL of the webpage that contains chocolate ratings
url = 'https://content.codecademy.com/courses/beautifulsoup/cacao/index.html'

# Sending a GET request to the URL and storing the response
response = requests.get(url)

# Creating a BeautifulSoup object to parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all tags containing the ratings of the chocolate bars
ratings_tag = soup.find_all(attrs={'class': 'Rating'})
ratings = []  # List to store ratings as floats

# Loop through the rating tags (skipping the first one) and extract the rating as a float
for score in ratings_tag[1:]:
  score = float(score.get_text())  # Convert the text content to a float
  ratings.append(score)  # Add the rating to the ratings list

# Uncomment the line below if you'd like to see the ratings list
# print(ratings)

# Creating a histogram to visualize the distribution of ratings
plt.hist(ratings)
plt.show()  # Display the histogram

# Select all tags containing company names (chocolate companies)
companies = soup.select('.Company')
company_names = []  # List to store the company names

# Loop through the company tags (skipping the first one) and extract the company names
for names in companies[1:]:
  names = names.get_text()  # Extract the text content (company name)
  company_names.append(names)  # Add the company name to the list

# Uncomment the line below if you'd like to see the company names list
# print(company_names)

# Create a DataFrame with columns for company names and ratings
chocbars_df = pd.DataFrame({
  'Company': company_names,  # Company names as a column
  'Ratings': ratings  # Ratings as a column
})

# Uncomment the line below if you'd like to see the DataFrame
# print(chocbars_df)

# Group the DataFrame by 'Company' and calculate the mean rating for each company
mean_ratings = chocbars_df.groupby("Company").Ratings.mean()

# Get the top 10 companies with the highest average ratings
ten_largest  = mean_ratings.nlargest(10)

# Uncomment the line below if you'd like to see the top 10 companies
# print(ten_largest)

# Select all tags containing cocoa percentage information
cocopercent = soup.select('.CocoaPercent')
percentcoco = []  # List to store cocoa percentages

# Loop through the cocoa percentage tags (skipping the first one) and extract the percentages
for coco in cocopercent[1:]:
  coco = coco.get_text()  # Extract the text content (percentage)
  percentcoco.append(coco)  # Add the percentage to the list

# Clean the cocoa percentages by removing the '%' symbol
stripped_cocoapercent = [values.replace('%', '') for values in percentcoco]

# Convert the cocoa percentages to floats
strippedfloat_cocoapercent = [float(num) for num in stripped_cocoapercent]

# Add the cleaned cocoa percentages as a new column to the DataFrame
chocbars_df['CocoaPercentage'] = strippedfloat_cocoapercent

# Uncomment the line below if you'd like to see the updated DataFrame
# print(chocbars_df)

# Create a scatterplot to visualize the relationship between cocoa percentage and rating
plt.scatter(chocbars_df.CocoaPercentage, chocbars_df.Ratings)
plt.clf()  # Clear the current plot to prepare for the next one

# Fit a line of best fit to the data and plot it
z = np.polyfit(chocbars_df.CocoaPercentage, chocbars_df.Ratings, 1)
line_function = np.poly1d(z)  # Create the line function
plt.plot(chocbars_df.CocoaPercentage, line_function(chocbars_df.CocoaPercentage), "r--")

# Show the scatterplot with the line of best fit
plt.show()

