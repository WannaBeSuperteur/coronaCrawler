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
            
        try:
            a = int(a)
            valueList.append(a)
        except:
            if a == '-': valueList.append(0)
            elif a == ' ' and daegu: valueList.append(0)
            elif len(a) >= 2:
                if a[len(a)-1] == '*' and int(time) >= 20031200: valueList.append(str(a[:len(a)-1]))

    print('')
    print('# VALUE LIST: LENGTH' + str(len(valueList)) + ' #')
    print(valueList)
    
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
        if int(time) >= 20031400: # 2020.03.14 00시 이후의 data 이면
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

        if int(time) >= 20040400: # 2020.04.04 00시 이후의 data이면

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
        if int(time) >= 20040400: # 2020.04.04 0시 이후의 data이면
            for j in range(93, 110): resultAppend += str(valueList[j]) + ' '
            resultAppend += str(valueList[110]) + '#'
            
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
