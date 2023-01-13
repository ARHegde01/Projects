import sys
import unittest


def most_active_cookies(cookie_log, date):
    cookie_counter = {}
    with open(cookie_log) as cfile:
        for line in cfile:
            cookie, datetime = line.strip().split(',')
            datetime = datetime[:10]
            if (datetime == date):
                if cookie not in cookie_counter:
                    cookie_counter[cookie] = 1
                else:
                    cookie_counter[cookie] += 1
    highest_count = max(cookie_counter.values())
    most_active = [cookie for cookie,
                   num in cookie_counter.items() if num == highest_count]
    return most_active


class UnitTestMostActiveCookies(unittest.TestCase):
    def most_active_cookies_singular_test(self):
        cookie_file = "cookie_log.csv"
        date = "2018-12-09"
        expected_result = ["AtY0laUfhglK3lC7"]
        self.assertEqual(most_active_cookies(
            cookie_log, date), expected_result)

    def most_active_cookies_multitude_test(self):
        cookie_file = "cookie_log.csv"
        date = "2018-12-08"
        expected_result = ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf"]
        self.assertEqual(most_active_cookies(
            cookie_log, date), expected_result)

    def most_active_cookie_none_test(self):
        cookie_log = "cookie_log.csv"
        date = "2018-12-04"
        expected_result = []
        self.assertEqual(most_active_cookies(
            cookie_log, date), expected_result)


if __name__ == '__main__':
    cookie_log = sys.argv[1]
    date = sys.argv[2]
    most_active_cookies = most_active_cookies(cookie_log, date)
    for cookie in most_active_cookies:
        print(cookie)

    unittest.main()
