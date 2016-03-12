#!/usr/bin/python3

from time import strftime
import requests
from lxml import html
import datetime


def main():

    timestr = strftime("%Y %m %d")
    yesterday = ((datetime.date.today() - datetime.timedelta(1)).strftime("%m/%d/%Y")).lstrip("0").replace("/0", "/")  # create a date string in format dd/mm/yyyy

    outfile = open(timestr+'.txt', 'a')

    init_r = requests.get('http://www.htzfm.com/broadcasthistory.aspx')  # get connection to a page
    VIEWSTATE = html.fromstring(init_r.content).cssselect('input#__VIEWSTATE')[0].get('value')  # retrieve viewstate var - long random string
    CTL00MAIN = html.fromstring(init_r.content).cssselect('select')[0].get('name')  # retrieve line name from POST

    data = {CTL00MAIN: yesterday, '__VIEWSTATE': VIEWSTATE}  # create POST request line

    r = requests.post('http://www.htzfm.com/broadcasthistory.aspx', data=data)  # send the request
    page = html.fromstring(r.content)
    tracks = [x for x in page.cssselect('.songList tr')]

    print(yesterday)

    for track in tracks:
        time, name, _ = [x for x in track.cssselect('td')]
        print('{} : {}'.format(time.text.strip(), name.text_content().strip()))
        outfile.write('{} : {}'.format(time.text.strip(), name.text_content().strip()))

    outfile.close()

if __name__ == "__main__": main()