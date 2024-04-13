import datetime


class Base():
    def __init__(self, browser):
        self.browser = browser

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print("Good url")

    """Method screenshots"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screen = 'screenshot' + now_date + '.png'
        self.browser.save_screenshot('C:\\Users\\Komp-880-PC\\PycharmProjects\\Screen' + name_screen)