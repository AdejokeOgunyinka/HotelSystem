class Table:
    def __init__(self, *fields):
        self.data = {}
        self.cursor = 0
        self.fields = fields

    def insert(self, **params):
        if not isinstance(params, dict):
            raise TypeError("Expected a dictionary")

        if len(params) == 0:
            raise Exception("Your dictionary should not be empty.")

        for key in params:
            if key not in self.fields:
                raise KeyError("Key was not found.")
        else:
            self.cursor += 1
            record_id = self.cursor
            params['_id'] = record_id
            self.data[record_id] = params
            return self.data[record_id]

    def select(self, **conditions):
        if not isinstance(conditions, dict):
            raise TypeError("Expected a dictionary.")

        if len(conditions) == 0:
            raise Exception("Your dictionary should not be empty.")

        for keys in conditions:
            if keys not in self.fields:
                raise KeyError("Key was not found.")

        else:
            def filter_func(argument):
                for key, value in conditions.items():
                    if argument.get(key) != value:
                        return False
                    else:
                        return True
            return list(filter(filter_func, self.data.values()))
