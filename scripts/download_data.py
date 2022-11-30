from bs4 import BeautifulSoup
import requests
import re

# SEMARNAT GACETA
def download_semarnat_pdfs():
    #   access website
    web = requests.get("http://sinat.semarnat.gob.mx/Gaceta/aniosgaceta").text
    soup = BeautifulSoup(web,"html.parser")

    # find list elements (years)
    years = soup.find_all('li')
    #   loop through years
    for year in years:

        #get year - link
        ylink = year.a['href']
        yyear = year.a.text
        print(f'''
            year: {yyear}
            link: {ylink}
        ''')

        #acces year information
        yweb = BeautifulSoup(requests.get(ylink).text,"html.parser")
        #find table row elements
        pdfs = yweb.find_all('tr')
        #   eliminate headers
        pdfs = pdfs[1:]

        #   loop through pdfs
        for pdf in pdfs:
            pdf_info = pdf.find_all('td')
            pdf_link = pdf_info[0].a['href']
            pdf_name = pdf_info[1].text
            pdf_published = pdf_info[2].text

            print(f'''
                PDF link : {pdf_link}
                PDF name: {pdf_name}
                PDF publish date: {pdf_published}
            ''')

            #save pdf
            saving_route = './raw_data/PDF/'
            with open(saving_route+pdf_name+'.pdf','wb') as f:
                pdf_download = requests.get(pdf_link)
                f.write(pdf_download.content)
                f.close()