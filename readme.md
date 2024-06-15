# LYProcess 立院處理器

## Introduction
This project aims to harness the power of open data released by the  [Legislative Yuan open data platform](https://data.ly.gov.tw),
to uncover hidden truth within the vast trove of information.

這個專案的目標是希望能透過[立法院開放資料](https://data.ly.gov.tw)，從海量的資料中挖掘出被淹沒的客觀事實。

## File structure
- `download/`: all downloaded data
    - `csv/`: csv files, typically directly downloaded fron [LY open data platform](https://data.ly.gov.tw)
    - `doc/`: doc files, typically downloaded from `docUrl` presented in the `.csv` files
        - file prefix:
            - LCEWC: 議事錄
            - LCIDC: 院會、黨團協商紀錄
            - LCEWA: 議案提案
- `parsed/`: parsed data
    - `doc_csv/`: convert all `download/doc` into csv format
        - csv fiels:
            - basic paragraph: `text`, `style`, `space_before`, `space_after`
            - in a table: `col_id`, `row_id`
            - cell info: `cell_width`, `cell_height`, `cell_id`
            - cell with same `cell_id` is in the same table
            - cell that merges other cells will have `cell_width` > 1 or `cell_height` > 1

## scripts
execute in sequential:
- `script01_download_csv.py`: download all csv files
- `script02_download_doc.py`: download all doc files listed in csv files
- `script03_read_doc.py`: parse all doc files

## How to participate
歡迎修改或利用這些程式來下載、分析立法院公開資料。歡迎提出各種建議、或直接拿去修改使用。

## Related projects
- 零時政府 g0v 有不少相關專案：https://dev.g0v.tw/Project-TWLY.html，大多已經超10年。
- 或許能更方便存取各種立法院資訊的API： https://github.com/openfunltd/ly.govapi.tw

# 立法院運作模式
> 來源：[立法院/開放國會/國會知識家](https://www.ly.gov.tw/Pages/List.aspx?nodeid=113)

## 會期
- 立法院會期每年兩次，自行集會。
- 每年二月至五月底、九月至十二月底是法定集會期間，必要時得依法延長會期。
- 立法委員每年2月1日、9月1日起報到，由各黨團協商決定開議日期。
- 若經總統解散後改選者，於選舉結果公告後第3日起報到，第10日開議。
- 立法院於停開院會期間，遇有重大事項發生，經立法委員1/4以上之請求，可以恢復開會。
- 此外，經總統之咨請或立法委員1/4以上之請求，得開臨時會。 

## 會議
### 院會
- 立法院會議簡稱院會，每週二、五舉行
- 每次院會9時至10時為國是論壇時間。
- 必要時經院會決議：
    - 可以增減會次
    - 由黨團協商合併若干日為1次會議。
- 出席條件
    - 院會須有委員總額1/3出席始得開會。
### 委員會
- 8個委員會：內政、外交及國防、經濟、財政、教育及文化、交通、司法及法制、社會福利
- 4個特種委員會：紀律、程序、修憲、經費稽核
- 召集委員應於收到書面後15日內定期召集會議：
    - 委員會會議於院會日期外，由召集委員召集。
    - 經委員會1/3以上之委員，以書面記明討論之議案及理由，提請召開。
- 院會及委員會會議公開舉行，必要時，可依法召開秘密會議。 
- 審查項目
    - 院會交付審查之議案
    - 人民請願書
    - 總統發布之緊急命令
    - 罷免或彈劾總統或副總統案
    - 對行政院院長提出之不信任案
- 招開方式
    - 得於每會期開始，邀請相關部會作業務報告並備質詢。
    - 由全體委員組成的全院委員會(舊版有關全院各委員會聯席會之文字刪除)，行使任命同意權：
        - 司法院院長、副院長、大法官、考試院院長、副院長、考試委員、監察院院長、副院長、監察委員、審計長
    - 遇有行政院移請覆議案時舉行之。
- 出席條件
    - 委員會會議須有1/3委員出席，始得開會
    - 出席委員不足3人時不得議決。
    - 各委員會至少13位委員，最多不得超過15位。委員會置召集委員2人，由各委員會委員互選之。
- 其他規定
    - 依憲法增修條文規定，立法院解散後，應於60日內舉行立法委員選舉，並於選舉結果確認後10日內自行集會；
    - 休會期間，遇有行政院移請覆議案時，應於7日內自行集會。
    - 立法院經總統解散後，在新選出之立法委員就職前，視同休會。
    - 惟遇有總統發布緊急命令之情況，則應於3日內自行集會。
## 立法程序

1. 提案的來源為：
    - 行政院 (預算案專屬於行政院)
    - 司法院
    - 考試院
    - 監察院
    - 立法委員
    - 符合立法院組織法規定之黨團

2. 程序委員會
    - 由秘書長編擬議事日程，經程序委員會審定後付印。
    - 程序委員會置委員19人，由各政黨(團)依其在院會席次之比例分配。
    - 但每一政黨(團)至少1人。院會審議法案的先後順序，由程序委員會決定。

3. 一讀：於院會中朗讀標題
    - 政府提案或委員所提法律案列入議程報告事項，於院會中朗讀標題(一讀)後，即應交付有關委員會審查或逕付二讀。
    - 委員提出之其他議案，於朗讀標題後，由提案人說明提案旨趣，經大體討論後，依院會之決議，交付審查或逕付二讀或不予審議。
    - 預算案於交付審查之前，行政院院長、主計長及財政部部長應列席院會，報告施政計畫及預算編製經過並備詢。

4. 審查會(逕付二讀)
    - 委員會審查議案時，可以邀請政府人員及社會上有關係人員列席就所詢事項說明事實或發表意見，以供委員參考。
    - 法律案交付審查後，性質相同者可以併案審查。
    - 已逐條討論通過之條文，不能因併案而再行討論。
    - 議案審查完竣後，應就該議案應否交由黨團協商，予以議決。
    - 院會討論各委員會議決不須黨團協商之議案，得經院會同意，不須討論，逕依審查意見處理。
    - 各委員會為審查院會交付之議案，得依規定舉行公聽會：
        - 邀請正、反意見相當比例之政府人員及社會上有關係人士出席表達意見。
        - 將意見提出報告，送交本院全體委員及出席者，作為審查該議案之參考。

5. 二讀：討論經各委員會審查之議案，或經院會決議逕付二讀之議案。
    - 二讀時先朗讀議案，再依次進行廣泛討論及逐條討論。
    - 二讀會是相當重要的一個環節，對於議案之深入討論、修正、重付審查、撤銷、撤回等，均是在這個階段做成決議。
    - 經過二讀之議案，應於下次會議進行三讀；
    - 如有出席委員提議，15人以上連署或附議，經表決通過，得於二讀後繼續三讀。

6. 三讀會
    - 除發現議案內容有互相牴觸，或與憲法、其他法律相牴觸者外，祇得為文字之修正。
    - 立法院議事，除法律案、預算案應經三讀程序議決外，其餘議案僅需經二讀會議決。
7. 復議、動議
    - 委員對於法律案、預算案部分或全案之決議有異議時，得依法於原案表決後，下次院會散會前，提出復議動議。
    - 復議動議經表決後，不得再為復議之動議。
    - 每屆立法委員任期屆滿時，除預(決)算及人民請願案外，尚未議決之議案，下屆不予繼續審議。
    - 完成三讀之法律案及預算案由立法院咨請總統公布並函送行政院。
    - 總統應於收到10日內公布之，或依憲法增修條文第3條規定之程序，由行政院移請立法院覆議。

# 資料來源：
## 可能比較重要的：
### [委員會審議之議案](https://data.ly.gov.tw/getds.action?id=46)
- fields: term, sessionPeriod, meetingNo, billNo, billName, docUrl, selectTerm
- docUrl 可以找到條文比較表 pdf 檔
- example: https://data.ly.gov.tw/odw/ID46Action.action?term=10&sessionPeriod=04&sessionTimes=01&meetingTimes=&fileType=csv

### [院會表決資料](https://data.ly.gov.tw/getds.action?id=370)
- fields: term, sessionPeriod, voteDate, voteTime, voteIssue, voteType, url
- url 可以找到當次表決贊成反對棄權的委員 xls 檔
- example: https://data.ly.gov.tw/odw/usageFile.action?id=370&type=CSV&fname=370_CSV.csv
- example url: https://ppg.ly.gov.tw/ppg/BillThirdReadingPassesClause/download/resources/ppgb32100/C202303071540380.xlsx

### [黨團協商](https://data.ly.gov.tw/getds.action?id=8)
- fields: comYear, comVolume, comBookId, term, sessionPeriod, sessionTimes, meetingTimes, meetingDate, meetingName, subject, pageStart, pageEnd, docUrl, htmlUrl, selectTerm
- subject 用於搜尋相關聯的議案
- docUrl 可以找到協商會議紀錄 doc 檔
- example: https://data.ly.gov.tw/odw/ID8Action.action?meetingDateS=101/01/01&meetingDateE=200/12/31&fileType=csv

### [委員會紀錄](https://data.ly.gov.tw/getds.action?id=22)
- example: https://data.ly.gov.tw/odw/usageFile.action?id=22&type=CSV&fname=22_1101CSV-1.csv
- fields: comYear, comVolume, comBookId, term, sessionPeriod, sessionTimes, meetingTimes, meetingDate, meetingName, subject, pageStart, pageEnd, docUrl, selectTerm
- docUrl 可以找到會議紀錄 doc 檔
- subject 用於搜尋關聯議案


### [院會紀錄](https://data.ly.gov.tw/getds.action?id=21)
- fields: comYear, comVolume, comBookId, term, sessionPeriod, sessionTimes, meetingTimes, meetingDate, meetingName, subject, pageStart, pageEnd, docUrl, htmlUrl, selectTerm
- example: https://data.ly.gov.tw/odw/ID21Action.action?term=11&sessionPeriod=01&meetingDateS=110/06/01&meetingDateE=113/12/31&fileType=csv
- docUrl 可以找到院會紀錄 doc 檔，含表決

### [會議完整影片相關資訊](https://data.ly.gov.tw/getds.action?id=143)
- fields: term, sessionPeriod, meetingDate, meetingTime, meetingTypeName, meetingName, meetingContent, videoUrl, selectTerm
- videoUrl 連結到IVOD
- example: https://data.ly.gov.tw/odw/usageFile.action?id=143&type=CSV&fname=143_1101CSV-1.csv

### [委員發言片段相關影片資訊](https://data.ly.gov.tw/getds.action?id=148)
- fields: term, sessionPeriod, meetingDate, meetingTime, meetingTypeName, meetingName, meetingContent, legislatorName, areaName, speechStartTime, speechEndTime, speechRecordUrl, videoLength, videoUrl, selectTerm
- speechRecordUrl 純文字逐字稿發言內容
- videoUrl IVOD 影片連結
- example: https://data.ly.gov.tw/odw/usageFile.action?id=148&type=CSV&fname=148_1101CSV-1.csv


## 其他所有資料
### URL 說明
- 說明頁 url: https://data.ly.gov.tw/getds.action?id=`id`
- 文件直接下載 url: https://data.ly.gov.tw/odw/usageFile.action?id=`id`&type=CSV&fname=`id`_`xxxx`CSV-1.csv
  - `xxxx`: 屆次/會期，例如 `1101` = 第十一屆 第一會期
  - 不是所有文件都能這樣下載
- API url: https://data.ly.gov.tw/odw/ID`id`Action.action?term=`term`&sessionPeriod=`session`&meetingDateS=`YYY`/`MM`/`DD`&meetingDateE=`YYY`/`MM`/`DD`&fileType=csv
  - `term`: 屆次，例如 `11` = 第十一屆
  - `session`: 會期，例如 `01` = 第一會期
  - `YYY`/`MM`/`DD`: 開始結束民國年月日，例如 `113/06/15`
  - 有時候不知道為什麼撈不到東西
### ID 與項目對應
- 1: 質詢事項(行政院答復部分)
- 2: 行政院答復
- 3: 報告事項
- 4: 討論事項
- 5: 同意權行使事項
- 6: 質詢事項(本院委員質詢部分)
- 7: 國是論壇
- 8: 黨團協商
- 9: 當屆委員資料
- 13: 當屆委員會-基本資料
- 14: 各委員會-委員名單資料
- 16: 歷屆委員資料
- 19: 法律條文對照表
- 20: 議案提案
- 21: 院會紀錄
- 22: 委員會紀錄
- 23: 報告事項決定
- 24: 討論事項決議
- 25: 議事日程原始檔案
- 41: 公報原始檔案
- 42: 會議資訊
- 44: 臨時提案
- 45: 議事錄原始檔案
- 46: 委員會審議之議案
- 48: 三讀通過議案
- 142: 遊說案件申請登記
- 143: 會議完整影片相關資訊
- 144: 遊說案件變更登記
- 145: 遊說案件終止登記
- 146: 年度申報財務收支報表
- 147: 終止登記申報財務收支報表
- 148: 委員發言片段相關影片資訊
- 153: 法律提案(API)
- 154: 委員發言(API)
- 221: 院會發言名單
- 223: 委員會登記發言名單
- 281: 機關權威檔
- 301: 法名稱權威檔
- 321: 同義詞權威檔
- 367: 委員會公聽會報告資訊
- 370: 院會表決資料
- 373: 三讀通過條文&附帶決議資訊
- 10770: 資訊安全政策
- 10771: 隱私權政策
- 10772: 立法院網站資料開放宣告
- 44938: 法制局研究成果(API)
- 44939: 預算中心研究成果(API)