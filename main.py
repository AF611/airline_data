#import matplotlib.pyplot as plt
xs = []
ys = []

with open("airline.csv", "r") as file:
    for line in file:
            line_splitted = line.strip().split(",")
            if line_splitted[0] == "Lufthansa":
                xs.append(line_splitted[2])
            print(xs)



