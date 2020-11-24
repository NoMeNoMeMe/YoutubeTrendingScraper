import csv

csv_file = open('Trending.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Id', 'Tytuł', 'Autor', 'Czas_trwania', 'Wyswietlenia', 'Link', 'Data', 'Godzina'])
