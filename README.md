# Analysing-Mental-Health-during-COVID

# Introduction
Nowadays Social Media is a place where millions of peoples share their lives every day, creating a platform of self-expression and interesting information. Studies have reported that individuals living with a range of mental disorders, including depression, psychotic disorders, or other severe mental illnesses, use social media platforms at comparable rates as the general population, with use ranging from about 70% among middle-age and older individuals to upwards of 97% among younger individuals.

# Statement of the Problem:
According to the World Health Organization (WHO), mental health is “a state of well-being in which the individual realizes his or her own abilities, can cope with the normal stresses of life, can work productively and fruitfully, and is able to make a contribution to his or her community”. According to an estimate by the WHO, mental illness makes about 15% of the total disease conditions around the world.

The COVID-19 pandemic is a major health crisis affecting several nations.By now 38,364,519 people have been affected worldwide.Such widespread outbreaks are associated with adverse mental health consequences. Keeping this in mind we thought of analysing the effect of COVID-19 on people's mental heath.

# The Project
In this project, we have focussed of collecting tweets for preparing the dataset. The tweets were collected by using keywords related to mental health and COVID.
There are two Datasets: 
  1. PreCovid: This is collection of tweets prior to the pandemic. It has about 400 tweets which are labelled as 0 (normal tweets) and 1 (negative/depressive tweets).
  2. PostCovid:  This is collection of tweets during the pandemic. It also has about 400 tweets which are labelled as 0 (normal tweets) and 1 (negative/depressive tweets).
 
Both the datasets were preprocessed and cleaned, then Count Vectorizer and Multinomial NB were used to perform the classification. 
After this, using Frequency Distribution, 50 most frequently occuring words were extracted and were used to prepare a worldcloud.
The worldcloud of the PreCovid dataset showed some relevant words like 'depress, anxiety, jope, life, time, people'. This suggests that mental health issues were prevalent before the outbreak of COVID-19. However, the worldcloud of the PostCovid Dataset contained some new words like 'lockdown, quarantine, stay home, unemployed, job, corona, ill' which clearly justifies that this outbreak has indeed affected and contributed towards increase in cases of mental illness.
From futher reasearch using news articles, we found more statiscal reports and research papers justifying the same.

# Team
The projected is contributed by:
  1. Smriti Nayak
  2. Shivani Gurbani
  3. Shruti Kumnhare
  4. Arnatri Bandopadhyay
