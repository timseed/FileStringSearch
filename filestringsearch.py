import logging.config

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
        self.logger.debug("In Dump")
        for i in self.results:
            print('{}'.format(i.strip()))

if __name__=="__main__":
    import logging.config
    import logging
    import argparse
    import yaml

    parser = argparse.ArgumentParser()
    parser.add_argument('-m',  type=str, dest = 'mainfile',help = 'Main Data file to search')
    parser.add_argument('-k',  type=str, dest = 'keyfile', help='Key file (One per line)')
    args = parser.parse_args()


    with open('logging.yaml', 'rt') as f:
        config = yaml.safe_load(f.read())
        f.close()
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
    logger.info("FileSearch is starting")
    fss = filestringsearch(args.mainfile,args.keyfile)
    fss.dump()
    logger.info("FileSearch finished")


