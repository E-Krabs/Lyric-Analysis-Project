from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import json

print('Enter Year:')
year = input()

url = 'https://www.billboard.com/charts/year-end/{}/'.format(year)
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers = hdr)
read_content = urlopen(req)

soup = BeautifulSoup(read_content, 'html.parser')

containers = soup.select('article[class*=chart]')

chart_song = []
chart_artist = []

for container in containers:

	song_container = container.find('div', {'class': 'ye-chart-item__title'})
	song = song_container.text.replace('\n', '')

	artist_container = container.find('div', {'class': 'ye-chart-item__artist'})
	artist = artist_container.text.replace('\n', '')

	rank = container.find('div', {'class': 'ye-chart-item__rank'})

	chart_song.append(song)
	chart_artist.append(artist)

	#titles.write(song + ' ' + artist + '\n')

lyric_url = []
chart = 0

for i in range(100):
	lyric_spotify = False
	song = chart_song[chart]
	artist = chart_artist[chart]
	song_uni = urllib.parse.quote(song)
	artist_uni = urllib.parse.quote(artist)

	#print(song_uni + artist_uni)

	token = ''
	api_url = 'https://api.genius.com/search?q={0}&access_token={1}&per_page=1'.format(artist_uni + '%20' + song_uni, token)
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = Request(api_url, headers = hdr)
	read_content = urlopen(req)
	data = json.load(read_content)
	
	for hit in data['response']['hits']:
		print(hit['result']['url'])
		if 'Spotify' in hit['result']['url']:
			lyric_spotify = True
			print('Spotify = True')

		if lyric_spotify == False:
			lyric_url.append(hit['result']['url'])

	chart += 1

lyrics_pool = []
lyrics_pool_str = ''
chart = 0
for url in lyric_url:
	skip = False
	url = lyric_url[chart]
	#print(url)
	hdr = {'User-Agent': 'Mozilla/5.0'}
	try:
		req = Request(url, headers = hdr)
		read_content = urlopen(req)
		soup = BeautifulSoup(read_content, 'html.parser')
	except:
		skip = True
	if skip == False:
		try:
			lyrics = soup.find('div', {'id': 'lyrics-root'}).get_text('\n')
			#print(lyrics)
		except:
			skip = True
		if skip == False:
			lyrics_pool.append(lyrics.split())
			print(lyrics)

			lyrics_pool_str += ('{} ').format(lyrics)

	chart += 1

#lyrics_pool_str = ''
#for i in lyrics_pool:
#	lyrics_pool_str += ('{} ').format(i)

with open('file.txt', 'w', encoding='utf-8') as output:
	output.write(lyrics_pool_str)
