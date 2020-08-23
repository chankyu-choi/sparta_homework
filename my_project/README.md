## 카카오 채팅 봇 만들기
### 기능 설명  
- 알람 기능 (필수)
  - 기념일
- 생활 뉴스 (필수)
  - 날씨
  - 주가
  - 실시간 키워드
- 부가 기능 (선택)
  - AI 챗봇 (GPT-3 기반)
- 레퍼런스 :[둘기의 삽질 일기](!https://dulki.tistory.com/category/%EA%B0%9C%EB%B0%9C/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%86%A1%20%EB%B4%87) 

### 레이아웃
- Front-end
  - 4주차 과제(원페이지 쇼핑몰)를 참고하여,
  - `날짜`, `기념일 내용`, `날씨`, `주가(코스피 지수)`, `실시간 키워드`를 입력 받고, 출력한다.
- Back-end
  - FE 에서 넘어온 값들을 처리한다. (저장, 불렁오기)
  - 매일 특정 시간에 `날씨`, `주가(코스피 지수)`, `실시간 키워드`를 수집한다.
- 카카오 Bot
  - 기념일을 등록할 수 있음 (예, `기념일 등록, 7월 21일, 최찬규 생일`)
  - 매일 특정 시간에 `기념일 내용`, `날씨`, `주가(코스피 지수)`, `실시간 키워드`를 출력한다.
- ![layout.jpeg](https://raw.githubusercontent.com/chankyu-choi/sparta_homework/master/layout.jpeg)

### 개발일지 (TIL)
- 20200812
  - [X] [FE] index.html 제작
  - [X] [BE] 스케쥴러 API 테스트 (주기적으로 날씨, 주가, 실시간 키워드 등의 정보를 크롤링 하기 위한 목적)
- 20200824
  - [X] [6주차 강의 복습](https://www.notion.so/6-31016b3771ae4afb8b0d1c8d9941a508)
    - AWS에 flast 설치하고, 5000 포트 열어서 test.py 실행
  - [X] 날씨, 주가, 실시간 키워드 크롤링 소스 
    - 기상청 날씨 정보 : http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109
    - 주가 정보
       - 코스피 : https://finance.naver.com/sise/sise_index.nhn?code=KOSPI
       - 네이버 : https://finance.naver.com/item/main.nhn?code=035420
    - 실시간 키워드 (06:00)
       - https://datalab.naver.com/keyword/realtimeList.naver?datetime=2020-08-24T06%3A00%3A00
  - [ ] 카카오톡 연동 방법 검색 (feasible test 진행중)
    - [ ] ~~NOX 등 애뮬레이터 설치하려고 했으나 맥에서 잘 안됨~~ 
    - [X] 모바일 공기계 구해서 TextNow 설치하고, 핸드폰 번호 발급 받아 카카오톡 계정 발급 완료
   