
from TestManager import TestManager
from speedtest_2.TestAnalyser import TestAnalyser

print(__name__)

if __name__ == '__main__':
    print("Tests werden gestartet")
    testManager = TestManager(True)
    testManager.speedtest()

    for res in testManager.results:
        print(res)

    testAnalyser = TestAnalyser(testManager.results)
    testAnalyser.writeReport()
    testAnalyser.plotResult()
