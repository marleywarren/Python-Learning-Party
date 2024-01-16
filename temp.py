def convert_to_celsius(farenheit):
    '''(number) -> float

    Return the number of clesius degrres to farenheit degrees
    
    >>>convert_to_celsius(32)
    0.0
    >>>convert_to_celsius(212)
    100.0
    '''

    return (farenheit-32) * 5/9
