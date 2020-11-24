from bs4 import BeautifulSoup
import requests
import time
import csv


def get_youtube_trending():
    html = requests.get('https://www.youtube.com/feed/trending').text
    soup = BeautifulSoup(html, 'lxml')

    container = soup.body.find('div', class_="feed-item-container browse-list-item-container yt-section-hover-container compact-shelf shelf-item branded-page-box vve-check clearfix")
    container = BeautifulSoup(str(container).replace(str(', '), ' '), 'lxml')
    all_videos = container.find_all('div', class_='yt-lockup-content')

    now = str(time.strftime("%c"))
    now = now.replace(':', '.')
    csv_file = open(now + '.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Tytuł', 'Autor', 'Czas_trwania', 'Wyswietlenia', 'Link'])

    for video in all_videos:
        vid_title = video.find('h3', class_='yt-lockup-title').a.text
        vid_time = video.find('h3', class_='yt-lockup-title').span.text
        vid_time_final = str(vid_time.split(':')[1] + ':' + vid_time.split(':')[2])
        vid_time_final = vid_time_final.replace('.', '')
        vid_time_final = vid_time_final.replace(' ', '')
        vid_author = video.find('div', class_='yt-lockup-byline').a.text
        vid_views = video.find('div', class_='yt-lockup-meta').ul.find_all('li')[1].text
        vid_views_final = vid_views.split(' ')
        vid_views_final = vid_views_final[0].replace('\\xao', '')
        vid_link = video.find('a', class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link')['href']
        vid_link_final = f'https://youtube.com{vid_link}'

        vid_link_final = vid_link_final.replace(',', ' ')
        vid_views_final = vid_views_final.replace(',', ' ')
        vid_time_final = vid_time_final.replace(',', ' ')
        vid_title = vid_title.replace(',', ' ')
        vid_author = vid_author.replace(',', ' ')

        # job_print = 'Tytuł: ' + vid_title + '\nAutor: ' + vid_author + '\nCzas trwania: ' + vid_time_final + '\nWyświetlenia: ' + vid_views_final + '\nLink: ' + vid_link_final + '\n\n'
        # print(job_print)
        csv_writer.writerow([vid_title, vid_author, vid_time_final, vid_views_final, vid_link_final])
    csv_file.close()


get_youtube_trending()
