import csv

def partitioned_values(data, partitioner_ind, value_of_interest_ind):
    result = {}
    for datarow in data:
        if datarow[partitioner_ind] in list(result.keys()):
            result[datarow[partitioner_ind]]['number'] += 1
            result[datarow[partitioner_ind]]['target_value'] += int(datarow[value_of_interest_ind])
        else:
            result[datarow[partitioner_ind]] = {'number': 1, 'target_value': int(datarow[value_of_interest_ind]) }
    return result        


def category_totals(partitioned_values):
    keys = list(partitioned_values.keys())
    values = [x['number'] for x in list(partitioned_values.values())]
    return [keys, values]
    
def columns_into_arrays(data, col_inds):
    results = [[] for x in range(len(col_inds))]
    for datarow in data:
        for col_ind in enumerate(col_inds):
            results[col_ind[0]].append(datarow[col_ind[1]])
    return results    

    
def max_by_column(data, column_ind):
    for datarow in enumerate(data):
        if datarow[0] == 0:
            max_val = datarow[1][column_ind]
        elif datarow[1][column_ind] > max_val:
            max_val = datarow[1][column_ind]
    return max_val     
                    
def category_averages(partitioned_values):
    keys = list(partitioned_values.keys())
    values = [x['target_value'] / float(x['number']) for x in list(partitioned_values.values())]
    return [keys, values]

def read_csv_file(filename):
    with open('student-mat.csv', newline='') as csvfile:
        sniffer = csv.Sniffer()
        # Detect delimiter, quotechar etc. automatically
        dialect = sniffer.sniff(csvfile.read(1024))
        # Go back to beginning
        csvfile.seek(0)
        csvreader = csv.reader(csvfile, dialect)
        return list(csvreader)
