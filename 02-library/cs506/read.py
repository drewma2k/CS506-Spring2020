def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    with open(csv_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            res.append([eval(x) for x in line.split(',')])

    return res
