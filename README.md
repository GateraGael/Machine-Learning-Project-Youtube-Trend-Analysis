# YouTube Trending Data Analysis Machine Learning Project
This project was created in order try various Machine Learning models on Youtube's Trending video statistics obtained from Kaggle for educational purposes. The main dataset used in this project is the one from the United States last updated on December 5th 2021.
Datasets from various countries can be downloaded and retrieved from: [YouTube Trending Video Dataset (updated daily)](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset)

![Youtube Trending Statistics](https://www.galaxymarketing.global/wp-content/uploads/2020/01/Youtube-Statistics-1536x753.png)
Image retrieved from: [Galaxy Marketing YouTube Stats](https://www.galaxymarketing.global/youtube/youtube-statistics-that-you-need-to-know-in-2020/)

# Table of contents
1. [Introduction](#Introduction)
    1. [USA Dataset](#USA_dataset)
    2. [Test with Colab Notebook](#ColabNotebook)


## Introduction <a name="Introduction"></a>
This dataset was created using a webscraper that used the [Youtube Data API](https://developers.google.com/youtube/registering_an_application), which is now a part of Google Cloud Platform. The scraper itself can be found at the following link: https://github.com/mitchelljy/Trending-YouTube-Scraper. The dataset that is updated daily is at the following kaggle site [YouTube Trending Video Dataset (updated daily)](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset).

The scrapper can create useable data in the from '.csv' files for different countries. Every single dataset comes with a column called category_id which is different for every region (there are a total of five regions in the dataset) most likely corresponding to:
1. Americas (North and South America)
2. Europe
3. Africa
4. Asia
5. Australia

Each file comes with a 'JSON' file in which users can retrieve the corresponding caterogry id's. An example of a category is music. I'll initially start with creating models with just data from the United States. Then potentially test on data from other countries to see if the models are consitent.

### USA Dataset<a name="USA_dataset"></a>


### Test with Colab Notebook<a name="ColabNotebook"></a>


<!--
see how to make table of contents in markdown: https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents

2. [Some paragraph](#paragraph1)
    1. [Sub paragraph](#subparagraph1)
3. [Another paragraph](#paragraph2)
-->

<!--
## Some paragraph <a name="paragraph1"></a>
The first paragraph text

### Sub paragraph <a name="subparagraph1"></a>
This is a sub paragraph, formatted in heading 3 style

## Another paragraph <a name="paragraph2"></a>
The second paragraph text

-->






