"# Digital-Humanities" 

Digital Humanaties - Feamale leading characters in animation movies over the years

Our research question:
We chose to investigate weather there is an increase in female leading characters in animation movies over the yeras.
In order to find some answers we chose to use IMDB as our source of information since IMDB has descriptions of over 6.5 million movies.

Data sources:
1. Basic database provided by IMDB containing for each title - which genres it is categorized as - DB link: https://datasets.imdbws.com/ (title.basics.tsv.gz)
2. IMDB api - the api provided an access to the plot of each animation movie
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
- Using OpenRefine we editted the information collected for the following results
- According to the information collected in the previous levels we created maps that show the distribution of the countries in which the movies were created
- In addition we formed a graph that shows a growth in the number of movies with female leading characters over the years
- A study case - the USA - a comparison between the total number of animation movies created in the US and the number of animation movies withe female leading characters
- Present the findings and the research process in a website

Summary of the process and our main challenges- 
- We went from having 6.5 million movies - to 7154 animation movies - to 1121 animation movies with female leading characters
- The data started as plots of movies, with no specific clasification weather the leading character is a female or male. 
furteremore, unlike regular movies (not animation) where the gender of the actors can imply on the gender of the leading character in the movie, in animation movies this is not always the case, so our only source of information was the plots of the movies and the words that are used there to describe the main characters - this was our main challenge in the process - deciding on a way to determine what is the gender of the leading characters from texts that do not directly imply on this kind of imformation.
- The formation of the data was very helpful for our research - the api of IMDB provided an efficient way to read the information and use our algorithms on it and made it possible to make most of the process automated and not manual.
- Reguarding the gender setermination challenge - The results we got contains movies that "passed" our filters although they are not female leading character's movies, meaning some of the results are "false positive". this is due to the algorithm we used, in further research these movies could be filtered either manualy or using pairs of words instead of singe words. either way - we prefered not missing potential movies and the results fitted our assamptions.

Results:
- The results show an increase in the number of animation movies with female leading characters over the years
- The study case we chose - mainly because the US is a very big manufacturer of animation movies - shows that even though there is an increase - the relative amounts of animation movies with female leading characters has decreased comparing to the increasing number of total animation movies created in the US.
- The first conclusion was not surprising to us given the "female status" in the world, more and more movies are written around strong independent woman figures (animation and regular movies)
- The secound result was very surprising - as we described on our site - it shows that there is still work to be done, and that the gap is still there in a country that has a very big animation movies industry.

In conclision - 
We took a subject that is not in the center of the attention regarding the status of women, since it is related with kids, were the comparison between the genders is not done as often as in grownups, therefore we didn't have the answers to our research question "clear" and "obvious"
Using different algorithms and manualy processing we were able to collect the results from the basic data base we had and present them in an imformative way to the wide audience.

Our project website:
https://mayaox.wixsite.com/wonderwomenanimation

Course website:
https://www.cs.bgu.ac.il/~dhcs202/Main


