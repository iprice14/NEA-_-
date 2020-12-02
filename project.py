#current_user_top_tracks(limit=50, offset=0, time_range='short_term')
#speechiness
#loudness
#instrumentalness
#id
#energy
#popularity
#danceability
#analysis_url
#track_href	string	A link to the Web API endpoint providing full details of the track.
#type	string	The object type: “audio_features”
#uri	string	The Spotify URI for the track.
# couldn't do the explicit bit
#{
#  "danceability": 0.696,
#  "energy": 0.905,
#        "key": 2,
#        "loudness": -2.743,
#        "mode": 1,
#  "speechiness": 0.103,
#  "acousticness": 0.011,
#        "instrumentalness": 0.000905,
#        "liveness": 0.302,
#  "valence": 0.625, (happiness)
#        "tempo": 114.944,
#        "type": "audio_features",
#        "id": "11dFghVXANMlKmJXsNCbNl",
#        "uri": "spotify:track:11dFghVXANMlKmJXsNCbNl",
#        "track_href": "https://api.spotify.com/v1/tracks/11dFghVXANMlKmJXsNCbNl",
#        "analysis_url": "https://api.spotify.com/v1/audio-analysis/11dFghVXANMlKmJXsNCbNl",
#        "duration_ms": 207960,
#        "time_signature": 4
#}
# spotify pword = AQA4thewin

def newsong(recs):
    for song in recs:
        if (song in current_user_saved_tracks(limit=None, offset=0)) or (song in current_user_recently_played(limit=None, after=2.628e+9, before=None)):
            new = False
        else:
            new = True
        return new

def judgetheirtaste():
    tunez = [current_user_top_tracks(limit=50, offset=0, time_range='short_term')]
    meanda = 0
    meansp = 0
    meanac = 0
    meanv = \
         trhkiy0
    for i in range (0,len(tunez)):
        tune = audio_features(tracks=[tunez[i]])
        danceability = tune["danceability"]
        energy = tune["energy"]
        speechiness = tune["speechiness"]
        acousticness = tune["acousticness"]
        valence = tune["valence"]
        meanda = meanda + danceability
        meansp = meansp + speechiness
        meanac = meanac + acousticness
        meanv = meanv + valence



    exp = explicit()
def authorise():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="c27acaf679dc495fb126aa95eca64afd",
                                                   client_secret="c31f73be54ac47a19d5d211a0bfc0a4c",
                                                   redirect_uri="http://example.com/callback", # have used a random redirect page as this isn't a real website
                                                   scope="user-library-read"))
    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
def wtfispygame():
    pygame.init()
    clock = pygame.time.Clock()
    vec = pygame.math.Vector2
    gamedisplay = pygame.display.set_mode((800, 600))
    done = False
    pygame.display.set_caption('Button')
    gamedisplay.fill((207, 232, 240))
    rect = pygame.draw.rect(gamedisplay, (0, 0, 0), pygame.Rect(280, 220, 230, 130))
    font = pygame.font.SysFont('inkfree', 100)
    text = font.render('Login', True, (200,0,0))
    gamedisplay.blit(text,rect)
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            pygame.display.flip()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (510 > mouse[0] > 280) and (350 > mouse[1] > 220):
            if click[0] == 1:
                authorise()
            rect = pygame.draw.rect(gamedisplay, (0, 0, 0), pygame.Rect(280, 220, 230, 130))
            font = pygame.font.SysFont('inkfree', 100)
            text = font.render('Login', True, (200, 0, 0))
            gamedisplay.blit(text, rect)
        pygame.display.update()
        clock.tick(15)





import pygame
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth # spotipy code

wtfispygame()


