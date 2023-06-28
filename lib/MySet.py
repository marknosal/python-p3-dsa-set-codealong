class MySet:

    def __init__(self, list = []):
        self.dictionary = {}
        for thing in list:
            self.dictionary[thing] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary = {}
        return self
    
    def __str__(self):
        set_list = []
        for k, _ in self.dictionary.items():
            set_list.append(str(k))
        return f'MySet: {{{",".join(set_list)}}}'
    

