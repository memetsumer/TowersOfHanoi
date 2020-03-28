from stack import Stack

print("\nLet's play Towers of Hanoi!!")


# Create the Stacks

def create_stacks():
    global stacks, left_stack, middle_stack, right_stack
    stacks = []
    left_stack = Stack("Left")
    middle_stack = Stack("Middle")
    right_stack = Stack("Right")
    stacks.append(left_stack)
    stacks.append(middle_stack)
    stacks.append(right_stack)


create_stacks()


# Set up the Game

def game_setup():
    global num_disks, num_optimal_moves
    num_disks = int(input("\nHow many disks do you want to play with?\n"))
    while num_disks < 3:
        num_disks = int(input("Enter a number greater than or equal to 3\n"))
    for i in range(num_disks, 0, -1):
        left_stack.push(i)
    num_optimal_moves = 2 ** num_disks - 1
    print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")


game_setup()


# Game Solver

def game_solver_util(N, begin: Stack, helper: Stack, end: Stack):
    if N == 1:
        end.push(begin.pop())
        return
    else:
        game_solver_util(N - 1, begin, end, helper)
        game_solver_util(1, begin, helper, end)
        game_solver_util(N - 1, helper, begin, end)


def game_solver(amount_disks):
    left_stack.empty_stack()
    middle_stack.empty_stack()
    right_stack.empty_stack()

    for i in range(amount_disks, 0, -1):
        left_stack.push(i)
    game_solver_util(amount_disks, left_stack, middle_stack, right_stack)
    print(left_stack.print_items(),
          middle_stack.print_items(),
          right_stack.print_items())


# Get User Input

def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    word = "solve!"

    while True:

        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]

            print(f"Enter {letter} for {name}")

        user_input = input()

        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]
        elif user_input == word:
            game_solver(num_disks)
            break


# Play the Game


def play_game():
    num_user_moves = 0

    while right_stack.get_size() != num_disks:
        print("\n\n\n...Current Stacks...")
        for i in stacks:
            print(i.print_items())
        while True:
            print("\nWhich stack do you want to move from?")
            from_stack = get_input()

            print("\nWhich stack do you want to move to?")
            to_stack = get_input()

            if from_stack.is_empty():

                print("\n\nInvalid Move. Try Again")
            elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
                disk = from_stack.pop()
                to_stack.push(disk)
                num_user_moves += 1
                break
            else:
                print("\n\nInvalid Move. Try Again")

        print(
            f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")


play_game()
