print("Welcome to the game!")
name = input("What is your name? ")
age = int(input("What is your age? "))



health = 10 



if age >= 18:
    print("Welcome!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with" , health , "health")
        print("Let the game begin!")

        left_or_right = input("First choice... left or right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you followed the path and made it to the river... Do you swim across or go over the bridge. (across/over)? ")

            if ans == "over":
                print("You made it to the other side of the river.") 

            elif ans == "across":
                print("You managed to get across, but you were bit by a fish and lost 5 health.")
                health -= 5 

            ans = input("You notice a house and the ocean. Which do you go to (house/ocean)? ") 
            if ans == "house":
                print("You go to the house and are greated by the owner he doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                  print("You now have 0, health Game Over!")
                  
                else:
                    print("Congrats you survived and won the game!")  

            else: "You fell into the ocean and died."
       
        else:
           print("You got attacted by a bear and died!")


    else:
        print("Good Bye!")

else:
  print("We are sorry you are not old enough to play this game! ")