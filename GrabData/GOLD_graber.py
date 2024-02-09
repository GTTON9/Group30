
# Gold网页数据爬取
# web报表类型
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class GrabHttp():
    def __init__(self, url  , xpath1):

        print("-----------直接抓取网页上的数据-----------")
        options = Options()
        # 禁止弹窗（此处不需要设置下载路径 因为没有下载任务）
        prefs = {"profile.default_content_settings.popups": 0}
        # 解决cmd运行时出现报错：连到系统上的设备没有发挥作用
        options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        options.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome()

        browser.get(url)
        browser.implicitly_wait(5)  # 隐式等待 在加载完毕之后自动继续运行  超过30秒会报错
        browser.set_page_load_timeout(10)
        time.sleep(1)  # 保险起见再等1秒
        ListValue = []  # 创建空列表
        for i in xpath1:  # 把所有xpath对应的值提取出来，放入一个列表-字典
            Indexid = i.get('IndexID')
            try:
                '''     
                   在生产服务器上，因为存在Xpath直接获取对应的相关数据会出现取值少单位量级的情况，因此现在此处加一个通用方法来解决相对应问题
                以保证此处的取值在生产环境上是正确的。所使用的附加class 是RepairXpathBug类,由于Xpath请求数据量特别大，为了加快请求速度,
                此处的设计方案是先把Xpath传入到对应类中，然后去检查相对应的Xpath,在从匹配表中做过滤用以返回
                '''

                indicator_value = browser.find_element(By.XPATH, i.get('IndexPath'))  # 获取指标展示值

                if (ReairXpathCheck == 0):
                    x_path = i.get('IndexPath')
                    IndexValue = indicator_value.text  # 获取指标展示值并保存
                    count1 = Indexid[2]
                    if(count1 == '03'):
                        print(x_path)
                        print(IndexValue)
                        print("Xpath取值")
                else:

                    print(indicator_value.text)
                    print("未修改值")
                    IndexValue = RepairXpathBug().Repair(indicator_value.text,i.get('IndexPath'))
                    x_path = i.get('IndexPath')
                    print(x_path)
                    print(IndexValue)
                    print("Xpath取值")

                ListValue.append(dict(indicator_id=Indexid, original_value=IndexValue))

            except:
                ListValue.append(dict(indicator_id=Indexid, original_value=None))  # 不能正确获取数据 用空值代替并打印提示
                print("\033[0;31;40m\t！提示：序列号为{}的指标出现了问题，请检查驾驶舱网页和该指标的Xpath\033[0m"
                      .format(Indexid))

        self.IndexValue = ListValue
