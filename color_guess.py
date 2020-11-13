def color_guess(color_input):
    '''
    Function transforms name of the color to RGB form
    
    Keyword arguments:
    color_input -- name of the color to transform
    '''
    input_filename = 'colors.txt'
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            color_name, color_number = line.split(':')
            if (color_name == color_input):
                color_number = color_number.split(',')
                for i in range(3):
                    color_number[i] = int(color_number[i])
                return color_number

