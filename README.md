"# Digital-Humanities" 

Digital Humanaties - Feamale leading characters in animation movies over the years

Our research question:
We chose to investigate weather there is an increase in female leading characters in animation movies over the yeras.
In order to find some answers we chose to use IMDB as our source of information since IMDB has descriptions of over 6.5 million movies.

Data sources:
1. Basic database provided by IMDB containing for each title - which genres it is categorized as
2. IMDB api - the api frovided an access to the plot of each animation movie
3. List of words and number of occurences of each word - built by us
3. Our last DB - animation movies with female leading characters - built by us.

The research process:
Level 1:
- Using a Python program written by us - we collected all the animation movies.
- Collecting the plots of all animation movies to one test file, in order to go over and count the common words
- Run common words algorithm on the file we created in order to create a corpus of words that are related with female leading characters
once we finished this step we were able to categorize the animation movies we collected according to two cetegories - Female leading characters (Our main focus) and None female leading characters.

Level 2:
- According to the corpus of words we built that contains the words related to female leading characters we built a Python program that determains if an animation movie has a female leading character or not
- The movies that "passed" the algorithm (meaning - their plots contain at least one of the words in our corpus) were written to our main data base.

Level 3:
- According to the information collected in the previous levels we created maps that show the distribution of the countries in which the movies were created
- In addition we formed a graph that shows a growth in the number of movies with female leading characters over the years
- A study case - the USA - a comparison between the total number of animation movies created in the US and the number of animation movies withe female leading characters
