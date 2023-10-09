def get_input():
  print('guess a number whore')
  user_guess = input()
  return user_guess

def check_guess(guess, secret):
  if guess == secret:
    print('hurrey! you win bitch')
  else:
    print('you lose dumbass')

def game():
  print('hi kid')
  print('welcome to my game, lets play')

  secret_number = 5
  user_guess = get_input()
  check_guess(user_guess, secret_number)
  print('bye noob')

game()
