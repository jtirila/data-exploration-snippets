import csv

def read_csv_file(filename, delimiter = None, quotechar = None, has_header = None):
    """Reads a csv file and returns the data as a list.

       This is somewhat crude and should be eliminated in the futures. Probably
       it is better to use the methods provided by the Pandas project to have
       efficient writes.

       Sniffer functionality is skipped if all the 'optional' parameters
       are provided. Otherwise, the ones provided are ignored and attempt
       is made at detecting the csv dialect completely automatically.
       Again, this is somewhat crude."""

    with open(filename, newline='') as csvfile:

        if should_sniff(delimiter, quotechar, has_header):
            sniffer = csv.Sniffer()
            # Detect delimiter, quotechar etc. automatically
            dialect = sniffer.sniff(csvfile.read(1024))
            # Go back to beginning
            csvfile.seek(0)
            csvreader = csv.reader(csvfile, dialect)
        else:
            csvreader = csv.reader(csvfile, delimiter = delimiter, quotechar = quotechar, )
            if has_header:
                next(csvreader, None)

        return list(csvreader)

def should_sniff(delimiter, quotechar, has_header):
    """Determines whether we must use the CSV sniffer or
       if everything is already known"""

    return delimiter == None or quotechar == None or has_header == None

