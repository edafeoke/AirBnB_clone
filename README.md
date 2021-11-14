# AirBnB_clone - The Console

![logo](hbnb.png)

##### A command interpreter to manipulate data without a visual interface (perfect for development and debugging)

![project_image](project.png)
# Installation

	git clone https://github.com/edafeoke/AirBnB_clone.git
	cd AirBnB_clone

# Usage
## Execution

#### It works in interactive mode

	./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit create show destroy all update
	
#### It also works in non-interactive mode

	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit create show destroy all update
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit create show destroy all update
	(hbnb) 
	$

## Console commands

##### EOF
###### Quits the console
	(hbnb) EOF
##### quit
###### Quits the console
	(hbnb) quit
##### help
###### Show help text
	(hbnb) help
	Documented commands (type help <topic>):
        ========================================
        EOF  help  quit create show destroy all update

	(hbnb) help quit
	(hbnb) Quits the console
##### create
###### Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
	(hbnb) create BaseModel
	49faff9a-6318-451f-87b6-910505c55907
	(hbnb)

# Authors

