# rock, paper, scissors
# wfp, 9/5/07

myBool = True
paperCount = 0
rockCount = 0
scissorCount = 0
computerWins = 0
userWins = 0
ties = 0

while myBool:
    
    choice = raw_input("Rock(r), Paper(p), Scissors(s) or Quit (q): ")
    choice = choice.lower()
    if choice in 'rpsq':
        if choice == 'q':
            myBool = False
        else:

# figure out the computer choice
            if paperCount > rockCount and paperCount > scissorCount:
                response = 's'
            elif rockCount>paperCount and rockCount > scissorCount:
                response = 'p'
            else:
                response = 'r'
# update user counts
            if choice == 'r': rockCount += 1
            elif choice == 'p': paperCount += 1
            else: scissorCount += 1

# check for a tie
            if choice == response:
                ties += 1
                print 'Human: ',choice,' Computer: ',response,': tie'

# human picks rock
            elif choice=='r':
                if response== 'p':
                    computerWins += 1
                    print 'Human: ',choice,' Computer: ',response,': computer wins'
                else: 
                    userWins += 1
                    print 'Human: ',choice,' Computer: ',response,': human wins'
                    
    # human picks paper
            elif choice=='p':
                if response=='s':
                    computerWins += 1
                    print 'Human: ',choice,' Computer: ',response,': computer wins'
                else: 
                    userWins += 1
                    print 'Human: ',choice,' Computer: ',response,': human wins'
                    
    # human picks scissors
            elif choice=='s':
                if response=='r':
                    computerWins += 1
                    print 'Human: ',choice,' Computer: ',response,': computer wins'
                else: 
                    userWins += 1
                    print 'Human: ',choice,' Computer: ',response,': human wins'
    else: 
        print "Bad choice with",choice,'choose again'

print 'Human: ',choice,' Computer: ',response,': human wins'
print "Game is over"
print "The computer won",computerWins,'rounds'
print 'The user won',userWins,'rounds'
print 'There were',ties,'ties'
print 'User picked rock',rockCount,'times'
print 'User picked paper',paperCount,'times'
print 'User picked scissors',scissorCount,'times'
