# Project3
# Netflix Series and Films Analysis Project

#Project Overview

This project aims to analyse the most viewed television series and films on Netflix, one of the world's leading streaming platforms with billions of daily viewers. We sought to investigate the top-charting films and television series, examining factors such as genre, length, and viewer count for each title. Our goal was to provide insights and inspiration for viewers looking for their next film or series to watch.

# Key Questions Addressed

1. Type- What is the preferred medium, films or TV shows, and what is the distribution between these two categories?
2. Premiere - Which year had the most releases?
3. Genre - What is the most popular genre?
4. Top TV Show - Which TV show achieved the highest viewership?
5. Top Film - Which film had the most views?
6. Overall Popularity - What is the most popular film or TV series, and which one ranks the highest overall?


#Data Visualisation

We utilised Matplotlib for data visualisation, enabling us to create clear and informative charts to present our findings. Here's a summary of our visual analyses:

- **Preferred Medium**: We used a pie chart to visualise the preference between films and television series among Netflix users. Our findings indicated a preference for films over television series. This preference may be influenced by the availability and production origins of TV series versus films on Netflix.
  
We analysed the number of releases per year to identify trends. The year 2019 had the highest number of releases (1,712 titles), coinciding with the onset of the COVID-19 pandemic, which likely impacted production and release schedules.

n 2019, "Crash Landing on You" (Series) and "Murder Mystery" (Film) were the most viewed, with a combined viewership of over 120.3 million.

Using Seaborn, we visualised the popularity of different genres. Comedy emerged as the most viewed genre, while News was the least viewed. This insight is crucial for Netflix to tailor content that aligns with viewer preferences and retain its audience.

#Engineering and Visualisation

To cater to both engineering and visualisation aspects of our analysis, we developed an app using the KIVY library. KIVY is a versatile library that allows for the development of apps with Python classes, making it an ideal choice for our project.

#Data Management

We employed MongoDB/NoSQL as our database solution, given the large size and complexity of the dataset. The dataset was transformed and split into two collections based on type (films and TV series), which were then exported in JSON format. This approach facilitated efficient data management and analysis.
