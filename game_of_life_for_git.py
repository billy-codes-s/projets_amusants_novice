import random, time, os

# python version 3.something probably compatible
# usage -- > RUN: it will generage a random patter that will follow
###         the rules of conway's game of life

map_dimension = 200  # the number of y and x lifes allocated


def main():

    ##initiate the map
    river_of_life = []

    ## we are going to place all the objects now
    for elements in range(map_dimension):

        ## this is a row
        new_river = []
        for els in range(map_dimension):
            ##it is important to make the "life" know where it is placed

            ## we want 1/3 of chance so that there is life
            cell = life(
                (els, elements),
                state=random.choice([True, False, False, False, False, False]),
            )
            new_river.append(cell)

        ## append row of xes
        river_of_life.append(new_river)

    while True:
        ## we have to do this in a seprate loop because not all of life was initiated
        ### the approach is non-continus, so cycle-based
        for elements in river_of_life:
            for el in elements:
                el.neig_calc(river_of_life)

        ### here it will apply the logic, and kill itself if neccessary
        for elements in river_of_life:
            for ele in elements:
                ele.evaluate()

        ### display in desired range
        for elements in river_of_life[0:80]:
            for el in elements[0:200]:
                if el.state:
                    print("#", end="")

                else:
                    print(" ", end="")
            print("")
        time.sleep(0.05)
        os.system("clear")


class life:
    def __init__(self, position, state=False):
        self.state = state
        self.qte_neighbours = 0
        self.position = position

    def neig_calc(self, river_of_life):

        ## it does a simple 3 - 3 matrix calculation
        neigh_count = 0
        for elementes in range(self.position[1] - 1, self.position[1] + 1):
            for elements in range(self.position[0] - 1, self.position[0] + 1):

                ## this is simply to prevent the error of going through the borders
                try:
                    if river_of_life[elementes][elements].state == True:
                        neigh_count = neigh_count + 1

                except:
                    ### it will continue, and not count the false n as an n
                    continue

        ## update the data
        self.qte_neighbours = neigh_count

    ## neighbour logic
    def evaluate(self):

        ## check flow chart for more details
        if (self.qte_neighbours < 2) or (self.qte_neighbours > 3):
            self.state = False
        else:
            self.state = True

    ## neighbour logic
    def evaluate(self):

        ## check flow chart for more details
        if (self.qte_neighbours < 2) or (self.qte_neighbours > 3):
            self.state = False
        else:
            self.state = True


### if you run this file, this will happen:
if __name__ == "__main__":
    main()
