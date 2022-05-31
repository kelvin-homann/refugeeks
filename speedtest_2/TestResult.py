class TestResult:
    def __init__(self, download, upload, timestamp):
        self.download = download
        self.upload = upload
        self.timestamp = timestamp

    def __str__(self):
        return "{} {} {}".format(self.convertToMBits(self.download), self.convertToMBits(self.upload), self.timestamp)

    def convertToMBits(self, bits):
        return round(bits / 1048576, 2)  # Bits to MBits

    def getDownloadInMBits(self):
        return self.convertToMBits(self.download)

    def getUploadInMBits(self):
        return self.convertToMBits(self.upload)
