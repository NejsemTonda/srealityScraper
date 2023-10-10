BOT_NAME = "sreality"

SPIDER_MODULES = ["sreality.spiders"]
NEWSPIDER_MODULE = "sreality.spiders"

ROBOTSTXT_OBEY = False


# uncomment this pipeline, if you wish to also save to postgreSQL 
#ITEM_PIPELINES = {
#    "sreality.pipelines.SrealityPipeline": 300,
#}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
