# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# # TODO-3: Whether if new bids need to be added
import art

print(art.logo)
bids = {}
continue_bidding = True

while continue_bidding:
    user_name = input("What is your name?\n").lower()
    bid = int(input("What is your bid?\n$"))
    bids[user_name] = bid
    others = input("Are there other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n" * 20)
    if others == "no":
        continue_bidding = False
        bid = bids
        highest_bidder = max(bids, key=bid.get)
        winning_amount = bid[highest_bidder]

        print(f"The winner is: {highest_bidder}, with {winning_amount}.")

# # TODO-4: Compare bids in dictionary
#bids = {'Alice': 150, 'Bob': 300, 'Charlie': 275}


# max function gets us the highest number in a list.
# formula = max(variable key=variable.get). but in our case, it's max(bids, key=bid.get)