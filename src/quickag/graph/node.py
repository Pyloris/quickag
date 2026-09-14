


class Node:

    def __init__(self, name, function, configuration):
        
        self.name = name
        self.function = function
    
        self.next = configuration.get("next_node", None)
        self.prev = configuration.get("prev_node", None)
        self.prev_output = configuration.get("prev_output", None)
   

    def execute(self, options):
        self.current_output = self.function(self.prev_output, options)

        # call the next node in line
        return self.next and self.next.execute(options)
