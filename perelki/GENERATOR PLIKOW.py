# wrzucic do folderu wdi[x] i uruchomic podac ilosc zad

directory = input("nazwa folderu w programowanie:")
num_of_files = int(input("Ile plików:")) + 1


for i in range(1, int(num_of_files)):
    name = "./{0}/zad {1}TODO.py".format(directory , i)
    fp = open(name, "x")
    fp.close()

print("done")
