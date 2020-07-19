import csv
from imdb import IMDb
import collections

# opening the 'title.basics.tsv.gz' data base
tsv_file = open('data.tsv', encoding='utf-8')
read_tsv = csv.reader(tsv_file, delimiter='\t')

# array to collect animation movies
animation_movies = []

# create a text file containing all animation movies plots
plot_file = open('plot_file.txt', 'w+', encoding='utf-8')

# the following loop is to collect only animation movies from the DB
i = 0
first_line = True
for line in read_tsv:
    # if i==500000:
    #     break
    if first_line:
        first_line = False
        continue
    title_type = line[1]
    if title_type == 'movie':
        genres = line[len(line)-1]
        genres = genres.split(',')
        for genre in genres:
            if genre == 'Animation':
                animation_movies.append(line[0][2:])
    print(i)
    i = i+1

# connect to IMDB
ia = IMDb()

# the following loop is responsible for writing the animation movie plots in to 'plot_file.txt'
j=0
for movie_id in animation_movies:
    movie = ia.get_movie(movie_id)
    plot = movie.get('plot')
    if plot != None:
        plot_file.write(plot[0]+'\n')
    print(j)
    j=j+1
plot_file.close()