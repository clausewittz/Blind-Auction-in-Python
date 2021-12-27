logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}
another_bid = True

def find_highest_bidder(bidding_record):
    
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while another_bid == True:
    name = input("What is your name? ")
    price = int(input("What is your bid? $ "))
    bids[name] = price

    ask = input("Is there anyone else to bid? Type 'yes' or 'no'.")

    if ask == "no":
        another_bid = False
        find_highest_bidder(bids)
