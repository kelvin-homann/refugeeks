
from TestManager import TestManager
from speedtest_2.TestAnalyser import TestAnalyser

if __name__ == '__main__':
    print("Tests werden gestartet")
    testManager = TestManager(False)
    testManager.speedtest()

    for res in testManager.results:
        print(res)

    testAnalyser = TestAnalyser(testManager.results)
    testAnalyser.writeReport()
    testAnalyser.plotResult()
