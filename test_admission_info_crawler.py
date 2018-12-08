# -*- coding: utf-8 -*-

import unittest
import admission_info_crawler as crawler
import re


class TesCrawler(unittest.TestCase):
    homepage_html = crawler.get_homepage_html()
    homepage_generator = crawler.parse_homepage(homepage_html)

    def setUp(self):
        pass

    def test_0_get_html(self):
        """
        Test case function to check the get_html function
        """
        print("Start get_html test\n")
        print("Testing for get_html valid url test")
        valid_url = 'https://www.baidu.com'
        self.assertIsNotNone(crawler.get_html(valid_url))
        print("Testing for get_html invalid url test")
        invalid_url = "One shades more, one rays less, has half impaired the nameless grace"
        self.assertIsNone(crawler.get_html(invalid_url))
        print("\nFinish get_html test\n")

    def test_1_get_homepage_html(self):
        """
        Test case function to check the get_homepage_html
        """
        print("Start get_homepage_html test\n")
        expected_title = "<title>2019浙江三位一体招生报考指南--中国教育在线</title>"
        acquired_content = crawler.get_homepage_html()
        self.assertTrue(re.search(expected_title, acquired_content))
        print("\nFinish get_html test\n")

    def test_2_parse_homepage(self):
        """
        Test case function to check the parse_homepage_html
        """
        print("Start parse_homepage test\n")
        school_dict = self.homepage_generator.__next__()
        print(school_dict)
        self.assertEqual(school_dict, {'name': '浙江工业大学',
                                       'date': '3月5日—3月19日',
                                       'link': "http://gaokao.eol.cn/zhe_jiang/dongtai/201802/t20180211_1585545.shtml"
                                       })
        print("\nFinish parse_homepage test\n")

    def test_3_write_homepage_form_to_excel(self):
        """
        Test case function to check the write_homepage_form_to_excel
        """
        sheet = crawler.sheet

        # Test if the header is successfully recorded
        self.assertEqual(sheet.cell(row=1, column=1).value, "高校名单")
        self.assertEqual(sheet.cell(row=1, column=2).value, "报名时间")
        self.assertEqual(sheet.cell(row=1, column=3).value, "招生简章")
        self.assertEqual(sheet.cell(row=2, column=1).value, "浙江工业大学")
        self.assertEqual(sheet.cell(row=2, column=2).value, "3月5日-3月10日")
        self.assertEqual(sheet.cell(row=2, column=3).value,
                         "http://gaokao.eol.cn/zhe_jiang/dongtai/201802/t20180211_1585545、"
                         ".shtml")

        print("Start write_homepage_form_to_excel test")


if __name__ == "__main__":
    unittest.main()
