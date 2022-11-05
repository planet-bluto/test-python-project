def loop():
	print("How are you?")
	response = input()
	print("You're \"" + response + "\"? Ok.")
	loop()

loop()