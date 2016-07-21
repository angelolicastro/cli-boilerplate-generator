# Command Line Argument (CLI) Boilerplate Generator

CLI Boilerplate Generator is a program that generates a friendly CLI boilerplate Python program using the [argparse](https://docs.python.org/3/library/argparse.html) module.

## Requirement

* Python 2 or Python 3

## Installation

	git clone https://github.com/angelolicastro/cli-boilerplate-generator.git

## Usage

	cli-boilerplate.py [_h] [_force] name args [args ...]

## Example

	$ python cli-boilerplate-generator.py myProgramName myFirstArgument mySecondArgument --myFirstFlag
	cli-boilerplate-generator.py: myProgramName.py was successfully generated!

This will generate the following program.

	$ cat myProgramName.py

	from argparse import ArgumentParser

	def main():
		parser = ArgumentParser()

		parser.add_argument('myFirstArgument')
		parser.add_argument('mySecondArgument')
		parser.add_argument('--myFirstFlag')

		args = parser.parse_args()

		# TODO: Add some stuff here!

	if __name__ == '__main__':
		main()


## License

[The MIT License (MIT)](LICENSE)

Copyright (c) 2016 [Angelo Licastro](http://angelolicastro.com)
