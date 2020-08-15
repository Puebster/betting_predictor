from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import json
import time


def get_table_per_gameday():
    # "https://www.kicker.de/1-bundesliga/spieltag/2012-13/"
    df_spieltage = {}
    for spieltag_num in range(1, 14):
        print(spieltag_num)
        try:
            link = 'https://www.kicker.de/1-bundesliga/spieltag/2019-20/'
            resp = requests.get(link + str(spieltag_num))
            soup = BeautifulSoup(resp.content.decode(), 'html.parser')
            all_table = soup.find_all('table')

            trs = all_table[0].find_all('tr')
            first = True
            table = []
            for tr in trs:
                if first:
                    first = False
                    continue
                tds = tr.find_all('td')
                values = [tds[3].find('a').find('span').text,
                          tds[4].text.replace('\n', '').replace(' ', ''),
                          tds[5].text.replace('\n', '').replace(' ', ''),
                          tds[6].text.replace('\n', '').replace(' ', '')]
                table.append(values)
            df_spieltage[spieltag_num] = table
        except Exception as e:
            print(e)

    json.dump(df_spieltage, open('C:/Users/Frido/Desktop/1920.json', 'w'))
    return df_spieltage


def get_elo_names_clubelo():
    resp = requests.get("http://clubelo.com/Ranking")
    soup = BeautifulSoup(resp.content.decode(), 'html.parser')
    name_d = {'England': [],
              'Germany': [],
              'Spain': [],
              'Italy': [],
              'France': []}
    all_td = soup.find_all('td')
    possible_nations = {'GER': 'Germany',
                        'FRA': 'France',
                        'ESP': 'Spain',
                        'ITA': 'Italy',
                        'ENG': 'England'}
    for i, td in enumerate(all_td):
        try:
            img = td.find('img')
            if img is not None:
                nation = img['alt']
                if 'l' in td['class'] and nation in possible_nations:
                    name = td.find('a').text
                    print(str(round(i/len(all_td)*100, 2)) + '%', name)
                    if str(name).replace(' ', '') not in name_d:
                        name_d[possible_nations[nation]].append(name)
        except Exception as e:
            print(e)
    json.dump(name_d, open('C:/Users/Frido/Desktop/elo_names.json', 'w'))
    return name_d

def get_elo_ratings_fussballelo():
    resp = requests.get("http://fussballelo.de/")
    soup = BeautifulSoup(resp.content.decode(), 'html.parser')
    names = []
    dates = []
    ratings = []
    all_sublinks = soup.find_all('a')
    for i, link in enumerate(all_sublinks):
        try:
            if 'report.php?team=' in link['href']:
                s_link = link['href']
                resp = requests.get("http://fussballelo.de/" + s_link)
                soup = BeautifulSoup(resp.content.decode(), 'html.parser')
                name = soup.find('title').text
                name = name.replace('Elo Report ', '')
                print(str(round(i/len(all_sublinks)*100, 2)) + '%', name)
                for row in soup.find_all('tbody',
                                         {'class': 'ratingTableBody'}):
                    for row2 in row.find_all('tr'):
                        short = row2.find_all('td')
                        names.append(name)
                        dates.append(short[0].text)
                        ratings.append(short[3].text)
        except Exception as e:
            print(e)

    end_data = pd.DataFrame({
        'name': names,
        'date': dates,
        'rating': ratings
        })

    end_data.to_csv('ratings.csv', encoding='utf-8')


def get_elo_files(name_d):
    total_num = 0
    i = 0
    for c in name_d:
        total_num += len(name_d[c])
    for country in name_d:
        folder_path = '../ratingFiles/' + country + '/'
        directory = os.path.dirname(folder_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        for team in name_d[country]:
            i+=1
            if not os.path.exists(folder_path + team):
                print(str(round(i/total_num*100, 2)) + '% - ',
                      team + ' - ' + country)
                url = 'http://api.clubelo.com/' + team
                r = requests.get(url)
                with open(folder_path + team, 'wb') as f:
                    f.write(r.content)
                time.sleep(8.7)

    print('finished')

def find_all_urls(url):

    getpage = requests.get(url)
    getpage_soup = BeautifulSoup(getpage.text, 'html.parser')

    all_links = getpage_soup.findAll('a')

    for link in all_links:
        print(link)


def main():

    return

if __name__ == '__main__':
    test = get_table_per_gameday()