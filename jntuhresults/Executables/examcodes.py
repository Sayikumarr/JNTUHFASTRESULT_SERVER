import requests
from bs4 import BeautifulSoup
urll = "http://results.jntuh.ac.in/jsp/home.jsp"


arr11,arr12,arr21,arr22,arr31,arr32,arr41,arr42=set(),set(),set(),set(),set(),set(),set(),set()
examcodes_dic={"11":{},"12":{},"21":{},"22":{},"31":{},"32":{},"41":{},"42":{}}
def examcodes():
    global examcodes_dic
    global arr11,arr12,arr21,arr22,arr31,arr32,arr41,arr42
    response = requests.request("GET", urll)
    soup = BeautifulSoup(response.content, "html.parser")
    tr= soup.find_all("table")[0].find_all("tr")
    for i in tr:
        td=i.find_all("td")[0]
        year = (i.find_all("td")[1].get_text())[-4:]
        href=td.find_all("a")[0]['href']
        text=td.get_text()
        code=''
        if code in text:
            examCode_Index=href.find("examCode")
            examCode=href[examCode_Index+9:examCode_Index+13]
            if(' I Year I ' in text):
                arr11.add(examCode)
                try:
                    examcodes_dic["11"].get(year).append(examCode)
                except:
                    examcodes_dic["11"][year]=[examCode]
            elif(' I Year II ' in text):
                arr12.add(examCode)
                try:
                    examcodes_dic["12"].get(year).append(examCode)
                except:
                    examcodes_dic["12"][year]=[examCode]
            elif(' II Year I ' in text):
                arr21.add(examCode)
                try:
                    examcodes_dic["21"].get(year).append(examCode)
                except:
                    examcodes_dic["21"][year]=[examCode]
            elif(' II Year II ' in text):
                arr22.add(examCode)
                try:
                    examcodes_dic["22"].get(year).append(examCode)
                except:
                    examcodes_dic["22"][year]=[examCode]
            elif(' III Year I ' in text):
                arr31.add(examCode)
                try:
                    examcodes_dic["31"].get(year).append(examCode)
                except:
                    examcodes_dic["31"][year]=[examCode]
            elif(' III Year II ' in text):
                arr32.add(examCode)
                try:
                    examcodes_dic["32"].get(year).append(examCode)
                except:
                    examcodes_dic["32"][year]=[examCode]
            elif(' IV Year I ' in text):
                arr41.add(examCode)
                try:
                    examcodes_dic["41"].get(year).append(examCode)
                except:
                    examcodes_dic["41"][year]=[examCode]
            elif(' IV Year II ' in text):
                arr42.add(examCode)
                try:
                    examcodes_dic["42"].get(year).append(examCode)
                except:
                    examcodes_dic["42"][year]=[examCode]
            
    arr11=sorted(arr11)
    arr12=sorted(arr12)
    arr21=sorted(arr21)
    arr22=sorted(arr22)
    arr31=sorted(arr31)
    arr32=sorted(arr32)
    arr41=sorted(arr41)
    arr42=sorted(arr42)


