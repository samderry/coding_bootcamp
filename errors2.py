1
2 # Syntax. Indentation error. Move 1 tab space to the left.
3 # Syntax. Indentation error. Move 1 tab space to the left.
4 # Syntax. Indentation error. Move 1 tab space to the left.
5 # Syntax. Indentation error. Move 1 tab space to the left.
6 # Syntax. Indentation error. Move 1 tab space to the left.
7 # Syntax. Indentation error. Move 1 tab space to the left. 
8 # Syntax. Indentation error. Move 1 tab space to the left.
9 # Syntax. Indentation error. Move 1 tab space to the left.
10 
11

animal = str("lion")      # Runtime and syntax. Name error. Needs to be defined. Amended to a string, put in inverted commas and brackets.
animal_type = str("cub")  # Runtime and syntax. Name error. Needs to be defined. Amended to a string, put in inverted commas and brackets.
number_of_teeth = int(16) # Runtime and syntax. Name error. Needs to be defined. Amended to an integer, and put in brackets.

full_spec = ("This is a {}. It is a {} and it has {} teeth.".format(animal, animal_type, number_of_teeth))    # Logical. When printed out on next line,
                                                                                                                # the values are not filled in in the curly 
                                                                                                                # brackets as the string has not been formatted.        
                                                                                                                # Therefore, have put in .format for teh values 
                                                                                                                # and then the print line runs correctly
 
print (full_spec)

