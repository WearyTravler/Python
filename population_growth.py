#!/usr/bin/python3


def main(): 

    # init # of organisms 
    # rate of growth
    # # of hours it takes to achieve this rate 
    # # of hours during which the population grows 

    #example 500 organisms, growth rate is 2, growth period 
    #is 6 hours, doubling in size every 6 hours 
    while True:
        try:
            number = int(input("Enter the initial number of organisms: "))

            growth_rate = int(input("Enter the rate of growth [a real number > 1]: "))

            growth_interval = int(input("Enter the number of hours to achieve the rate of growth: : "))

            hours_growth = int(input("Enter the total hours of growth: "))
            
            break

        except ValueError:
            print("Please input a number, not a float or otherwise.")


    # The number of times to loop is hours_growth / growth_interval 

    loop_count = hours_growth / growth_interval
    
    while loop_count != 0:
        number = number * growth_rate 
        loop_count -= 1 
    
    print("The total population is ", number)


    another_population = input("Do you have another population [y/n]: ")
    if another_population == "n":
        exit()
    else:
        main()

main()

