#SECTION D
from abc import ABC, abstractmethod

class BaseProcessor(ABC):
    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def parsed_file(self):
        pass

class LogFile(BaseProcessor):
    def __init__(self, filename):
        self.filename = filename
        records = []

    def load_file(self, filename):
        with open(filename, "r") as file:
            self.records = file.readlines()
    
    def parsed_records(self):
        parsed = []
        for line in self.records:
            parts = line.strip().split(",")

        if len[parts] >= 2:
            parsed.append ({
                "users" : parts[0],
                "status" : parts[1]
            })

            self.records = parsed
    
    def __len__(self):
        return len(self.records)
    def __str__(self):
        return f"Log File {(self.filename)} with {len(self)} records"
    
class UserAnalytics():
    def __init__(self, records):
        self.records = records
    
    def calculate_stats(self):
        stats = {}
        for record in self.records:
            user = record["user"]
            stats[user] = stats.get(user, 0)+1
            return stats
        
    
    def generate_report(self):
        stats = self.calculate_stats()
        for user, count in stats.items():
            print(f"{user}->{count} logs")

    def modify_list(data):
        data.append("new entry")
    
    my_list = [1,2,3]
    modify_list(my_list)
    print(my_list)

    import copy
    original = [{"a" : 1}]
    shallow_copy = copy.copy(original)
    deep_copy = copy.deepcopy(original)
    original[0]["a"] = 99
    print(shallow_copy)
    print(deep_copy)