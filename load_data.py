class Load:
#knmi csv file openen
    def __init__(self, folder, filename):
        #Set object variables
        self.folder = folder
        self.filename = filename
        self.info = ""
        self.column_names = []
        self.data = []
        self.open()
        
    def __str__(self):
        #return file path
        return self.folder + '/' + self.filename
    
    def open(self):
        #Load the file into comments and data as two strings.
        with open(self.folder + '/' + self.filename, 'r') as text_file:
            line = text_file.readline()
            while line:
                if line.startswith("#") or line.startswith("\""):
                    self.info += line
                else:
                    self.data_line(line)
                line = text_file.readline()
        self.set_columns_names()
    
    def data_line(self, line):
        #Delete spaces and newLine split on ,
        self.data.append(line.replace(' ', '').replace('\n', '').split(','))
           
    def set_columns_names(self):
        #Split the comments on lines. Take the last line. Remove the first character. Remove all whitespaces. Split on ',' Remove the commas and add to column_names.
        self.column_names = self.info.splitlines()[-1][1:].replace(' ', '').replace('\n', '').split(',')
        
    def __str__(self) -> str:
        concat = ""
        for item in self.column_names:
            concat += ', '.join(item) + '\n'
        for i in range(min(5, len(self.data))):  # Ensure we don't go beyond the available rows
            concat += ', '.join(self.data[i]) + '\n'
        return concat
