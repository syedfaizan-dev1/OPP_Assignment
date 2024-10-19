class Classes:
    def __init__(self, classes):
        # list of classes and timing of classes
        self.classes = {}

    def __str__(self):
        return str(self.classes)
    
    def add_class(self, class_name, timing):
        self.classes[class_name] = timing