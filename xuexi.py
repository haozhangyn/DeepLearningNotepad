from selenium import webdriver
import time
import numpy as np
import pandas as pd

papers = pd.read_csv('paper.csv', engine='python')
videos = pd.read_csv('video.csv', engine='python')

study_paper_list=[]#papers.values
study_video_list=[] #videos.values


def get_current_window(driver):
    current_window = driver.current_window_handle
    all_windows = driver.window_handles
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)

def roll_page(driver):
    js_bottom = "var q=document.documentElement.scrollTop=10000"
    #js_bottom2 = "window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js_bottom)
    #driver.execute_script(js_bottom2)

def paper_study(driver):
    driver.find_element_by_xpath('//*[@id="root"]/div/header/div[2]/div[1]/div[1]/a[3]').click()
    get_current_window(driver)
    time.sleep(5)
    paper_list = driver.find_elements_by_class_name('text-link-item-title')
    print(paper_list)
    #paper.click()
    time.sleep(1)
    for i, paper in enumerate(paper_list):
        if i>=6:
            break
        if paper.text not in study_paper_list:
            paper.click()
            study_paper_list.append(paper.text)
            roll_page(driver)
            time.sleep(62)

def get_today_score(driver):
    driver.find_element_by_xpath("//a[text()='我的积分']").click()
    time.sleep(5)
    paper_score_card = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]')
    video_n_score_card = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[3]/div[2]/div[1]/div[2]')
    video_t_score_card = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[4]/div[2]/div[1]/div[2]')
    paper_score = paper_score_card.text.splite('/')[0].replace('分')
    video_n_score = video_n_score_card.text.splite('/')[0].replace('分')
    video_t_score = video_t_score_card.text.splite('/')[0].replace('分')
    return paper_score, video_n_score, video_t_score


def get_today_score(driver):
    driver.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div/a').click()
    get_current_window(driver)
    time.sleep(3)
    driver.find_element_by_xpath("//a[text()='我的积分']").click()
    time.sleep(5)
    paper_score_card = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]')
    video_n_score_card = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[3]/div[2]/div[1]/div[2]')
    video_t_score_card = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[4]/div[2]/div[1]/div[2]')
    paper_score = paper_score_card.text.splite('/')[0].replace('分')
    video_n_score = video_n_score_card.text.splite('/')[0].replace('分')
    video_t_score = video_t_score_card.text.splite('/')[0].replace('分')
    return paper_score, video_n_score, video_t_score


def video_study(driver):

    driver.find_element_by_xpath("//a[text()='学习电视台']").click()
    time.sleep(10) #//*[@id="root"]/div/header/div[2]/div[1]/div[1]/a[1]
    get_current_window(driver)
    driver.find_element_by_xpath('//*[@id="495f"]/div/div/div/div/div/section/div/div/div/div[1]/div[1]/div/div').click()
    get_current_window(driver)
    time.sleep(10)
    video_list = driver.find_elements_by_class_name('textWrapper')
    print(video_list)  #//*[@id="1novbsbi47k-5"]/div/div/div/div/div/div/section/div[3]/section/div/div/div[1]/div[1]/div[1]
    for i, video in enumerate(video_list):
        if i>=6:
            break
        if video.text not in study_video_list:
            study_video_list.append(video.text)
            video.click()
            time.sleep(62)




def everyday_answer_question(driver):
    driver.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div/a').click()
    get_current_window(driver)
    time.sleep(3)
    driver.find_element_by_xpath("//*[text()='我的学习']").click()
    time.sleep(5)
    get_current_window(driver)
    driver.find_element_by_xpath('//*[text()="我要答题"]').click()
    time.sleep(4)
    get_current_window(driver)
    driver.find_element_by_xpath("//*[text()='每日答题']").click()
    time.sleep(4)
    for i in range(6):
        time.sleep(1)
        chooses = driver.find_elements_by_class_name('choosable')  # q-answer choosable
        time.sleep(1)
        driver.find_element_by_xpath("//*[contains(text(),'查看提示')]").click()
        time.sleep(1)

        # get_current_window(driver)
        if len(chooses) != 0:

            tips = driver.find_elements_by_xpath('//font[@color="red"]')
            driver.find_element_by_xpath("//*[contains(text(),'查看提示')]").click()
            answers = [tip.text.lstrip() for tip in tips]
            for choose in chooses:
                tmp_ans = choose.text.split('.')[1].lstrip()
                print(tmp_ans)
                print(answers)
                print(tmp_ans in answers)
                if tmp_ans in answers:
                    print('ppppp')
                    choose.click()
            driver.find_element_by_tag_name('button').click()
            # get_current_window(driver)
        else:
            tip = driver.find_element_by_xpath('//font[@color="red"]')
            # Sget_current_window(driver)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input').send_keys(
                tip.text)
            driver.find_element_by_xpath("//*[contains(text(),'查看提示')]").click()

            driver.find_element_by_tag_name('button').click()
            # get_current_window(driver)

def everyweek_answer_question(driver):
    driver.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div/a').click()
    get_current_window(driver)
    time.sleep(3)
    driver.find_element_by_xpath("//*[text()='我的学习']").click()
    time.sleep(5)
    get_current_window(driver)
    driver.find_element_by_xpath('//*[text()="我要答题"]').click()
    time.sleep(4)
    get_current_window(driver)
    driver.find_element_by_xpath("//*[text()='每周答题']").click()
    time.sleep(4)
    t = driver.page_source
    print(t)
    #get_current_window(driver)
    buttons = driver.find_elements_by_tag_name('button')

    print('tttt')
    print(buttons)
    for button in buttons:
        print(button.text)
        if button.text =='重新答题':
            button.click()
            break
    time.sleep(4)
    for i in range(6):
        time.sleep(1)
        chooses = driver.find_elements_by_class_name('choosable') #q-answer choosable
        time.sleep(1)
        driver.find_element_by_xpath("//*[contains(text(),'查看提示')]").click()
        time.sleep(1)

        #get_current_window(driver)
        if len(chooses) != 0:
            time.sleep(1)
            tips = driver.find_elements_by_xpath('//font[@color="red"]')
            driver.find_element_by_xpath("//*[contains(text(),'查看提示')]").click()
            answers = [tip.text.lstrip() for tip in tips]
            for choose in chooses:
                tmp_ans = choose.text.split('.')[1].lstrip()
                print(tmp_ans)
                print(answers)
                print(tmp_ans in answers)
                if tmp_ans in answers:
                    print('ppppp')
                    choose.click()
            driver.find_element_by_tag_name('button').click()
            #get_current_window(driver)
        else:
            tip = driver.find_element_by_xpath('//font[@color="red"]')
            #Sget_current_window(driver)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input').send_keys(tip.text)

            driver.find_element_by_xpath("//*[contains(text(),'查看提示')]").click()

            driver.find_element_by_tag_name('button').click()
            #get_current_window(driver)

def personal_answer_question(driver):
    driver.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div/a').click()
    get_current_window(driver)
    time.sleep(3)
    driver.find_element_by_xpath("//*[text()='我的学习']").click()
    time.sleep(5)
    get_current_window(driver)
    driver.find_element_by_xpath('//*[text()="我要答题"]').click()
    time.sleep(4)
    get_current_window(driver)
    driver.find_element_by_xpath("//*[text()='专项答题']").click()
    time.sleep(4)
    t = driver.page_source
    print(t)
    #get_current_window(driver)
    buttons = driver.find_elements_by_tag_name('button')

    print('tttt')
    print(buttons)
    for button in buttons:
        print(button.text)
        if button.text =='已满分':
            button.click()
            break
    time.sleep(4)
    for i in range(11):
        time.sleep(1)
        chooses = driver.find_elements_by_class_name('choosable') #q-answer choosable
        time.sleep(1)
        driver.find_element_by_xpath("//*[contains(text(),'查看提示')]").click()
        time.sleep(1)

        #get_current_window(driver)
        if len(chooses) != 0:
            time.sleep(1)
            tips = driver.find_elements_by_xpath('//font[@color="red"]')
            driver.find_element_by_xpath("//*[contains(text(),'查看提示')]").click()
            answers = [tip.text.lstrip() for tip in tips]
            for choose in chooses:
                tmp_ans = choose.text.split('.')[1].lstrip()
                print(tmp_ans)
                print(answers)
                print(tmp_ans in answers)
                if tmp_ans in answers:
                    print('ppppp')
                    choose.click()
            driver.find_element_by_tag_name('button').click()
            #get_current_window(driver)
        else:
            tip = driver.find_element_by_xpath('//font[@color="red"]')
            #Sget_current_window(driver)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[2]/div/input').send_keys(tip.text)

            driver.find_element_by_xpath("//*[contains(text(),'查看提示')]").click()

            driver.find_element_by_tag_name('button').click()
            #get_current_window(driver)





def study():
    driver = webdriver.Chrome()
    driver.get("https://pc.xuexi.cn/points/login.html?ref=https%3A%2F%2Fwww.xuexi.cn%2Findex.html")
    #print(driver.get_cookies())
    #driver.find_elements_by_css_selector('"input[type=\"butt\"]"')
    #cookie = [{'domain': '.xuexi.cn', 'expiry': 1599989716, 'httpOnly': False, 'name': 'zwfigprt', 'path': '/', 'secure': False, 'value': 'b3e9257d13677b10e6daf1a5a52d432b'}, {'domain': '.xuexi.cn', 'httpOnly': False, 'name': 'webUmidToken', 'path': '/', 'secure': False, 'value': 'T2gAITGySbNZTv64fq5NkIc_OcpIo7AFcr5X9lsUFSR42skJ_mZg-rSNYF6gt4qfKyg_HkpKdLm1t3OG5D2vTn9I'}, {'domain': '.xuexi.cn', 'expiry': 1599989716, 'httpOnly': False, 'name': 'tmzw', 'path': '/', 'secure': False, 'value': '1599903316563'}, {'domain': '.xuexi.cn', 'expiry': 1631439314, 'httpOnly': False, 'name': '__UID__', 'path': '/', 'secure': False, 'value': '42ec50a0-f4db-11ea-b2dc-23d698c8caee'}, {'domain': '.xuexi.cn', 'httpOnly': False, 'name': 'uaToken', 'path': '/', 'secure': False, 'value': '122#pAE/cJVdEExjGEpZy4pjEJponDJE7SNEEP7ZpJRBuDPpJFQLpCGwoHZDpJEL7SwBEyGZpJLlu4Ep+FQLpoGUEELon4yE7SNEEP7ZpERBuDPE+BQPpC76EJponDJLKMQEI1P+XDJ2tO9/a2Ie3P7Ny0VJaEBthWO/8AHtG0solH+YDu7fqcbCmg50o1Aw5lVDqMf21DLxnSp4AObEDtVZ8CL6JDEEyBfDqWv2EEpadBZ9kxgbELVrtFpUJDEbyo3mqW32E5pangL4uO0EDtVZ8CL6JNEEyBfDqMf2DEpxnSp1uOIEEIhr8Cpka4bEyofm7g/qEWfACI5KjOa2rJVS3eT6udRshnEuNNdB7McWigItD3WXFlmAkt7QAWzTwhBTJX4zMVHvAVjw5ZkZVeZTWdTMOAfTM0+XbYABriwzMg+lq9K+HLFTpjHSckcp/XzTZzClKKsC/WB/ivn86zN6OVkp7Jkic1SL9Lr/h8ivG5l1VOLAi4lA112XE36dOwv06GIZ2oo1F7cHWTfXIbGFO6o2p0QsMq+jt5lSIQQbYafEMF6sJNEmQyc3Ig02pEhc25WJKp5NjiR+QFMAfzttPlYYkXFbcDifrD2dzdbcBjjTIoXgIv9XCEDqE2LWgPa/0gLVf6EgoLOtQu4QjjX+rQQ9uRUkQ03Dz7urxMWh2nu+eM6e1Z3PXmUo8eXaQMaBNGxBIfOI4Q5chafgRaYCA7rVBYP9LAv0TAv/dOSJtUIszQO3UsAJh1q1UtzHYBdf3stx3zoR3sAVYNyRp0BHDuGU7A/dtTje40QjeSAiLqSddHtm63AmQFKnpE=='}, {'domain': 'pc.xuexi.cn', 'expiry': 1915263314, 'httpOnly': False, 'name': '_uab_collina', 'path': '/points', 'secure': False, 'value': '159990331435512460021351'}]
    #driver.add_cookie(cookie)
    #driver.refresh()
    time.sleep(10)
    try:
        paper_study(driver)
        print("文章学习完成")
    except Exception as e:
        print(e)
        pass
    try:
        video_study(driver)
        print("视频学习完成")
    except Exception as e:
        print(e)
        pass
    try:
        print("开始答题")
        everyday_answer_question(driver)
    except Exception as e:
        print(e)
        pass

    try:
        personal_answer_question(driver)
    except Exception as e:
        print(e)
        pass
    try:
        everyweek_answer_question(driver)
    except Exception as e:
        print(e)
        pass

    driver.quit()





if __name__ =='__main__':
    study()
    df_paper = pd.DataFrame(study_paper_list)
    df_video = pd.DataFrame(study_video_list)
    df_paper.to_csv('paper.csv',index=None)
    df_video.to_csv('video.csv',index=None)






