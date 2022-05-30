
from TestManager import TestManager

if __name__ == '__main__':
    print("Tests werden gestartet")
    testManager = TestManager(True)
    testManager.speedtest()

    for result in testManager.results:
        print(result)
