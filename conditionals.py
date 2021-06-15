#conditionals
userReply = input("Do you need to ship a packae?(Type yes or no)")
if userReply == "yes":
    print("we can help you ship the package")

#add else statement
else:
    print("Please come back when you do need to ship a package: Thank you.")
#add elif statemenet
userReply = input("would you like to buy stamp, an envelope, or make a copy? (Type stamps, envelope, or copy)")
if userReply == "stamps":
    print("we have plenty of stamp designs to choose form.")
elif userReply == "envelope":
    print("we have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Type a number)")
    print("Here are {} copies".format(copies))
else:
    print("Thank you, Please come again")