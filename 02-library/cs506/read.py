
def read_csv(csv_file_path):
    """
    Given a path to a csv file
    Read data from csv file
    Convert data into its original data type
    return a matrix
    """
    res = []
<<<<<<< HEAD
    with open(csv_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            res.append([eval(x) for x in line.split(',')])

    return res
=======
    with open(csv_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            row = []
            for x in line.split(","):
                row.append(eval(x))
            res.append(row)

    return res

>>>>>>> 1acf19dd2c7705eb45dfacbc6138d2979fdc013f
