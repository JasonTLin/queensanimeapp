from .Pymoe import Kitsu

client_id = "dd031b32d2f56c990b1425efe6c42ad847e7fe3ab46bf1299f05ecd856bdb7dd"
client_secret = "54d7307928f63414defd96399fc31ba847961ceaecef3a5fd93144e960c0e151"

uid = "431596"

instance = Kitsu(client_id, client_secret)
filter = {
    "fields[anime]": "slug,posterImage,canonicalTitle,titles,synopsis,subtype,startDate,status,averageRating,popularityRank,ratingRank,episodeCount",
    "fields[users]": "id",
    "filter[user_id]": "431596",
    "filter[kind]": "anime",
    "include": "anime,user,mediaReaction",
    "sort": "status,-progressed_at"
}


def retrieve():
    animelist = list()

    test = instance.library.get(uid, filter)

    i = 0

    for item in test["included"]:
        animedict = {
            "anime": (test["included"][i + 1]["attributes"]["canonicalTitle"]),
            "synopsis": (test["included"][i + 1]["attributes"]["synopsis"]),
            "images": (test["included"][i + 1]["attributes"]["posterImage"]["small"])
        }
        animelist.append(animedict)
        i += 1
        if i == len(test["included"]) - 1:
            break
    return animelist
