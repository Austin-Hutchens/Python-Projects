from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


url = 'https://content.codecademy.com/courses/beautifulsoup/cacao/index.html'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

ratings_tag = soup.find_all(attrs={'class': 'Rating'})
ratings = []

for score in ratings_tag[1:]:
  score = float(score.get_text())
  ratings.append(score)

#print(ratings)

plt.hist(ratings)
plt.show()

companies = soup.select('.Company')
company_names = []

for names in companies[1:]:
  names = names.get_text()
  company_names.append(names)

#print(company_names)

chocbars_df = pd.DataFrame({
  'Company': company_names,
  'Ratings': ratings
})

#print(chocbars_df)

mean_ratings = chocbars_df.groupby("Company").Ratings.mean()
ten_largest  = mean_ratings.nlargest(10)
#print(ten_largest)


cocopercent = soup.select('.CocoaPercent')
percentcoco = []
for coco in cocopercent[1:]:
  coco = coco.get_text()
  percentcoco.append(coco)

stripped_cocoapercent = [values.replace('%', '') for values in percentcoco]
strippedfloat_cocoapercent = [float(num) for num in stripped_cocoapercent]

chocbars_df['CocoaPercentage'] = strippedfloat_cocoapercent

#print(chocbars_df)

plt.scatter(chocbars_df.CocoaPercentage, chocbars_df.Ratings)
plt.clf()


z = np.polyfit(chocbars_df.CocoaPercentage, chocbars_df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(chocbars_df.CocoaPercentage, line_function(chocbars_df.CocoaPercentage), "r--")


plt.show()
