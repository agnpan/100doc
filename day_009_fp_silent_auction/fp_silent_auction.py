# SILENT AUCTION

from art import logo

all_bids = {}


def take_bid():
    """
    Takes the bidder's name and value and adds it to the dictionary storing the bidders.
    """
    bidder_name = input("What is your name? ")
    bid = int(input("Please enter your bid: $"))

    all_bids[bidder_name] = bid


def check_for_other_bidders():
    """
    Checks if there are more bidders after the user enters their data.
    :return: True if the user selects other bidders, False if they don't.
    """
    other_bidders = "answer"
    while other_bidders[0] not in ("y", "n"):
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if other_bidders[0] == "y":
        return True
    else:
        return False


def show_highest_bid():
    """
    :return: The name and the value of the highest bid.
    """
    highest_bid = 0
    winner = []
    for bid in all_bids.values():
        if bid > highest_bid:
            highest_bid = bid

    for person in all_bids.keys():
        if all_bids[person] == highest_bid:
            winner.append(person)

    if len(winner) == 1:
        return f"The winner is {winner} with ${highest_bid}."
    else:
        return f"The winners are {winner} with ${highest_bid}."


print(logo)
start_again = True

while start_again:
    take_bid()
    another_bidder = check_for_other_bidders()
    if another_bidder:
        for i in range(51):
            print()
    else:
        start_again = False

print(show_highest_bid())

# TODO: figure out what to do when there is more than 1 highest bidder with the same amount
