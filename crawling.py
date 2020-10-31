# 질병관리본부 보도자료 (https://www.cdc.go.kr/board/board.es?mid=a20501000000&bid=0015) 코로나19 크롤러
# 본 크롤러를 이용하여 수집한 데이터의 외부 공개 시 출처(질병관리본부) 명시 바람.

from urllib.request import urlopen
from bs4 import BeautifulSoup

f = open('list.txt', 'r')
linkList = f.readlines()
f.close()

ff = open('result.txt', 'w')
result = '' # 전체 데이터를 저장

areaList = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

for i in range(len(linkList)): # list.txt 파일에 있는 각 질병관리본부 보도자료 링크에 있는 자료에 대하여 
    link = linkList[i].split(' ')[0]
    time = linkList[i].split(' ')[1].split('\n')[0]

    print('')
    print('### LINK: ' + str(link) + ' ###')
    html = urlopen(link)
    bsObject = BeautifulSoup(html, "html.parser")

    allSpan = bsObject.find_all('span')
    valueList = []
    areaExist = []

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
    print(valueList[:20])
    print(valueList[20:40])
    print(valueList[40:60])
    print(valueList[60:80])
    print(valueList[80:])

    if int(time) >= 20072000: # 2020.07.20 00시 이후의 data 이면
        if time == '20103100': # 2020.10.31 00시의 data 이면
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
              time == '20101200' or time == '20102800' or time == '20102900'):
            val0 = valueList[38] + valueList[67]
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
