csv_input = """date,process,host,log,bytes 
20140206,cme_trader_2,cme0001,0345-cme_trader_2.log.gz,15400000
20140206,phlx_trader_1,phlx0001,0651-phlx_trader_1.log.gz,14100000
20140206,phlx_trader_2,phlx0001,0645-phlx_trader_2.log.gz,13800000
20140207,cme_trader_2,cme0001,0345-cme_trader_2.log.gz,15800000
20140207,cme_trader_3,cme0001,0345-cme_trader_3.log.gz,14200000
20140207,phlx_trader_1,phlx0001,0651-phlx_trader_1.log.gz,24100000
"""
"""
Builds with len of list, list rows and log_map, returns finished dict
:param list_length, rows, log_map: list_length used to iterate, create log_list
with rows and build to log_map 
:return: log_map, finished with key and value pairs
""" 
def build_map(list_length, rows, log_map):
     # Loop through len of items, split into items at ","
    for i in range(list_length): 
        # Create list of all words in row, save all values in appropriate variables
        log_list = rows[i].split(",")
        date_val = log_list[0]
        exchange_type = log_list[1].split("_")[0]
        bytes_val = int(log_list[-1])
        # Add variables to dict, date and exchange are keys and bytes_val are the value
        # Group bytes used on same day for same exchange
        log_map[(date_val, exchange_type)] = log_map[(date_val, exchange_type)] + bytes_val if (date_val,exchange_type) in log_map else bytes_val

"""
Builds final String and prints header
:param date_and_exchange: keys date and exchange 
:return: formatted string of all values
"""
def build_final_string(date_and_exchange):
    print("date,exchange,total_bytes")
    for key in date_and_exchange:
        print(str(key[0]) + "," + str(key[1]) + "," + str(log_map[key]) + "\n")


# Create empty dictionary, turn each input line into a list
# pop heading
# set length to n of items - 1 since it has to start from 0
log_map = {}
rows = csv_input.split('\n')
rows.pop(0)
list_length = len(rows) - 1

# Build map with all list items, sort dict by dates
build_map(list_length, rows, log_map)
date_and_exchange = sorted(log_map.keys(), key = lambda x: x[0])
# Loop all keys in dict, return formatted final output
build_final_string(date_and_exchange)