# 질병관리청 보도자료 (https://www.cdc.go.kr/board/board.es?mid=a20501000000&bid=0015) 코로나19 크롤러
# 본 크롤러를 이용하여 수집한 데이터의 외부 공개 시 출처(질병관리청) 명시 바람.

from urllib.request import urlopen
from bs4 import BeautifulSoup

f = open('list.txt', 'r')
linkList = f.readlines()
f.close()

ff = open('result.txt', 'w')
result = '' # 전체 데이터를 저장

areaList = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

for i in range(len(linkList)): # list.txt 파일에 있는 각 질병관리청 보도자료 링크에 있는 자료에 대하여

    # repeat until successful
    while True:
        try:
            link = linkList[i].split(' ')[0]
            time = linkList[i].split(' ')[1].split('\n')[0]

            print('')
            print('### LINK: ' + str(link) + ' ###')
            html = urlopen(link)
            bsObject = BeautifulSoup(html, "html.parser")

            allSpan = bsObject.find_all('span')
            valueList = []
            areaExist = []

            assert(len(allSpan) > 0)

            break
        except:
            pass

    daegu = False
    
    for span in allSpan:
        a = span.text.replace(",","")
        if a == '대구': daegu = True
        
        for j in range(17):
            if a == areaList[j]: areaExist.append(a)

        if a[len(a)-2:] == '**': a = a[:len(a)-2]
        elif a[len(a)-3:] == '** ': a = a[:len(a)-3]
            
        try:
            a = int(a)
            valueList.append(a)
        except:
            if a == '-': valueList.append(0)
            elif a == ' ' and daegu: valueList.append(0)
            elif len(a) >= 2:
                if a[len(a)-1] == '*' and int(time) >= 20031200:
                    valueList.append(str(a[:len(a)-1]))

    print('')
    print('# VALUE LIST: LENGTH' + str(len(valueList)) + ' #')
    
    for i in range(int(len(valueList) / 20) + 1):
        print(valueList[i*20:(i+1)*20])
        if i % 5 == 4: print('')

    if int(time) >= 20072000: # 2020.07.20 00시 이후의 data 이면
        if time == '21072300': # 2021.07.23 00시의 data 이면
            val0 = valueList[80] + valueList[109]
            val1 = valueList[144]
            val2 = valueList[145]
            val3 = valueList[147]
        elif time == '21072200': # 2021.07.22 00시의 data 이면
            val0 = valueList[81] + valueList[108]
            val1 = valueList[139]
            val2 = valueList[140]
            val3 = valueList[142]
        elif time == '21072100': # 2021.07.21 00시의 data 이면
            val0 = valueList[231] + valueList[260]
            val1 = valueList[292]
            val2 = valueList[293]
            val3 = valueList[295]
        elif time == '21072000': # 2021.07.20 00시의 data 이면
            val0 = valueList[79] + valueList[108]
            val1 = valueList[142]
            val2 = valueList[143]
            val3 = valueList[145]
        elif time == '21071900': # 2021.07.19 00시의 data 이면
            val0 = valueList[231] + valueList[260]
            val1 = valueList[294]
            val2 = valueList[295]
            val3 = valueList[297]
        elif time == '21071800': # 2021.07.18 00시의 data 이면
            val0 = valueList[79] + valueList[108]
            val1 = valueList[140]
            val2 = valueList[141]
            val3 = valueList[143]
        elif time == '21071700': # 2021.07.17 00시의 data 이면
            val0 = valueList[263] + valueList[292]
            val1 = valueList[326]
            val2 = valueList[327]
            val3 = valueList[329]
        elif time == '21071600': # 2021.07.16 00시의 data 이면
            val0 = valueList[79] + valueList[108]
            val1 = valueList[141]
            val2 = valueList[142]
            val3 = valueList[144]
        elif time == '21071500': # 2021.07.15 00시의 data 이면
            val0 = valueList[77] + valueList[106]
            val1 = valueList[136]
            val2 = valueList[137]
            val3 = valueList[139]
        elif time == '21071400': # 2021.07.14 00시의 data 이면
            val0 = valueList[219] + valueList[248]
            val1 = valueList[281]
            val2 = valueList[282]
            val3 = valueList[284]
        elif time == '21071300': # 2021.07.13 00시의 data 이면
            val0 = valueList[77] + valueList[106]
            val1 = valueList[146]
            val2 = valueList[147]
            val3 = valueList[149]
        elif time == '21071200': # 2021.07.12 00시의 data 이면
            val0 = valueList[218] + valueList[247]
            val1 = valueList[275]
            val2 = valueList[276]
            val3 = valueList[278]
        elif time == '21071100': # 2021.07.11 00시의 data 이면
            val0 = valueList[76] + valueList[105]
            val1 = valueList[132]
            val2 = valueList[133]
            val3 = valueList[135]
        elif time == '21071000': # 2021.07.10 00시의 data 이면
            val0 = valueList[267] + valueList[296]
            val1 = valueList[330]
            val2 = valueList[331]
            val3 = valueList[333]
        elif time == '21070900': # 2021.07.09 00시의 data 이면
            val0 = valueList[76] + valueList[105]
            val1 = valueList[137]
            val2 = valueList[138]
            val3 = valueList[140]
        elif time == '21070800': # 2021.07.08 00시의 data 이면
            val0 = valueList[76] + valueList[105]
            val1 = valueList[136]
            val2 = valueList[137]
            val3 = valueList[139]
        elif time == '21070700': # 2021.07.07 00시의 data 이면
            val0 = valueList[218] + valueList[247]
            val1 = valueList[277]
            val2 = valueList[278]
            val3 = valueList[280]
        elif time == '21070600': # 2021.07.06 00시의 data 이면
            val0 = valueList[75] + valueList[104]
            val1 = valueList[137]
            val2 = valueList[138]
            val3 = valueList[140]
        elif time == '21070500': # 2021.07.05 00시의 data 이면
            val0 = valueList[194] + valueList[223]
            val1 = valueList[254]
            val2 = valueList[255]
            val3 = valueList[257]
        elif time == '21070300': # 2021.07.03 00시의 data 이면
            val0 = valueList[235] + valueList[264]
            val1 = valueList[296]
            val2 = valueList[297]
            val3 = valueList[299]
        elif time == '21070200': # 2021.07.02 00시의 data 이면
            val0 = valueList[74] + valueList[103]
            val1 = valueList[135]
            val2 = valueList[136]
            val3 = valueList[138]
        elif time == '21070100': # 2021.07.01 00시의 data 이면
            val0 = valueList[73] + valueList[102]
            val1 = valueList[129]
            val2 = valueList[130]
            val3 = valueList[132]
        elif time == '21062800': # 2021.06.28 00시의 data 이면
            val0 = valueList[196] + valueList[225]
            val1 = valueList[250]
            val2 = valueList[251]
            val3 = valueList[253]
        elif time == '21062700': # 2021.06.27 00시의 data 이면
            val0 = valueList[73] + valueList[102]
            val1 = valueList[128]
            val2 = valueList[129]
            val3 = valueList[131]
        elif time == '21062600': # 2021.06.26 00시의 data 이면
            val0 = valueList[236] + valueList[265]
            val1 = valueList[291]
            val2 = valueList[292]
            val3 = valueList[294]
        elif time == '21062500': # 2021.06.25 00시의 data 이면
            val0 = valueList[73] + valueList[102]
            val1 = valueList[132]
            val2 = valueList[133]
            val3 = valueList[135]
        elif time == '21062400' or time == '21062900' or time == '21070400':
            val0 = valueList[73] + valueList[102]
            val1 = valueList[127]
            val2 = valueList[128]
            val3 = valueList[130]
        elif time == '21062300' or time == '21063000':
            val0 = valueList[196] + valueList[225]
            val1 = valueList[256]
            val2 = valueList[257]
            val3 = valueList[259]
        elif time == '21062200': # 2021.06.22 00시의 data 이면
            val0 = valueList[73] + valueList[102]
            val1 = valueList[134]
            val2 = valueList[135]
            val3 = valueList[137]
        elif time == '21062100': # 2021.06.21 00시의 data 이면
            val0 = valueList[169] + valueList[198]
            val1 = valueList[229]
            val2 = valueList[230]
            val3 = valueList[232]
        elif time == '21062000': # 2021.06.20 00시의 data 이면
            val0 = valueList[72] + valueList[101]
            val1 = valueList[135]
            val2 = valueList[136]
            val3 = valueList[138]
        elif time == '21061900': # 2021.06.19 00시의 data 이면
            val0 = valueList[201] + valueList[230]
            val1 = valueList[257]
            val2 = valueList[258]
            val3 = valueList[260]
        elif time == '21061800': # 2021.06.18 00시의 data 이면
            val0 = valueList[69] + valueList[98]
            val1 = valueList[123]
            val2 = valueList[124]
            val3 = valueList[126]
        elif time == '21061700': # 2021.06.17 00시의 data 이면
            val0 = valueList[69] + valueList[98]
            val1 = valueList[121]
            val2 = valueList[122]
            val3 = valueList[124]
        elif time == '21061600': # 2021.06.16 00시의 data 이면
            val0 = valueList[168] + valueList[198]
            val1 = valueList[224]
            val2 = valueList[225]
            val3 = valueList[227]
        elif time == '21061500': # 2021.06.15 00시의 data 이면
            val0 = valueList[69] + valueList[98]
            val1 = valueList[126]
            val2 = valueList[127]
            val3 = valueList[129]
        elif time == '21061400': # 2021.06.14 00시의 data 이면
            val0 = valueList[169] + valueList[198]
            val1 = valueList[227]
            val2 = valueList[228]
            val3 = valueList[230]
        elif time == '21061300': # 2021.06.13 00시의 data 이면
            val0 = valueList[69] + valueList[98]
            val1 = valueList[130]
            val2 = valueList[131]
            val3 = valueList[133]
        elif time == '21061200': # 2021.06.12 00시의 data 이면
            val0 = valueList[201] + valueList[230]
            val1 = valueList[259]
            val2 = valueList[260]
            val3 = valueList[262]
        elif time == '21061100': # 2021.06.11 00시의 data 이면
            val0 = valueList[69] + valueList[98]
            val1 = valueList[124]
            val2 = valueList[125]
            val3 = valueList[127]
        elif time == '21060900': # 2021.06.09 00시의 data 이면
            val0 = valueList[143] + valueList[172]
            val1 = valueList[198]
            val2 = valueList[199]
            val3 = valueList[201]
        elif time == '21060800': # 2021.06.08 00시의 data 이면
            val0 = valueList[75] + valueList[105]
            val1 = valueList[128]
            val2 = valueList[129]
            val3 = valueList[131]
        elif time == '21060700': # 2021.06.07 00시의 data 이면
            val0 = valueList[143] + valueList[172]
            val1 = valueList[209]
            val2 = valueList[210]
            val3 = valueList[212]
        elif time == '21060600': # 2021.06.06 00시의 data 이면
            val0 = valueList[66] + valueList[95]
            val1 = valueList[121]
            val2 = valueList[122]
            val3 = valueList[124]
        elif time == '21060500': # 2021.06.05 00시의 data 이면
            val0 = valueList[167] + valueList[196]
            val1 = valueList[220]
            val2 = valueList[221]
            val3 = valueList[223]
        elif time == '21060400': # 2021.06.04 00시의 data 이면
            val0 = valueList[87] + valueList[116]
            val1 = valueList[144]
            val2 = valueList[145]
            val3 = valueList[147]
        elif time == '21060300': # 2021.06.03 00시의 data 이면
            val0 = valueList[66] + valueList[95]
            val1 = valueList[113]
            val2 = valueList[114]
            val3 = valueList[116]
        elif time == '21060200': # 2021.06.02 00시의 data 이면
            val0 = valueList[143] + valueList[172]
            val1 = valueList[199]
            val2 = valueList[200]
            val3 = valueList[202]
        elif time == '21060100': # 2021.06.01 00시의 data 이면
            val0 = valueList[66] + valueList[95]
            val1 = valueList[115]
            val2 = valueList[116]
            val3 = valueList[118]
        elif time == '21053100': # 2021.05.31 00시의 data 이면
            val0 = valueList[142] + valueList[171]
            val1 = valueList[196]
            val2 = valueList[197]
            val3 = valueList[199]
        elif time == '21053000': # 2021.05.30 00시의 data 이면
            val0 = valueList[74] + valueList[103]
            val1 = valueList[130]
            val2 = valueList[131]
            val3 = valueList[133]
        elif time == '21052900': # 2021.05.29 00시의 data 이면
            val0 = valueList[175] + valueList[204]
            val1 = valueList[233]
            val2 = valueList[234]
            val3 = valueList[236]
        elif time == '21052800' or time == '21052700' or time == '21061000':
            val0 = valueList[66] + valueList[95]
            val1 = valueList[118]
            val2 = valueList[119]
            val3 = valueList[121]
        elif time == '21052600': # 2021.05.26 00시의 data 이면
            val0 = valueList[138] + valueList[167]
            val1 = valueList[194]
            val2 = valueList[195]
            val3 = valueList[197]
        elif time == '21052500': # 2021.05.25 00시의 data 이면
            val0 = valueList[61] + valueList[90]
            val1 = valueList[118]
            val2 = valueList[119]
            val3 = valueList[121]
        elif time == '21052400': # 2021.05.24 00시의 data 이면
            val0 = valueList[138] + valueList[167]
            val1 = valueList[194]
            val2 = valueList[195]
            val3 = valueList[197]
        elif time == '21052200': # 2021.05.22 00시의 data 이면
            val0 = valueList[159] + valueList[188]
            val1 = valueList[217]
            val2 = valueList[218]
            val3 = valueList[220]
        elif time == '21052100' or time == '21052300': 
            val0 = valueList[64] + valueList[93]
            val1 = valueList[119]
            val2 = valueList[120]
            val3 = valueList[122]
        elif time == '21052000': # 2021.05.20 00시의 data 이면
            val0 = valueList[64] + valueList[93]
            val1 = valueList[120]
            val2 = valueList[121]
            val3 = valueList[123]
        elif time == '21051900': # 2021.05.19 00시의 data 이면
            val0 = valueList[135] + valueList[164]
            val1 = valueList[193]
            val2 = valueList[194]
            val3 = valueList[196]
        elif time == '21051700': # 2021.05.17 00시의 data 이면
            val0 = valueList[105] + valueList[134]
            val1 = 122163
            val2 = 8224
            val3 = 1903
        elif time == '21051600' or time == '21051800':
            val0 = valueList[64] + valueList[93]
            val1 = valueList[121]
            val2 = valueList[122]
            val3 = valueList[124]
        elif time == '21051500': # 2021.05.15 00시의 data 이면
            val0 = valueList[113] + valueList[142]
            val1 = valueList[168]
            val2 = valueList[169]
            val3 = valueList[171]
        elif time == '21051400': # 2021.05.14 00시의 data 이면
            val0 = valueList[64] + valueList[93]
            val1 = valueList[118]
            val2 = valueList[119]
            val3 = valueList[121]
        elif time == '21051300': # 2021.05.13 00시의 data 이면
            val0 = valueList[52] + valueList[81]
            val1 = valueList[106]
            val2 = valueList[107]
            val3 = valueList[109]
        elif time == '21051200': # 2021.05.12 00시의 data 이면
            val0 = valueList[100] + valueList[129]
            val1 = valueList[153]
            val2 = valueList[154]
            val3 = valueList[156]
        elif time == '21051100': # 2021.05.11 00시의 data 이면
            val0 = valueList[52] + valueList[81]
            val1 = valueList[108]
            val2 = valueList[109]
            val3 = valueList[111]
        elif time == '21051000': # 2021.05.10 00시의 data 이면
            val0 = valueList[101] + valueList[130]
            val1 = valueList[158]
            val2 = valueList[159]
            val3 = valueList[161]
        elif time == '21050900': # 2021.05.09 00시의 data 이면
            val0 = valueList[92] + valueList[121]
            val1 = valueList[149]
            val2 = valueList[150]
            val3 = valueList[152]
        elif time == '21050800': # 2021.05.08 00시의 data 이면
            val0 = 118234 + valueList[119]
            val1 = valueList[153]
            val2 = valueList[154]
            val3 = valueList[156]
        elif time == '21050700': # 2021.05.07 00시의 data 이면
            val0 = valueList[97] + valueList[126]
            val1 = valueList[151]
            val2 = valueList[152]
            val3 = valueList[154]
        elif time == '21050600': # 2021.05.06 00시의 data 이면
            val0 = valueList[89] + valueList[118]
            val1 = valueList[140]
            val2 = valueList[141]
            val3 = valueList[143]
        elif time == '21050500': # 2021.05.05 00시의 data 이면
            val0 = valueList[90] + valueList[119]
            val1 = valueList[152]
            val2 = valueList[153]
            val3 = valueList[155]
        elif time == '21050400': # 2021.05.04 00시의 data 이면
            val0 = valueList[90] + valueList[119]
            val1 = valueList[144]
            val2 = valueList[145]
            val3 = valueList[147]
        elif time == '21050300': # 2021.05.03 00시의 data 이면
            val0 = valueList[87] + valueList[116]
            val1 = valueList[143]
            val2 = valueList[144]
            val3 = valueList[146]
        elif time == '21050100': # 2021.05.01 00시의 data 이면
            val0 = valueList[94] + valueList[124]
            val1 = valueList[154]
            val2 = valueList[155]
            val3 = valueList[157]
        elif time == '21043000' or time == '21050200':
            val0 = valueList[87] + valueList[116]
            val1 = valueList[142]
            val2 = valueList[143]
            val3 = valueList[145]
        elif time == '21042900': # 2021.04.29 00시의 data 이면
            val0 = valueList[94] + valueList[123]
            val1 = valueList[154]
            val2 = valueList[155]
            val3 = valueList[157]
        elif time == '21042800': # 2021.04.28 00시의 data 이면
            val0 = valueList[90] + valueList[119]
            val1 = valueList[149]
            val2 = valueList[150]
            val3 = valueList[152]
        elif time == '21042700': # 2021.04.27 00시의 data 이면
            val0 = valueList[87] + valueList[116]
            val1 = valueList[147]
            val2 = valueList[148]
            val3 = valueList[150]
        elif time == '21042600': # 2021.04.26 00시의 data 이면
            val0 = valueList[94] + valueList[123]
            val1 = valueList[150]
            val2 = valueList[151]
            val3 = valueList[153]
        elif time == '21042500': # 2021.04.25 00시의 data 이면
            val0 = valueList[173] + valueList[260]
            val1 = valueList[339]
            val2 = valueList[342]
            val3 = valueList[348]
        elif time == '21042400': # 2021.04.24 00시의 data 이면
            val0 = valueList[97] + valueList[126]
            val1 = valueList[153]
            val2 = valueList[154]
            val3 = valueList[156]
        elif time == '21042300': # 2021.04.23 00시의 data 이면
            val0 = valueList[93] + valueList[122]
            val1 = valueList[153]
            val2 = valueList[154]
            val3 = valueList[156]
        elif time == '21042200': # 2021.04.22 00시의 data 이면
            val0 = valueList[94] + valueList[123]
            val1 = valueList[149]
            val2 = valueList[150]
            val3 = valueList[152]
        elif time == '21041100': # 2021.04.11 00시의 data 이면
            val0 = valueList[39] + valueList[68]
            val1 = valueList[97]
            val2 = valueList[98]
            val3 = valueList[100]
        elif time == '21040500': # 2021.04.05 00시의 data 이면
            val0 = valueList[40] + valueList[69]
            val1 = valueList[97]
            val2 = valueList[98]
            val3 = valueList[100]
        elif time == '21040300': # 2021.04.03 00시의 data 이면
            val0 = valueList[38] + valueList[69]
            val1 = valueList[97]
            val2 = valueList[98]
            val3 = valueList[100]
        elif time == '21033000': # 2021.03.30 00시의 data 이면
            val0 = valueList[38] + valueList[67]
            val1 = valueList[96]
            val2 = valueList[97]
            val3 = valueList[99]
        elif time == '21031200': # 2021.03.12 00시의 data 이면
            val0 = valueList[40] + valueList[70]
            val1 = valueList[98]
            val2 = valueList[99]
            val3 = valueList[101]
        elif time == '21031100': # 2021.03.11 00시의 data 이면
            val0 = valueList[38] + valueList[68]
            val1 = valueList[96]
            val2 = valueList[97]
            val3 = valueList[99]
        elif time == '21031000': # 2021.03.10 00시의 data 이면
            val0 = valueList[39] + valueList[69]
            val1 = valueList[91]
            val2 = valueList[92]
            val3 = valueList[94]
        elif time == '21030900': # 2021.03.09 00시의 data 이면
            val0 = valueList[38] + valueList[68]
            val1 = valueList[83]
            val2 = valueList[84]
            val3 = valueList[86]
        elif time == '21030700' or time == '21030800':
            val0 = valueList[38] + valueList[68]
            val1 = valueList[92]
            val2 = valueList[93]
            val3 = valueList[95]
        elif time == '21030500': # 2021.03.05 00시의 data 이면
            val0 = valueList[38] + valueList[68]
            val1 = valueList[90]
            val2 = valueList[91]
            val3 = valueList[93]
        elif time == '21030200': # 2021.03.02 00시의 data 이면
            val0 = valueList[38] + valueList[69]
            val1 = valueList[94]
            val2 = valueList[95]
            val3 = valueList[97]
        elif time == '21030100': # 2021.03.01 00시의 data 이면
            val0 = valueList[38] + valueList[69]
            val1 = valueList[95]
            val2 = valueList[96]
            val3 = valueList[98]
        elif time == '21022700': # 2021.02.27 00시의 data 이면
            val0 = int(valueList[38]) + valueList[68]
            val1 = valueList[89]
            val2 = valueList[90]
            val3 = valueList[92]
        elif time == '21020700' or time == '21040200':
            val0 = int(valueList[38]) + valueList[67]
            val1 = valueList[102]
            val2 = valueList[103]
            val3 = valueList[105]
        elif time == '21012200': # 2021.01.22 00시의 data 이면
            val0 = int(valueList[38]) * 10000 + int(valueList[39]) + valueList[68]
            val1 = valueList[93]
            val2 = valueList[94]
            val3 = valueList[96]
        elif time == '21012100' or time == '21012300' or time == '21012500' or time == '21020800' or time == '21021400' or time == '21021700' or time == '21042100':
            val0 = int(valueList[38]) + valueList[67]
            val1 = valueList[98]
            val2 = valueList[99]
            val3 = valueList[101]
        elif (time == '21011400' or time == '21011600' or time == '21012700' or time == '21013100' or time == '21020200' or
              time == '21020600' or time == '21021800' or time == '21022500' or time == '21022800' or time == '21032100' or
              time == '21040400' or time == '21040900' or time == '21041500' or time == '21041600'):
            val0 = int(valueList[38]) + valueList[67]
            val1 = valueList[97]
            val2 = valueList[98]
            val3 = valueList[100]
        elif time == '21011000': # 2021.01.10 00시의 data 이면
            val0 = int(valueList[39]) + valueList[70]
            val1 = valueList[105]
            val2 = valueList[106]
            val3 = valueList[108]
        elif time == '21010500' or time == '21013000' or time == '21021000' or time == '21041700':
            val0 = valueList[38] + valueList[67]
            val1 = valueList[100]
            val2 = valueList[101]
            val3 = valueList[103]
        elif time == '21010300': # 2021.01.03 00시의 data 이면
            val0 = valueList[39] + valueList[69]
            val1 = valueList[92]
            val2 = valueList[93]
            val3 = valueList[95]
        elif time == '20123100': # 2020.12.31 00시의 data 이면
            val0 = valueList[39] + valueList[70]
            val1 = valueList[98]
            val2 = valueList[99]
            val3 = valueList[101]
        elif time == '20122900': # 2020.12.29 00시의 data 이면
            val0 = valueList[39] + valueList[69]
            val1 = valueList[94]
            val2 = valueList[95]
            val3 = valueList[97]
        elif time == '20121800' or time == '21031500':
            val0 = valueList[38] + valueList[67]
            val1 = valueList[89]
            val2 = valueList[90]
            val3 = valueList[92]
        elif time == '20121100' or time == '20122200' or time == '21020900' or time == '21022000':
            val0 = int(valueList[38]) + valueList[67]
            val1 = valueList[99]
            val2 = valueList[100]
            val3 = valueList[102]
        elif time == '20121000' or time == '21022600':
            val0 = int(valueList[38]) + valueList[67]
            val1 = valueList[101]
            val2 = valueList[102]
            val3 = valueList[104]
        elif (time == '20120800' or time == '20121500' or time == '20122600' or time == '21010100' or time == '21010400' or
              time == '21022400' or time == '21032400'):
            val0 = valueList[38] + valueList[67]
            val1 = valueList[95]
            val2 = valueList[96]
            val3 = valueList[98]
        elif (time == '20120700' or time == '20120900' or time == '20121600' or time == '20123000' or time == '21010700' or
              time == '21010800' or time == '21011100' or time == '21011800' or time == '21011900' or time == '21020300' or
              time == '21020500' or time == '21021600' or time == '21022300' or time == '21031600' or time == '21031900' or time == '21040800'):
            val0 = int(valueList[38]) + valueList[67]
            val1 = valueList[96]
            val2 = valueList[97]
            val3 = valueList[99]
        elif time == '20120500' or time == '20122400':
            val0 = int(valueList[38]) + valueList[68]
            val1 = valueList[93]
            val2 = valueList[94]
            val3 = valueList[96]
        elif time == '20120400' or time == '20122700' or time == '21011200' or time == '21012400' or time == '21012900' or time == '21020400' or time == '21040100':
            val0 = valueList[38] + valueList[67]
            val1 = valueList[90]
            val2 = valueList[91]
            val3 = valueList[93]
        elif (time == '20120200' or time == '20120600' or time == '20122100' or time == '20122300' or time == '20122800' or
              time == '21010600' or time == '21010900' or time == '21011700' or time == '21012000' or time == '21021100' or
              time == '21021900' or time == '21022100' or time == '21022200' or time == '21031400' or time == '21032200' or
              time == '21041000' or time == '21041900' or time == '21042000'):
            val0 = int(valueList[38]) + valueList[67]
            val1 = valueList[94]
            val2 = valueList[95]
            val3 = valueList[97]
        elif time == '20113000': # 2020.11.30 00시의 data 이면
            val0 = valueList[38] + valueList[67]
            val1 = 0
            val2 = 0
            val3 = 0
        elif time == '20112900' or time == '20121400':
            val0 = int(valueList[38]) + valueList[68]
            val1 = valueList[101]
            val2 = valueList[102]
            val3 = valueList[104]
        elif time == '20112800' or time == '21032500':
            val0 = valueList[38] + valueList[67]
            val1 = valueList[88]
            val2 = valueList[89]
            val3 = valueList[91]
        elif time == '20112600': # 2020.11.26 00시의 data 이면
            val0 = int(valueList[38]) + valueList[67]
            val1 = valueList[112]
            val2 = valueList[113]
            val3 = valueList[115]
        elif (time == '20112500' or time == '20121900' or time == '21011300' or time == '21012800' or time == '21021300' or
              time == '21032600' or time == '21040700' or time == '21041400'):
            val0 = int(valueList[38]) + valueList[67]
            val1 = valueList[91]
            val2 = valueList[92]
            val3 = valueList[94]
        elif time == '20112200' or time == '20112300':
            val0 = valueList[39] + valueList[70]
            val1 = valueList[94]
            val2 = valueList[95]
            val3 = valueList[97]
        elif time == '20112000': # 2020.11.20 00시의 data 이면
            val0 = valueList[39] + valueList[70]
            val1 = valueList[99]
            val2 = valueList[100]
            val3 = valueList[102]
        elif (time == '20111900' or time == '21010200' or time == '21011500' or time == '21012600' or time == '21030600' or
              time == '21031700' or time == '21032000' or time == '21032300' or time == '21040600' or time == '21041300'):
            val0 = valueList[38] + valueList[67]
            val1 = valueList[92]
            val2 = valueList[93]
            val3 = valueList[95]
        elif time == '20111600': # 2020.11.16 00시의 data 이면
            val0 = valueList[39] + valueList[70]
            val1 = valueList[92]
            val2 = valueList[93]
            val3 = valueList[95]
        elif time == '20111300' or time == '20111700' or time == '20112700':
            val0 = valueList[39] + valueList[70]
            val1 = valueList[96]
            val2 = valueList[97]
            val3 = valueList[99]
        elif time == '20111100' or time == '20111800' or time == '20120100' or time == '21020100':
            val0 = valueList[38] + valueList[67]
            val1 = valueList[95]
            val2 = valueList[96]
            val3 = valueList[98]
        elif (time == '20110500' or time == '20111200' or time == '20120300' or time == '20121700' or time == '20122000' or
              time == '21021200' or time == '21021500' or time == '21030300' or time == '21030400' or time == '21031300' or
              time == '21031800' or time == '21032700' or time == '21032800' or time == '21032900' or time == '21033100' or time == '21041200' or time == '21041800'):
            val0 = int(valueList[38]) + valueList[67]
            val1 = valueList[93]
            val2 = valueList[94]
            val3 = valueList[96]
        elif time == '20110300' or time == '20111000':
            val0 = valueList[39] + valueList[70]
            val1 = valueList[95]
            val2 = valueList[96]
            val3 = valueList[98]
        elif time == '20103100' or time == '20110200' or time == '20110400' or time == '20111500' or time == '20112400':
            val0 = valueList[39] + valueList[70]
            val1 = valueList[97]
            val2 = valueList[98]
            val3 = valueList[100]
        elif time == '20093000': # 2020.09.30 00시의 data 이면
            val0 = valueList[42] + valueList[73]
            val1 = int(str(valueList[88]) + str(valueList[89]))
            val2 = int(str(valueList[90]) + str(valueList[91]))
            val3 = valueList[93]
        elif time == '20092000': # 2020.09.20 00시의 data 이면
            val0 = valueList[38] + valueList[73]
            val1 = valueList[88]
            val2 = valueList[89]
            val3 = valueList[91]
        elif time == '20091700': # 2020.09.17 00시의 data 이면
            val0 = valueList[39] + int(valueList[72])
            val1 = valueList[88]
            val2 = valueList[89]
            val3 = valueList[91]
        elif time == '20091000': # 2020.09.10 00시의 data 이면
            val0 = valueList[40] + valueList[71]
            val1 = valueList[86]
            val2 = valueList[87]
            val3 = valueList[89]
        elif time == '20090600': # 2020.09.06 00시의 data 이면
            val0 = valueList[39] + valueList[72]
            val1 = valueList[88]
            val2 = valueList[89]
            val3 = valueList[91]
        elif time == '20090900': # 2020.09.09 00시의 data 이면
            val0 = valueList[39] + valueList[70]
            val1 = valueList[84]
            val2 = valueList[85]
            val3 = valueList[87]
        elif (time == '20082800' or time == '20082900' or time == '20100200' or time == '20101000' or time == '20101100' or
              time == '20101200' or time == '20102800' or time == '20102900' or time == '20110100' or time == '20110600' or
              time == '20111400' or time == '20112100' or time == '20121200' or time == '20121300' or time == '20122500'):
            val0 = int(valueList[38]) + valueList[67]
            val1 = valueList[82]
            val2 = valueList[83]
            val3 = valueList[85]
        elif (time == '20082100' or time == '20083000' or time == '20083100' or time == '20090100' or time == '20091200' or
              time == '20091400' or time == '20091500' or time == '20091600' or time == '20092100' or time == '20092200' or
              time == '20092300' or time == '20092400' or time == '20092500' or time == '20092700' or time == '20092800' or
              time == '20092900' or time == '20100100' or int(time) >= 20100300):
            val0 = valueList[39] + valueList[70]
            val1 = valueList[85]
            val2 = valueList[86]
            val3 = valueList[88]
        elif (time == '20082000' or time == '20082200' or time == '20082300' or time == '20082400' or time == '20082500' or
              time == '20083000' or time == '20083100' or time == '20090300' or time == '20090400' or time == '20090500' or
              time == '20090700' or time == '20091300' or time == '20091800' or time == '20091900'):
            val0 = valueList[39] + int(valueList[71])
            val1 = valueList[87]
            val2 = valueList[88]
            val3 = valueList[90]
        elif time == '20081200' or time == '20081300' or time == '20090200' or time == '20091100':
            val0 = valueList[39] + valueList[69]
            val1 = valueList[84]
            val2 = valueList[85]
            val3 = valueList[87]
        elif time == '20081100' or time == '20081400' or time == '20081900' or time == '20090800':
            val0 = valueList[39] + valueList[71]
            val1 = valueList[86]
            val2 = valueList[87]
            val3 = valueList[89]
        elif time == '20080900': # 2020.08.09 00시의 data 이면
            val0 = valueList[38] + valueList[74]
            val1 = valueList[90]
            val2 = valueList[91]
            val3 = valueList[93]
        elif time == '20080500' or time == '20080800':
            val0 = valueList[38] + valueList[69]
            val1 = valueList[85]
            val2 = valueList[86]
            val3 = valueList[88]
        elif (time == '20072200' or time == '20073000' or time == '20073100' or time == '20080300' or time == '20080400' or
              time == '20080600' or time == '20080700' or time == '20081000' or time == '20082600' or time == '20082700'):
            val0 = valueList[38] + valueList[69]
            val1 = valueList[84]
            val2 = valueList[85]
            val3 = valueList[87]
        elif time == '20072400': # 2020.07.24 00시의 data 이면
            val0 = valueList[37] + valueList[66]
            val1 = valueList[81]
            val2 = valueList[82]
            val3 = valueList[84]
        elif time == '20072600': # 2020.07.26 00시의 data 이면
            val0 = valueList[39] + valueList[68]
            val1 = valueList[83]
            val2 = valueList[84]
            val3 = valueList[86]
        elif time == '20080100' or time == '20080200':
            val0 = valueList[38] + valueList[70]
            val1 = valueList[86]
            val2 = valueList[87]
            val3 = valueList[89]
        else:
            val0 = valueList[38] + valueList[67]
            val1 = valueList[82]
            val2 = valueList[83]
            val3 = valueList[85]
        result += str(time) + ' ' + str(val0) + ' ' + str(val1) + ' ' + str(val2) + ' ' + str(val3) + ' '
        for i in range(74): result += '0 '
        result += '0#'
        continue
    
    # append to result
    # result(크롤링 결과 테이블)의 구성 (총 80 열):
    #     1열: 날짜시간 (yyMMddhh)
    #  2~ 8열: 확진합계(=격리해제+격리중+사망), 격리해제, 격리중, 사망, 검사합계(=검사중+음성), 검사중, 음성 (전국 기준)
    #  9~26열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
    # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
    # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
    # 63~80열: 지역별 합계    (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
    #                 (=격리중+격리해제+사망자수)
    
    print('')
    print('# APPEND TO RESULT #')

    ###     1열: 날짜시간 (yyMMddhh)
    
    resultAppend = str(time) + ' ' # result 에 추가할 내용

    ###  2~ 8열: 확진합계(=격리해제+격리중+사망), 격리해제, 격리중, 사망, 검사합계(=검사중+음성), 검사중, 음성 (전국 기준)
    
    if int(time) >= 20022016: # 2020.02.20 16시 이후의 data 이면
        if int(time) == 20070800: # 2020.07.08 00시의 data 이면
            resultAppend += str(valueList[32]) + ' ' + str(valueList[33]) + ' ' + str(valueList[34]) + ' ' + str(valueList[35]) + ' '
            resultAppend += str(valueList[36]+valueList[37]) + ' ' + str(valueList[36]) + ' ' + str(valueList[37]) + ' '
        elif int(time) == 20070400: # 2020.07.04 00시의 data 이면
            resultAppend += str(valueList[31]) + ' ' + str(valueList[32]) + ' ' + str(valueList[33]) + ' ' + str(valueList[34]) + ' '
            resultAppend += str(valueList[35]+valueList[36]) + ' ' + str(valueList[35]) + ' ' + str(valueList[36]) + ' '
        elif int(time) >= 20031400: # 2020.03.14 00시 이후의 data 이면
            resultAppend += str(valueList[30]) + ' ' + str(valueList[31]) + ' ' + str(valueList[32]) + ' ' + str(valueList[33]) + ' '
            resultAppend += str(valueList[34]+valueList[35]) + ' ' + str(valueList[34]) + ' ' + str(valueList[35]) + ' '
        elif time == '20030109': # 2020.03.01 09시의 data 이면
            for j in range(30, 36): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[36]) + ' '
        else: # 2020.03.01 09시 외의 data 이면
            for j in range(31, 37): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[37]) + ' '
            
    else: # 2020.02.20 09시까지의 data 이면
        if time == '20021816': resultAppend += '31 12 19 0 9741 818 8923 ' # 02.18 16시
        elif time == '20021716': resultAppend += '30 10 20 0 8688 708 7980 ' # 02.17 16시
        elif time == '20021709': resultAppend += '30 9 21 0 8141 408 7733 ' # 02.17 09시
        elif time == '20021609': resultAppend += '29 9 20 0 7890 577 7313 ' # 02.16 09시
        elif time == '20021116': resultAppend += '28 4 24 0 4297 762 3535 ' # 02.11 09시
        elif time == '20021009': resultAppend += '27 3 24 0 2749 809 1940 ' # 02.10 09시
        else: # 상기한 시각의 자료 외의 경우 아래와 같은 일반적인 규칙에 따라 크롤링
            resultAppend += str(valueList[30]) + ' ' + str(valueList[32]) + ' ' + str(valueList[31]) + ' 0 '
            resultAppend += str(valueList[33]) + ' ' + str(valueList[34]) + ' ' + str(valueList[35]) + ' '

    ###  9~26열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
    ### 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
    ### 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
    ### 63~80열: 지역별 합계    (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
    ###                 (=격리중+격리해제+사망자수)

    if int(time) >= 20030600: # 2020.03.06 00시 이후의 data이면

        #  9~26열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
        # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
        # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)

        if time == '20050300':

            # 9~16열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(37, 49): resultAppend += str(valueList[j]) + ' '
            resultAppend += '15 '
            for j in range(49, 53): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[53]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(55, 72): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[72]) + ' '

            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(74, 91): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[91]) + ' '

        elif (time == '20041900' or time == '20042400' or time == '20042500' or time == '20042600' or time == '20050800'
             or time == '20050900' or time == '20051000' or time == '20051100' or time == '20051300' or time == '20051500'
             or time == '20051600' or time == '20051700' or time == '20051900' or time == '20052000' or time == '20052200'
             or time == '20052400' or time == '20052700' or time == '20052800' or time == '20052900' or time == '20053000'
             or time == '20060400' or time == '20060500' or time == '20060600' or time == '20060700' or time == '20060800'
             or time == '20061100' or time == '20061300' or time == '20061400' or time == '20061500' or time == '20062100'
             or time == '20062200' or time == '20062400' or time == '20062600' or time == '20062700' or time == '20062800'
             or time == '20062900' or time == '20063000' or time == '20070100' or time == '20070200' or time == '20070300'
             or time == '20070400' or time == '20071100' or time == '20071300' or time == '20071400' or time == '20071500'):

            # 9~16열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(37, 54): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[54]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(56, 73): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[73]) + ' '

            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(75, 92): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[92]) + ' '

        elif (time == '20062000'): # 2020.06.20 00시의 data이면

            # 9~16열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(43, 60): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[60]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(62, 79): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[79]) + ' '
            
            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(81, 98): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[98]) + ' '

        elif (time == '20061900'): # 2020.06.19 00시의 data이면

            # 9~16열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(41, 58): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[58]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(60, 77): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[77]) + ' '
            
            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(79, 96): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[96]) + ' '

        elif (time == '20061800'): # 2020.06.18 00시의 data이면

            # 9~16열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(40, 57): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[57]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(59, 76): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[76]) + ' '
            
            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(78, 95): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[95]) + ' '

        elif (time == '20070800'): # 2020.07.08 00시의 data이면

            # 9~16열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(39, 56): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[56]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(58, 75): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[75]) + ' '
            
            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(77, 94): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[94]) + ' '

        elif (time == '20061000'): # 2020.06.10 00시의 data이면

            # 9~16열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(38, 55): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[55]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(57, 74): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[74]) + ' '
            
            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(76, 93): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[93]) + ' '

        elif int(time) >= 20040400: # 2020.04.04 00시 이후의 data이면

            # 9~16열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(36, 53): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[53]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(55, 72): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[72]) + ' '

            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(74, 91): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[91]) + ' '

        elif int(time) >= 20031600: # 2020.03.16 00시 이후의 data이면

            # 9~26열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(43, 60): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[60]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(62, 79): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[79]) + ' '

            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(81, 98): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[98]) + ' '

        elif int(time) >= 20031400: # 2020.03.14 00시 이후의 data이면

            # 9~26열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(43, 60): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[60]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(61, 78): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[78]) + ' '

            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(79, 96): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[96]) + ' '

        elif time == '20030800': # 2020.03.08 00시의 data이면

            # 9~26열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(47, 64): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[64]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(65, 82): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[82]) + ' '

            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(83, 100): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[100]) + ' '
            
        else: # 그렇지 않으면
            # 9~26열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(46, 63): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[63]) + ' '

            # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(64, 81): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[81]) + ' '

            # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
            for j in range(82, 99): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[99]) + ' '

        # 63~80열: 지역별 합계    (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
        #                 (=격리중+격리해제+사망자수)
        if (time == '20041900' or time == '20042400' or time == '20042500' or time == '20042600' or time == '20050800'
            or time == '20050900' or time == '20051000' or time == '20051100' or time == '20051300' or time == '20051500'
            or time == '20051600' or time == '20051700' or time == '20051900' or time == '20052000' or time == '20052200'
            or time == '20052400' or time == '20052700' or time == '20052800' or time == '20052900' or time == '20053000'
            or time == '20060400' or time == '20060500' or time == '20060600' or time == '20060700' or time == '20060800'
            or time == '20061100' or time == '20061300' or time == '20061400' or time == '20061500' or time == '20062100'
            or time == '20062200' or time == '20062400' or time == '20062600' or time == '20062700' or time == '20062800'
            or time == '20062900' or time == '20063000' or time == '20070100' or time == '20070200' or time == '20070300'
            or time == '20070400' or time == '20071100' or time == '20071300' or time == '20071400' or time == '20071500'):
            
            for j in range(94, 111): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[111]) + '#'

        elif (time == '20062000'): # 2020.06.20 00시의 data이면
            for j in range(100, 117): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[117]) + '#'

        elif (time == '20061900'): # 2020.06.19 00시의 data이면
            for j in range(98, 115): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[115]) + '#'

        elif (time == '20061800'): # 2020.06.18 00시의 data이면
            for j in range(97, 114): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[114]) + '#'

        elif (time == '20070800'): # 2020.07.08 00시의 data이면
            for j in range(96, 113): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[113]) + '#'

        elif (time == '20061000'): # 2020.06.10 00시의 data이면
            for j in range(95, 112): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[112]) + '#'
            
        elif int(time) >= 20040400: # 2020.04.04 0시 이후의 data이면
            for j in range(93, 110): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[110]) + '#'

        elif int(time) >= 20033000: # 2020.03.30 0시 이후의 data이면
            for j in range(101, 118): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[118]) + '#'
            
        elif int(time) >= 20031600: # 2020.03.16 0시 이후의 data이면
            for j in range(100, 117): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[117]) + '#'
            
        elif int(time) >= 20031400: # 2020.03.14 0시 이후의 data이면
            for j in range(97, 114): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[114]) + '#'
        
        elif time == '20030700' or int(time) >= 20030900: # 2020.03.07 0시의 data이거나, 2020.03.09 0시 이후의 data이면
            for j in range(100, 117): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[117]) + '#'
            
        elif time == '20030800': # 2020.03.08 0시의 data이면
            resultAppend += str(valueList[101]) + ' '
            for j in range(103, 119): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[119]) + '#'
            
        else: # 어떤 것도 아니면
            for j in range(101, 118): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[118]) + '#'
            
    else: # 그 이전의 (~2020.03.05) data이면

        #  9~26열: 지역별 격리중  (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
        # 27~44열: 지역별 격리해제(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
        # 45~62열: 지역별 사망자수(순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
        # 위 3가지의 데이터는 제공되지 않으므로 N(null)으로 표시
        for j in range(17): resultAppend += 'N '
        resultAppend += 'N '
        for j in range(17): resultAppend += 'N '
        resultAppend += 'N '
        for j in range(17): resultAppend += 'N '
        resultAppend += 'N '

        # 63~80열: 지역별 합계    (순서: 전국 서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주)
        #                 (=격리중+격리해제+사망자수)
        if int(time) >= 20030300: # 2020.03.03 0시 이후
            for j in range(66, 83): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[83]) + '#'
            
        elif time == '20030200': # 2020.03.02 0시
            for j in range(83, 100): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[100]) + '#'
            
        elif int(time) >= 20022616: # 2020.02.26 16시 이후 ~ 2020.03.01까지
            resultAppend += str(valueList[len(valueList)-1]) + ' '
            for j in range(len(valueList)-18, len(valueList)-2): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[len(valueList)-2]) + '#'
            
        else: # 2020.02.06 09시 이전 데이터는 제공되지 않음
            for j in range(17): resultAppend += 'N '
            resultAppend += 'N#'

    print(resultAppend)

    result += resultAppend # 전체 데이터인 result에 해당 질병관리본부 보도자료 링크의 자료 추가

# 파일에 쓰기
ff.write(result)
ff.close()
    
# result persing (tab으로 구분되어 있어서 복사하기 쉬움)
fff = open('result.txt', 'r')
fl = fff.readlines()[0].replace('#', '\n').replace(' ', '\t')
fff.close()
ffff = open('result_.txt', 'w')
ffff.write(fl)
ffff.close()
