class Processor:
    def __init__(self,reader,writer):
        self.reader = reader
        self.writer = writer
    def process(self):
        while 1:
            data = self.reader.readline()
            if not data: break
            data = self.conventer(data)
            self.writer.write(data)
    def conventer(self, data):
        assert False, 'conventer must be defined'