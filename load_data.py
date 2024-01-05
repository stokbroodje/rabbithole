class Load:
#knmi csv file openen
    def __init__(self, filename, folder = None):
        #Set object variables
        path = self.select_path(folder, filename)
        self.bg_words = []
        self.open(path)
        
    def __str__(self):
        #return file path
        return self.folder + '/' + self.filename
    
    def open(self, path):
        #Load the file into comments and data as two strings.
        with open("tatoeba_bg_eng.tsv", encoding="utf8") as text_file:
            line = text_file.readline()
            while line:
                self.bg_words.extend(self.select(line))
                line = text_file.readline()
    
    def select(self, line):
        #select all bg words from line add to list
        line = line.split('\t')
        if len(line) >= 2:
            line = self.remove_non_letter(line[1])
            return line.lower().split(' ')
        return ""
        
    def remove_non_letter(self, line):
        #dirty
        return line.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("\"", "").replace("(", "").replace(")", "")      
        
    def __str__(self) -> str:
        concat = ""
        for i in range(min(5, len(self.bg_words))):  # Ensure we don't go beyond the available rows
            concat += ', '.join(self.bg_words[i]) + '\n'
        return concat
    
    def select_path(self, folder, filename):
            if folder != None:
                return folder + '/' + filename
            else:
                return filename
            