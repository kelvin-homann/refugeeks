import pandas as pd
import matplotlib.pyplot as plt


class TestAnalyser:
    def __init__(self, results):
        resultDict = {
            "Download": [],
            "Upload": [],
            "TimeStamp": []
        }

        for res in results:
            resultDict["Download"].append(res.getDownloadInMBits())
            resultDict["Upload"].append(res.getUploadInMBits())
            resultDict["TimeStamp"].append(res.timestamp)

        self.resultFrame = pd.DataFrame(resultDict)
        print(self.resultFrame)

    def writeReport(self):
        resFile = open("result.txt", "w")

        downloadColumn = self.resultFrame["Download"]
        uploadColumn = self.resultFrame["Upload"]

        resFile.write("Download - Max: {} Min: {} Mean: {}\n".format(
            downloadColumn.max(), downloadColumn.min(), downloadColumn.mean()))

        resFile.write("Upload - Max: {} Min: {} Mean: {}\n".format(
            uploadColumn.max(), uploadColumn.min(), uploadColumn.mean()))

        resFile.close()

    def plotResult(self):
        downloadColumn = self.resultFrame["Download"]
        uploadColumn = self.resultFrame["Upload"]
        timesColumn = self.resultFrame["TimeStamp"]

        plt.plot(timesColumn, downloadColumn)
        plt.plot(timesColumn, uploadColumn)
        plt.show()
