import schedule


from TrendingScraper import get_youtube_trending

schedule.every(1).minutes.do(get_youtube_trending, print)

