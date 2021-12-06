# YouTube Trending Data Analysis Machine Learning Project
This project was created in order try various Machine Learning models on Youtube's Trending video statistics obtained from Kaggle for educational purposes. The main dataset used in this project is the one from the United States last updated on December 5th 2021.
Datasets from various countries can be downloaded and retrieved from: [YouTube Trending Video Dataset (updated daily)](https://www.kaggle.com/rsrishav/youtube-trending-video-dataset)

![Youtube Trending Statistics](https://www.galaxymarketing.global/wp-content/uploads/2020/01/Youtube-Statistics-1536x753.png)
Image retrieved from: [Galaxy Marketing YouTube Stats](https://www.galaxymarketing.global/youtube/youtube-statistics-that-you-need-to-know-in-2020/)

# Table of contents
1. [Introduction](#Introduction)
    1. [Installation](#Installation)
    2. [Test with Colab Notebook](#ColabNotebook)
<!--
see how to make table of contents in markdown: https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents

2. [Some paragraph](#paragraph1)
    1. [Sub paragraph](#subparagraph1)
3. [Another paragraph](#paragraph2)
-->

## Introduction <a name="introduction"></a>

In this repository, I will be Experimenting with Google Research Football Environment.
Football has been a passion of mine since I can remember, it is fantastic that I can use a passion of mine to continue learning about my field of study.

Having had the chance to actually play the sport at a semi-professional level maybe I can provide some unprecedented insight and help train the models.

Created a function that takes screenshots from that used pyautogui's _.screenshot_
Full Doc at Link: [pyautogui-screenshot function](https://pyautogui.readthedocs.io/en/latest/screenshot.html)

Published paper linked here: [Google Research Football: A Novel Reinforcement Learning Environment](https://arxiv.org/pdf/1907.11180.pdf).


### Installation <a name="Installation"></a>
After struggling with the different installation instructions. The docker image with gpu support and tensorflow base was by far the best and that actually rendered the game.


**Instructions on how to install with docker linked here:** [Google Research Football Docker Image](https://github.com/google-research/football/blob/master/gfootball/doc/docker.md).


[My Own Installations hyperlinked here](./Installation.md)

### Test with Colab Notebook<a name="ColabNotebook"></a>

Using the following link: [Tutorial Colab Notebook!](https://colab.research.google.com/github/google-research/football/blob/master/gfootball/colabs/gfootball_example_from_prebuild.ipynb) 
Honnestly does not teach much. Not sure it was inteded to teach anything or simply as a quickstart. Created a directory titled "ColabTutorial" where I will be running the above notebook as .py files. Please refer to the readme file titled "Colab_summary.md" hyperlinked: [Colab_summary](https://github.com/GateraGael/Google-Research-Football-Environment-Experiment/blob/main/ColabTutorial/colab_summary.md) in which I basically logged all my trials.

<!--
## Some paragraph <a name="paragraph1"></a>
The first paragraph text

### Sub paragraph <a name="subparagraph1"></a>
This is a sub paragraph, formatted in heading 3 style

## Another paragraph <a name="paragraph2"></a>
The second paragraph text

-->


# December 24th 2020
On Decmber 23rd, I ran different trials with the given started tutorial notebook to get a reward, some of them had a reward, while some other did not.
Therefore wanted to get a more thorough understanding of what was going on in the background.

Please see folder [Colab_summary](https://github.com/GateraGael/Google-Research-Football-Environment-Experiment/blob/main/ColabTutorial/colab_summary.md) file for an overview of my trials.

Also have been refering to the the actual paper in order to get better insight into the environments, variables and actions the agents take.

Page 4 of the resarch paper explains that the football engine rewards the team or agent when a goal is scored (+1) and rewards a (-1) when a goal is scored against. Therefore only my Trial #2 successfully scored a goal while all the other attemps had the ball taken away.
At Trial #10 I was able to make our agent Alan Turing dribble directly into the goal.
Unfortunately no A.I. yet, simply needed to do this to get an understanding of the football engine.

![](ColabTutorial/trial10_logs/screenshots/00m40s.png)




