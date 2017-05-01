from core.property_finder import *


class DuckDuckGoTests(unittest.TestCase, PropertyFinder):

    def setUp(self):
        PropertyFinder.__init__(self)
        self.mobile_driver.implicitly_wait(10)  # Give simulator time to load the app.

    def test_open_article_in_browser(self):
        self.mobile_driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]"
                                                 "/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]"
                                                 "/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]"
                                                 "/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]"
                                                 "/android.view.View[1]/android.support.v7.widget.RecyclerView[1]"
                                                 "/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]"
                                                 "").click()  # DuckDuckGo article menu has no resource id.
        self.mobile_driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.ListView[1]"
                                                 "/android.widget.TextView[3]").click()
        self.assertNotEqual(self.mobile_driver.current_activity, self.android_capabilities['appActivity'])

    def test_share_article(self):
        self.mobile_driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]"
                                                 "/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]"
                                                 "/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]"
                                                 "/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]"
                                                 "/android.view.View[1]/android.support.v7.widget.RecyclerView[1]"
                                                 "/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]"
                                                 "").click()  # DuckDuckGo article menu has no resource id.
        self.mobile_driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.ListView[1]"
                                                 "/android.widget.TextView[2]").click()
        self.assertNotEqual(self.mobile_driver.current_activity, self.android_capabilities['appActivity'])

    def tearDown(self):
        self.mobile_driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DuckDuckGoTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
