from core.modules import *


class PropertyFinder(object):

    def __init__(self):
        self.capabilities_location = os.path.join(os.getcwd(), 'core', 'capabilities.ini')
        self.android_capabilities = {}
        self.mobile_driver = None
        self.driver_uri = None
        self.set_capabilities()
        self.get_app_location()
        self.start_driver()

    def set_capabilities(self):
        capabilities = ConfigParser()
        capabilities.optionxform = str
        capabilities.read(self.capabilities_location)
        for section in capabilities.sections():
            for option in capabilities.options(section):
                if section == "Android":
                    self.android_capabilities[option] = capabilities.get(section, option)
                if option == 'android_server':
                    self.driver_uri = capabilities.get(section, option)

    def start_driver(self):
        self.mobile_driver = app.Remote(self.driver_uri, self.android_capabilities)

    def get_app_location(self):
        self.android_capabilities['app'] = os.path.join(os.getcwd(), 'core', 'apps', self.android_capabilities['app'])
