class _ContextConfig(dict):
    """
    This class want to be a static global class that stores all the global
    config of running environment
    """
    def __init__(self):
        super().__init__(**{})

    def __getattribute__(self, name):
        return self[name]

    def __setattr__(self, key, value):
        self[key] = value


class _GlobalConfig:
    """
    This class manage configurations for all the app and can manage individual
    configs for each crawler
    """

    def __init__(self):
        self.running_config: dict = None
        self._crawlers = {}

    def get_config_crawler(self, name: str):
        """Get config for specific crawler

        :return: return Crawlino object
        :rtype: Crawlino

        """
        return self._crawlers[name]

    def add_crawler_crawler(self, crawler):
        self._crawlers[crawler.name] = crawler


current_config = _GlobalConfig()

__all__ = ("current_config", )
