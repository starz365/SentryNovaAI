import time, sys, os

def anim_exit(options, opt):
    duration = 3  # Total duration before exiting
    start_time = time.time()
    print(f"\n{' '*4}You've chosen to {opt};")

    while time.time() - start_time <= duration:
        for dots in range(1, 5):  # Show 1 to 4 dots
            print(f"\r{' '*9}Parsing for {options}" + "#" * dots, end="", flush=True)
            time.sleep(0.5)  # Wait before adding another dot
        print(f"\r{' '*9}Parsing {options}    {' '*4}", end="", flush=True)  # Reset the dots
    
    print(f"\r{' '*9}Parsing {options}" + "#"*4 + " Done!\n")


def animation(options, opt):
    duration = 5  # Total duration before exiting
    start_time = time.time()
    print(f"\n{' '*4}You've chosen to view {options};")

    while time.time() - start_time <= duration:
        for dots in range(1, 5):  # Show 1 to 4 dots
            print(f"\r{' '*9}Parsing {options}" + "#" * dots, end="", flush=True)
            time.sleep(0.5)  # Wait before adding another dot
        print(f"\r{' '*9}Parsing {options}     {' '*4}", end="", flush=True)  # Reset the dots
    
    print(f"\r{' '*9}Parsing {options}" + "#"*4 + " Done!\n")


def multi_use(options):
    new ="\n"*20
    space = " "*21
    duration = 4  # Total duration before exiting
    start_time = time.time()

    while time.time() - start_time <= duration:
        for dots in range(1, 6):  # Show 1 to 4 dots
             print(f"\r{space}{options}" + "#" * dots, end="", flush=True)
             time.sleep(0.5)# Wait before adding another dot
        print(f"\r{space}{options}    {' '*4}", end="", flush=True)  # Reset the dots
    
    print(f"\r{space}{options}" + "#"*5)


#if __name__ == "__main__":
    #animation ("logs", "opt")
    #anim_exit("Exiting ", "opt" )
    #multi_use("logout ")