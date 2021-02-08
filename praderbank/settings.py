BOT_NAME = 'praderbank'

SPIDER_MODULES = ['praderbank.spiders']
NEWSPIDER_MODULE = 'praderbank.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 1

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'praderbank.pipelines.PraderbankPipeline': 100,

}