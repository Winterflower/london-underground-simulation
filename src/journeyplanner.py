
import journeyplannerutils




def print_options():
    options={"help":"For help, please type 'help'",
            "shortest":"To find the shortest path between two Tube stations type 'shortest'",
             "exit":"To exit the planner, type 'exit'"}
    for option in options.keys():
        print options[option]

def parser(command):
    if command=="help":
        print "HAHA, I don't have a help functionality"
    elif command=="shortest":
        print "From: "
        source=raw_input()
        print "To: "
        destination=raw_input()
        journeyplannerutils.find_shortest_path(source,destination)

    elif command=="exit":
        return 0
    else:
        print "Apologies, the command was not recognized"


def main():
    print "####################***#####################"
    print "##########SIMPLE JOURNEY PLANNER############"
    print "####################***#####################"

    print "Welcome to the London Underground"
    print_options()

    while True:
        print "Please enter command"
        command=raw_input()
        code=parser(command)
        if code==0:
            break


if __name__=="__main__":
    main()
