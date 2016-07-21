#!/usr/bin/env python

"""
cli-boilerplate-generator
Copyright (c) 2016 Angelo Licastro
See LICENSE and README.md.
"""

from argparse import ArgumentParser

from os.path import basename
from os.path import isfile

PREPEND_TEXT = [
	'from argparse import ArgumentParser\n\n',

	'def main():\n',
		'\tparser = ArgumentParser()\n\n'
]

APPEND_TEXT = [

		'\n\targs = parser.parse_args()\n\n',

		'\t# TODO: Add some stuff here!\n\n',

	'if __name__ == \'__main__\':\n',
		'\tmain()\n'
]

def getDecoratedArguments(args):
	"""Returns a list of decorated arguments."""
	decoratedArgumentBoilerplate = '\tparser.add_argument(\'{0}\')\n'
	return [decoratedArgumentBoilerplate.format(arg) for arg in args]

def writeProgram(filename, decoratedArguments):
	"""Writes the program to filename."""
	with open(filename, 'w') as f:
		f.write(''.join([''.join(item) for item in [PREPEND_TEXT, \
			[decoratedArgument for decoratedArgument in decoratedArguments], \
			APPEND_TEXT]]))

def main():
	try:
		parser = ArgumentParser(description='Generate a friendly command line \
			interface (CLI) boilerplate Python program.', prefix_chars='_')

		parser.add_argument('_force', action='store_true', \
			help='Forcibly overwrite an already existing program.')

		parser.add_argument('name', help='The name of the program.')
		parser.add_argument('args', help='The arguments of the program.', nargs='+')

		args = parser.parse_args()

		filename = '{0}.py'.format(args.name)

		if isfile(filename) and not args.force:
			print('{0}: FATAL: {1} already exists!' \
				.format(basename(__file__), filename))
			print('{0}: Use _force to forcibly overwrite {0}.' \
				.format(basename(__file__), filename))
			return

		decoratedArguments = getDecoratedArguments(args.args)

		writeProgram(filename, decoratedArguments)

		print('{0}: {1} was successfully generated!' \
			.format(basename(__file__), filename))

	except Exception as e:
		print('{0}: An unknown error occurred!\n{1}'.format(basename(__file__), e))

if __name__ == '__main__':
	main()
