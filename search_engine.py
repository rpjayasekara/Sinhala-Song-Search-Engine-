import nltk
import json
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch(HOST="http://localhost",PORT=9200)


lyricist = ['ගත්කරු','රචකයා','ලියන්නා','ලියන','රචිත','ලියපු','ලියව්‌ව','රචනා','රචක','ලියන්']
artist = ['ගායකයා','ගයනවා','ගායනා','ගායනා','ගැයු','ගයන', 'සින්දු','සිංදු', 'සිංදුව','කිව්ව']
music = ['සංගීත']
genre = ['කැලිප්සෝ','සම්භාව්ය','වත්මන්','චිත්‍රපට','පොප්','දේවානුභාවයෙන්','රන්','පැරණි','රන්වන්','පොප්','කණ්ඩායම්','යුගල','අලුත්','නව','පැරණි','පොප්ස්']

stop_words = ['හොඳම','ජනප්‍රිය','ප්‍රචලිත','ප්‍රසිද්ධ','හොදම','ජනප්‍රියම', 'කල', 'ගීත', 'සිංදු', 'සිංදුව', 'ගත්කරු','රචකයා','ලියන්නා','ලියන','රචිත','ලියපු','ලියව්‌ව','රචනා','රචක','ලියන්', 'ගායකයා','ගයනවා','ගායනා','ගායනා','ගැයු','ගයන', 'සංගීත']


def creat_feature_list_with_boosting(boosting_list):
    lyricist_boosted = "sinhala_lyricst^"+str(boosting_list[0])
    artist_boosted = "sinhala_artist^"+str(boosting_list[1])
    music_boosted = "sinhala_music^" + str(boosting_list[2])
    genre_boosted = "Genre^" + str(boosting_list[3])
    lyrics_boosted = "lyrics^" + str(boosting_list[4])
    title_boosted = "title_sinhala^" + str(boosting_list[5])
    return [lyricist_boosted, artist_boosted, music_boosted, genre_boosted, lyrics_boosted, title_boosted]


def create_query(search_query, fields):

    query = {
            "size": 500,
		    "explain": True,
            "query":{
                "multi_match" : {
                    "query": search_query,
                    "fields": fields,
                    "type": "best_fields",
                    "operator": 'or'
             }
        }
    }

    query = json.dumps(query)
    return query


def _search(search_query):
    wordsList = nltk.word_tokenize(search_query)
    boosted = False
    # Index 0 - lyricist, 1 - artist, 2 - musician, 3 - genre, 4 - lyrics, 5 - title
    boosting_list = [1,1,1,1,1,1]
    for word in wordsList:
        if word in lyricist:
            boosted = True
            boosting_list[0] = 3
            print("boost lyricist")
        elif word in artist:
            boosting_list[1] = 3
            boosted = True
            print("boost artist")
        elif word in music:
            boosting_list[2] = 3
            boosted = True
            print("boost musician")
        if word in genre:
            boosting_list[3] = 3
            boosted = True
            print("boost genre")

    if (boosted):
        wordsList = [w for w in wordsList if not w in stop_words]
    else:
        boosting_list[4] = 3
        boosting_list[5] = 5
        print("Boost lyrics")

    new_query = ""

    for word in wordsList:
        new_query = new_query + word + " "

    fields = creat_feature_list_with_boosting(boosting_list)
    query = create_query(new_query, fields)

    res = es.search(index="songs", body=query)
    hits = res['hits']['hits']

    # print(new_query)
    # print(wordsList)
    #
    # print(hits)
    return hits


# print (creat_feature_list_with_boosting([1,1,1,1,1]))
#
# search("අමරදේව ගායනා කල හොදම ගීත 10")

