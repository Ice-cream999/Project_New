import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url - ' + get_url)

    def get_word_for_check(self, word, text):
        word_text = word.text
        assert word_text == text
        print ('Text correct')

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Диана\\PycharmProjects\\pythonProject15\\screen\\' + name_screenshot)
        print(name_screenshot)

    def assert_url(self, url):
        current_url = self.driver.current_url
        assert url == current_url
        print('Good value url')







