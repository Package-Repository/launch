import json

'''
json format
{
    task: "task_name",
    data: "data"
    end_condition: "end_condition"
}
'''

'''
    discord: @kialli
    github: @kchan5071
    
    parses json file for task queue
'''

class JSONParser:
    def __init__(self, file_name):
        self.task = []
        self.data = []
        self.end_condition = []
        self.file = file_name
        
    def set_file(self, file):
        self.file = file
        
    def parse(self):
        with open(self.file) as f:
            data = json.load(f)
            self.task.append(data['task'])
            self.data.append(data['data'])
            self.end_condition.append(data['end_condition'])
            
    def get_next_task(self):
        return self.task.pop(0), self.data.pop(0), self.end_condition.pop(0)