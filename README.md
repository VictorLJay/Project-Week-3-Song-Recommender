<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Song Recommender P-9000
*Víctor López*

*DAFT October 2020, Barcelona & 11/11/2020*

## Content
- [Project Description](#project-description)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)


## Project Description
**Song Recommender P-9000** suggest a song based on the input of the user. There are two scenarios:
- If the hot is trendy (Billboard HOT 100), it will return another song from that list.
- If not, it will search the song features of the input and suggest another, from a Spotify list, that belongs to the same cluster.

The goal of the project is discover new songs that match with your preferences.

## Dataset
The dataset that we used was the original contained on the folder, the **accidents-2017.csv**. From that data, we isolated part of it in different CSV files mentioned above.

## Workflow
  * Web scrapping the **Billboard HOT 100** and creation of a Dataframe with those songs.
  * Obtaining, in this case, 10K Songs from a Spotify playlist using the Spotify API.
  * Create a dataframe of those new songs and cluster it in 7 different groups based on their song features.
  * Project runs. The user inputs a song and the prototype will return another one. If the input is found on the first Dataframe, it will return another song from that one. If not, the prototype will detect the song features of the input, match their features with the correct cluster and return another song from the cluster it belongs.

For better clarification, see the image below:

![image info](C:/Users/GiantsV3/Documents/Ironhack/Week3/Project-Week-3-Song-Recommender/images/workflow.png)

## Organization

The organization of the folder is the following one:
1. Initial folder where you can find the *README*, *.gitignorefile* and three folders (*data*, *images* and *your-code*). The *data* and *images* folders contain just one file, being one CSV file and the image of the workflow, respectively.
2. On the *your-code* folder, there you can find the final code with all the project and the steps. Also, you can find another folder named *old-files*, where there are other jupyter notebooks used for the creation of that project.

## Links
Include links to your repository, slides and kanban board. Feel free to include any other links associated with your project.

[Repository](https://github.com/VictorLJay/Project-Week-3-Song-Recommender)
