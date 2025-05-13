from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.profile = (By.CSS_SELECTOR,"#app > div > div.header > div > div.header__avatar")
        self.exit = (By.CSS_SELECTOR,"#app > div > div.inforation > div > div > div:nth-child(7) > div")
        self.sure_exit =(By.CSS_SELECTOR,"#dialog > div > div > div.material-dialog__window-actions > button:nth-child(2) > span")
        self.qa = (By.CSS_SELECTOR,"#app > div > div.home-content > div > div > div > div > div.home__education > div.home__education-page > div > div:nth-child(2) > div.home-card__bot > div > div.avatar.baseavatar_go.home-card__bot-content-btn.baseavatar")
        self.ranks =(By.CSS_SELECTOR,"#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(4) > span > span")
        self.homework =(By.CSS_SELECTOR,"#tabbar > div > div.tab-header > div.tab-header__wrapper > div:nth-child(4) > span > span")
        self.select_hw = (By.CSS_SELECTOR,"#app > div > div.container.container_mobile > div > div > div.tab-content.group-homeworks-tab-content > div > div > div > div:nth-child(9) > div.work-dropdown.homework-card_drop.grow > div > div > div.list-tile__leading-box > div > span")

    # def click_profile(self):
    #     WebDriverWait(self.driver,5).until(
    #         EC.element_to_be_clickable(self.profile)
    #     ).click()

    # def click_exit(self):
    #     WebDriverWait(self.driver,5).until(
    #         EC.element_to_be_clickable(self.exit)
    #     ).click()
    #
    # def click_sure_exit(self):
    #     WebDriverWait(self.driver,5).until(
    #         EC.element_to_be_clickable((self.sure_exit))
    #     ).click()

    def click_qa(self):
        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.qa)
        ).click()

    def click_ranks(self):
        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.ranks)
        ).click()

    def click_homework(self):
        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.homework)
        ).click()

    def click_select_hw(self):
        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.select_hw)
        ).click()

