# Twitter-Streaming-Data-Analysis

As more data is generated, it’s becoming increasingly important to be able to work with real-time data. Real-time, or streaming, data is generated continuously, and in the case of the stock market, there can be millions of rows generated every hour. Being able to work with streaming data is a critical skill for any aspiring data scientist. In this thesis, I’ll use Twitter data as an example and work with Hadoop in virtual machine and pandas data frame in Python.

## Introduction
For this project, I applied API key from Twitter Developer Account. I picked Skin Care and Trade War as my two topics. Then I started to collect data for two topics according to different key words. The key words I used for Skin Care are skin care, anti-aging and skincare routine. Since my key words are very specific, it took me 39 hours to collect a meaningful dataset. The final file size is 74.3 MB and number of tweets is 14044. 

For the Trade War topic, I used China trade, China trump and Trade war as my key words. And especially in Dec.2, the US and China agreed to a temporary truce to deescalate trade tensions. Therefore, it’s a great time to collect tweets to gather everybody’s opinion. It took me around 30 hours and the number of tweets is 35758. 

After geeting all the data I need, I started my analysis in Hadoop and Python regarding to topics like top hastags, top authoritatice users, top significant words and etc.
