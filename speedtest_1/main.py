
from TestManager import TestManager

if __name__ == '__main__':
    print("Tests werden gestartet")
    # hier wird promptConfig() aufgerufen
    testManager = TestManager(True)
    # hier wird der Speedtest durchgeführt
    testManager.speedtest()

    for result in testManager.results:
        print(result)
