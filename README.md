# Sinhala Songs Search Engine

Sinhala Song search engine using Sinhala language. The search engine presents following functions.

* Search by artist – The Search Engine can search songs which are sang by particular artist.
     * Eg:- අමරව ගායනා කල ගීත
* Search by lyricist – The Search Engine can search songs which are written by particular lyricist.
     * Eg:- මදවල එස් රත්නායක ලියපු ගීත
* Search by musician – The Search Engine can search songs which are music directed by particular musician.
     * Eg:- අමරව සංගීත කල ගීත
* Search by lyrics – The Search Engine can search songs by providing lyrics.
     * Eg:- බඹරෙකු ආවයි
* Search by genre – The Search Engine can search songs by the song genre.
     * Eg:- කැලිප්සෝ ගීත
     

## Quickstart:
To start the search engine follow the instructions given below.
* Start an ElasticSearch Instance on the port 9200
* Run createIndex.py file to create index
* Run the python3 server.py` to run the search engine server
* Visit http://localhost:5000 and search by entering relevant queries in Sinhala language

## Data
The dataset contains 500 songs scraped from this [website](http://sinhalasongbook.com/). It contains lyrics and following metadata about the songs.

* Title in English
* Title in Sinhala
* Genre in Sinhala
* Lyricist name in Sinhala
* Artist name in Sinhala
* Musicians name in Sinhala
* Lyricist name in English
* Artist name in English
* Musicians name in English


## Directory Structure

* Sinhala song corpus - Contains the scrapped song data set.
* Templates - Contains the User interface templates.
* createIndex.py - Contains code to create the index.
* search_engine.py - Contains the logic of the search engine.
* server.py - Contains the code to run the search engine server.



