import pandas as pd

df = pd.read_excel("股票代码.xlsx")
data = list(df['股票代码'])
for k in data:
    if k >= 100000:
        k = k
    else :
        k = str(k).zfill(6)
    try:
        for i in (2019,1999,-1):
            for j in range(4,0,-1):
                url = 'http://quotes.money.163.com/trade/lsjysj_{}.html?year={}&season={}'.format(k,i,j)
                # print(url)
                gp = pd.read_html(url)[3]
                print(gp.head())
                gp.to_csv(r'D:/stock/{}.csv'.format(k),mode='a',encoding='utf_8_sig',header=True,index=0)

                print('股票'+str(k)+'在'+str (i)+'年第'+str(j)+'季度的数据抓取完成')

    except:
        pass
    continue
print('所有股票数据抓取完成')