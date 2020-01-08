#https://www.cnblogs.com/liujiacai/p/7804848.html
import logging,time,datetime
logger = logging.getLogger('ooooo')
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

#console = logging.StreamHandler()
#console.setLevel(logging.INFO)

logger.addHandler(handler)
#logger.addHandler(console)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
try:
    #open("sklearn.txt","rb")
    time.sleep(5)
except (SystemExit,KeyboardInterrupt):
    pass
except Exception:
    logger.error("Faild to open sklearn.txt from logger.error",exc_info = True)
finally:
    print '====end=====',datetime.datetime.now()
    exit()
