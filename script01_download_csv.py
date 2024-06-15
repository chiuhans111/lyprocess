from download import download

term = 11
period = 1

# 委員會審議之議案
download(
    f"https://data.ly.gov.tw/odw/ID46Action.action?term={term:02d}&sessionPeriod={period:02d}&fileType=csv",
    f"./download/csv/委員會審議之議案_{term:02d}{period:02d}.csv"
)

# 黨團協商
download(
    f"https://data.ly.gov.tw/odw/ID8Action.action?meetingDateS=101/01/01&meetingDateE=200/12/31&fileType=csv",
    f"./download/csv/黨團協商.csv"
)

# 院會表決資料
download(
    "https://data.ly.gov.tw/odw/usageFile.action?id=370&type=CSV&fname=370_CSV.csv",
    "./download/csv/院會表決資料.csv"
)

# 委員會紀錄
download(
    f"https://data.ly.gov.tw/odw/usageFile.action?id=22&type=CSV&fname=22_{term:02d}{period:02d}CSV-1.csv",
    f"./download/csv/委員會紀錄_{term:02d}{period:02d}.csv"
)

# 院會紀錄
download(
    f"https://data.ly.gov.tw/odw/ID21Action.action?term={term:02d}&sessionPeriod={period:02d}&meetingDateS=110/06/01&meetingDateE=200/12/31&fileType=csv",
    f"./download/csv/院會紀錄_{term:02d}{period:02d}.csv"
)

# 會議完整影片相關資訊
download(
    f"https://data.ly.gov.tw/odw/usageFile.action?id=143&type=CSV&fname=143_{term:02d}{period:02d}CSV-1.csv",
    f"./download/csv/會議完整影片相關資訊_{term:02d}{period:02d}.csv"
)

# 委員發言片段相關影片資訊
download(
    f"https://data.ly.gov.tw/odw/usageFile.action?id=148&type=CSV&fname=148_{term:02d}{period:02d}CSV-1.csv",
    f"./download/csv/委員發言片段相關影片資訊_{term:02d}{period:02d}.csv"
)

# 委員會公聽會報告資訊
download(
    "https://data.ly.gov.tw/odw/usageFile.action?id=367&type=CSV&fname=367_CSV.csv",
    "./download/csv/委員會公聽會報告資訊.csv"
)

# 議事錄原始檔案
download(
    "https://data.ly.gov.tw/odw/usageFile.action?id=45&type=CSV&fname=45_CSV.csv",
    "./download/csv/議事錄原始檔案.csv"
)

# 議案提案
download(
    f"https://data.ly.gov.tw/odw/usageFile.action?id=20&type=CSV&fname=20_{term:02d}{period:02d}CSV-1.csv",
    f"./download/csv/議案提案_{term:02d}{period:02d}.csv"
)