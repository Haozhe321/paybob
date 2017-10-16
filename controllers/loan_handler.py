import telepot
import Database
from controllers.utilities import isReceiving
import math

USAGE_MESSAGE = "`/loan <user>` to display loans to one user, `/loan` to display all"
NO_LOANS_MESSAGE = "You have not loaned anyone anything."
INVALID_USER_MESSAGE = "The username of the user should start with @."

# Initialise database
db = Database.Database()


def loan_handler(user_id, arguments):
    # Initialisation of bot
    paybot = telepot.Bot("452146569:AAG0SaDSKuvln4Qks1aj52BdA7P3-hvz9gM")
    user = db.getUsername(user_id)

    if arguments is None:
        singleLoan = False
    else:
        singleLoan = True
        transactee = arguments[0]

    if singleLoan:
        amount = db.moneyOwed(user, transactee)
        paybot.sendMessage(user_id, single_loan_message(transactee, amount))
    else:
        loans = db.hasNotPaid(user)
        db.printTable("user")
        if loans == []:
            paybot.sendMessage(user_id, NO_LOANS_MESSAGE)
        else:
            message = "Loans:"
            counter = 1
            for loan in loans:
                (transactee, amount) = loan
                message += "\n" + str(counter) + ". " + single_loan_message(user, amount)
                counter += 1
            paybot.sendMessage(user_id, message)


def single_loan_message(transactee, amount):

    if (db.userExists(transactee) == False):
        return transactee + " does not use PayBot."
    elif amount == 0:
        return transactee + " owes you nothing."
    elif isReceiving(amount):
        return transactee + " owes you $" + str(amount)
    else:
        absAmount = math.fabs(amount)
        return transactee + " owes you nothing. In fact, You owe " + transactee + " $" + str(amount)
