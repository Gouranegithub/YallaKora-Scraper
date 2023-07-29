
import requests
from bs4 import BeautifulSoup
import csv



date= input("please enter a date in the following format MM/DD/YYYY:  ")
page= requests.get(f'https://www.yallakora.com/match-center?date={date}' )  

def main(page):
    src=page.content
    soup = BeautifulSoup(src, 'lxml')
    championship = soup.find_all("div",{'class':'matchCard'})
    match_details=[]
    
    def get_match_info(championship):
        championship_name= championship.contents[1].find('h2').text.strip()
        
        all_matches= championship.contents[3].find_all("li",{'class':'item future'})
       
    

        for match in all_matches:           
            match_info= match.find('a').find('div').find('div',{'class':'teamCntnr'}).find('div',{'class':'teamsData'})
            match_result=match_info.find('div',{'class':'MResult'})
            
            match_scor = match_result.find_all('span',{'class':'score'})
            score= f'{match_scor[0].text.strip()} - {match_scor[1].text.strip()}'
            
            match_time = match_result.find('span',{'class':'time'}).text.strip()
            
            
            
            match_teams= match_info.find_all('div', {'class':'teams'})
            teamA= match_teams[0].find('p').text.strip()
            teamB= match_teams[1].find('p').text.strip()
            
            match_details.append({'نوع البطولة': championship_name,'الفريق الاول':teamA,'الفريق الثاني':teamB,'الميعاد':match_time,'النتيجة': score})
            
    for champ in championship:
        get_match_info(champ)
    
    keys =  match_details[0].keys()   #['نوع البطولة', 'الفريق الاول','الفريق الثاني','الميعاد','النتيجة' ]
   
    with open('C:\\Users\\ABDELLAH\\Desktop\\selenium\\matches.csv','w', encoding='utf-8-sig', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, delimiter=',' )
        dict_writer.writeheader()
        for mat in match_details:
            dict_writer.writerow(mat)
        print('file_created')
    
main(page)



#exemple of input: 7/30/2023




