def find_log_entries(log_type):
    with open("data_test/application.log", "r") as file:
        for line in file:
            if log_type in line:
                print(line)


find_log_entries("ERROR")
