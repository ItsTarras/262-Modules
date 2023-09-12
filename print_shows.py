def print_shows(show_list):
    """Returns the biggest number using the greedy algorithm"""
    totals = []
    done = False
    starts = []
    for item in show_list:
        total = item[1] + item[2]
        totals.append(total)
        starts.append(item[1])
    #print(totals)
    start = float('-inf')
    while start < max(totals):
        if start > max(starts):
            break
        #print(start, max(totals))
        minimum = float('inf')
        for item in show_list:
            end_time = item[1] + item[2]
            start_time = item[1]
            index = item[0]
            #Create a variable START which the end must be bigger than or = to.
            if start_time >= start:
                if end_time >= start:
                    if end_time <= minimum:
                        minimum = end_time
                        saved_start = start_time
                        saved_end = end_time
                        saved_index = index
        print(f"{saved_index} {saved_start} {saved_end}")
        start = saved_end
            #If it IS bigger than or equal to, we need to find the fastest finish time
            

        
# The example from the lecture notes
print_shows([
    ('a', 0, 6),
    ('b', 1, 3),
    ('c', 3, 2),
    ('d', 3, 5),
    ('e', 4, 3),
    ('f', 5, 4),
    ('g', 6, 4),
    ('h', 8, 3)])

# The example from the lecture notes
print_shows([
('Lazaro Lindo', 948, 48),
('Otelia Olivar', 415, 37),
('Lean Lyall', 111, 45),
('Sherlene Schneck', 841, 34),
('Jacinta Jara', 53, 36),
('Jamaal Jonson', 267, 11),
('Ehtel Engram', 24, 2),
('Catrina Coletta', 167, 50),
('Diann Dimeo', 698, 2),
('Glenn Garst', 583, 5),
('Ciera Canela', 198, 22),
('Youlanda Yepez', 695, 31),
('Kandra Keasler', 641, 23),
('Hettie Housand', 205, 6),
('Brenna Blanca', 324, 22),
('Virgil Vides', 770, 34),
('Krystina Karcher', 47, 47),
('Sindy Simek', 179, 14),
('Leanne Lindauer', 132, 49),
('Cristie Chesnutt', 12, 30),
('Migdalia Manske', 484, 8),
('Abram Aquilino', 143, 45),
('Minnie Mcclinton', 678, 24),
('Hilma Hodgin', 760, 5),
('Edythe Estepp', 436, 7),
('Zonia Zacharias', 263, 33),
('Marylin Mai', 550, 4),
('Tana Tonn', 170, 2),
('Lawrence Longacre', 554, 11),
('Delbert Degarmo', 234, 16),
('Margit Mendenhall', 767, 11),
('Liz Low', 640, 40),
('Nakisha Ned', 525, 26),
('Octavia Ojeda', 554, 21),
('Gertha Greening', 1, 37),
('Jolanda Jakubowski', 532, 26),
('Codi Covert', 344, 45),
('Cammie Cassidy', 109, 44),
('Tilda Tippie', 995, 15),
('Sherril Strebel', 986, 42),
('Lizzette Lawless', 771, 18),
('Leia Lieu', 355, 12),
('Julian Joe', 161, 30),
('Carolynn Canez', 974, 27),
('Magda Mcdowell', 904, 40),
('Izola Igoe', 375, 21),
('Shakira Sonnenberg', 9, 4),
('Ardith Artiaga', 858, 20),
('Marry Montag', 708, 6),
('Rod Ruggiero', 973, 16)
])