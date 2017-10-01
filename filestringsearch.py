import logging
import logging.config
import yaml


class filestringsearch(object):

    def __init__(self,file,keys_to_find):
        self.logger = logging.getLogger(__name__)
        self.logger.debug('{} initialized')
        self.keys=[]
        self.results=[]
        with open(keys_to_find,'rt') as kf:
            for line in kf:
                self.keys.append(line.strip())
        self.logger.debug("We have {} keys loaded".format(len(self.keys)))

        with open(file,"rt",encoding='utf-8',errors='ignore') as main_file:
            for line in main_file:
                for k in self.keys:
                    if k in line:
                        self.results.append(line)

    def dump(self):
        for i in self.results:
            print('{}'.format(i.strip()))

if __name__=="__main__":
    import logging.config
    import logging

    with open('logging.yaml', 'rt') as f:
        config = yaml.safe_load(f.read())
        f.close()
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    logger.info("FileSearch is starting")
    fss = filestringsearch("/Users/tim/Dev/SecLists/Passwords/alleged-gmail-passwords.txt", "keys.txt")
    fss.dump()
    logger.info("FileSearch finished")



