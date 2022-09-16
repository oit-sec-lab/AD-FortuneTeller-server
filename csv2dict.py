import csv

def Csv2Dict(fname):

    with open(fname, "r") as f:
        reader = csv.reader(f)

        csv_dict = {}
    
        for row in reader:
            index = int(row[0])
            url = row[1]
            csv_dict[index] = url

    return csv_dict

if __name__ == "__main__":
    print(Csv2Dict("ryousei.csv"))
