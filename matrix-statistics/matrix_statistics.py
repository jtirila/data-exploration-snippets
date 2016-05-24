import csv

def partitioned_values(data, partitioner_ind, value_of_interest_ind):
    """Partitions the data into separate chunks by the value in the column
    specified by the partitioner_ind column number.

    The result is of the form
    {
      'A': { 'number': 8, 'target_value': 234.5 },
      'B': { 'number': 3, 'target_value': 89.6 }
    }

    where 'A' and 'B' are the values present in the partitioned_ind column in
    the data, for each row 'number' is the number of occurrences of that key
    and 'target_value' is the cumulative total of the value_of_interest column
    values for the corresponding group in the partitioner column.

    """
    result = {}
    for datarow in data:
        if datarow[partitioner_ind] in list(result.keys()):
            result[datarow[partitioner_ind]]['number'] += 1
            result[datarow[partitioner_ind]]['target_value'] += \
                    int(datarow[value_of_interest_ind])
        else:
            result[datarow[partitioner_ind]] = {'number': 1, \
                    'target_value': int(datarow[value_of_interest_ind]) }
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
    """Hackety hack. The interface of this function is hideous
    and needs to be refactored into something that makes some
    sense."""

    keys = list(partitioned_values.keys())
    values = [x['target_value'] / float(x['number']) \
            for x in list(partitioned_values.values())]
    return [keys, values]

# TODO: continue with the refactoring, this ist just the original file  
# copied over to a new location.
