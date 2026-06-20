
import csv

class ExpenseSharing:

    def __init__(self, friends):
        self.friends = friends
        self.balances = {friend: 0 for friend in friends}

    def add_expense(self, payer, amount, participants):

        # Equal share for each participant
        split_amount = amount / len(participants)

        # Subtract each participant's share
        for participant in participants:
            self.balances[participant] -= split_amount

        # Add full amount to the payer
        self.balances[payer] += amount

    def calculate_settlement(self):

        creditors = []
        debtors = []

        # Separate creditors and debtors
        for friend, balance in self.balances.items():

            if balance > 0:
                creditors.append((friend, balance))

            elif balance < 0:
                debtors.append((friend, -balance))

        print("\nFinal Settlement:\n")

        while debtors and creditors:

            debtor, debt_amount = debtors.pop()
            creditor, credit_amount = creditors.pop()

            payment = min(debt_amount, credit_amount)

            print(f"{debtor} pays {creditor}: Rs.{payment:.2f}")

            # Debtor still owes money
            if debt_amount > payment:
                debtors.append(
                    (debtor, debt_amount - payment)
                )

            # Creditor still has to receive money
            if credit_amount > payment:
                creditors.append(
                    (creditor, credit_amount - payment)
                )


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":

    # Input friend names
    friends = input(
        "Enter the names of friends separated by commas: "
    ).split(",")

    friends = [friend.strip() for friend in friends]

    expense_sharing = ExpenseSharing(friends)

    # Create CSV file
    with open("expenses.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Payer",
            "Amount",
            "Participants"
        ])

    while True:

        payer = input(
            "\nEnter the name of the person who paid (or 'done' to finish): "
        )

        if payer.lower() == "done":
            break

        # Check invalid payer
        if payer not in friends:
            print("Invalid payer name! Please enter a valid friend name.")
            continue

        amount = float(
            input("Enter the amount paid: ")
        )

        # Refund detection
        if amount < 0:
            print("Refund transaction detected.")

        participants = input(
            "Enter the names of participants separated by commas: "
        ).split(",")

        participants = [
            participant.strip()
            for participant in participants
        ]

        # Remove duplicate names
        participants = list(set(participants))

        # Remove invalid participants
        valid_participants = []

        for participant in participants:

            if participant in friends:
                valid_participants.append(participant)

            else:
                print(
                    f"{participant} is not a valid friend and will be ignored."
                )

        participants = valid_participants

        # No valid participants
        if len(participants) == 0:
            print("No valid participants found.")
            continue

        # Add expense
        expense_sharing.add_expense(
            payer,
            amount,
            participants
        )

        # Save to CSV
        with open("expenses.csv", "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                payer,
                amount,
                ",".join(participants)
            ])

    # Print balances
    print("\nBalances:\n")

    for friend, balance in expense_sharing.balances.items():

        print(f"{friend}: {balance:.2f}")

    # Final settlement
    expense_sharing.calculate_settlement()

