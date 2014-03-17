from eztv_api import EztvAPI

test_api = EztvAPI().tv_show('Game Of Thrones')

#get all the seasons from Game Of Thrones
seasons = test_api.seasons()
for season in seasons:
    for episode in seasons[season]:
        # will print the magnet link of all episodes, in all seasons
        print seasons[season][episode]

# specific season
episodes = test_api.season(3)
for episode in episodes:
    # will print the magnet link for all episodes
    print episodes[episode]

#specific episode
print test_api.episode(3, 10)

# get upcoming shows of given day
print test_api.get_upcoming_tvshows_on_given_day('SUNDAY')
