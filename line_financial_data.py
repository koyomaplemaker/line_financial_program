import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


token="0xNwGE1c9YLV3EIKYbORf6MsOsAMNiR3ClKgw4I54KQ"
url="https://notify-api.line.me/api/notify"

# S&P500のページ
sp500_url="https://site0.sbisec.co.jp/marble/fund/detail/achievement.do?s_rflg=1&Param6=203311187&int_fd=fund:psearch:search_result"

# オルカンのページ
all_country_url="https://site0.sbisec.co.jp/marble/fund/detail/achievement.do?s_rflg=1&Param6=20331418A&int_fd=fund:psearch:search_result"


# 野村半導体のページ
nomura_ai_url="https://site0.sbisec.co.jp/marble/fund/detail/achievement.do?s_rflg=1&Param6=201313098&int_fd=fund:psearch:search_result"


# webページをヘッドレスモードで立ち上げる
options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

driver.get(sp500_url)
elements = driver.find_elements(By.CLASS_NAME, 'md-l-table-01' and 'md-l-utl-mt4')


sp500_data_01 = elements[52].text
sp500_data_02 = elements[56].text

driver.get(all_country_url)
elements = driver.find_elements(By.CLASS_NAME, 'md-l-table-01' and 'md-l-utl-mt4')


all_country_data_01 = elements[52].text
all_country_data_02 = elements[56].text

driver.get(nomura_ai_url)
elements = driver.find_elements(By.CLASS_NAME, 'md-l-table-01' and 'md-l-utl-mt4')


nomura_ai_data_01 = elements[52].text
nomura_ai_data_02 = elements[56].text


#ドライバーを終了させる
driver.quit()


# ラインに送信用のメッセージに整形する
financial_message = "【S&P500】\n" + sp500_data_01 + sp500_data_02 + "\n\n【オルカン】\n" + all_country_data_01 + all_country_data_02 + "\n\n【野村半導体】\n" + nomura_ai_data_01 + nomura_ai_data_02

# ラインに送信する
auth={"Authorization":"Bearer "+token}
content={"message":financial_message}
requests.post(url,headers=auth, data=content)

#ドライバーを終了させる
driver.quit()