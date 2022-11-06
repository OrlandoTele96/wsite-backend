from configparser import ConfigParser

class ConfigParserDB:
    def __init__(self,filepath,section):
        self.filepath=filepath
        self.section=section

    def getConfig(self):
        #print ("Parsing Config to DB")
        parser=ConfigParser()
        parser.read(self.filepath)
        db={}
        if parser.has_section(self.section):
            #print("Configuration with file: \t", self.section)
            params = parser.items(self.section)
            for param in params:
                db[param[0]]=param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(self.section, self.filepath))
        return db

