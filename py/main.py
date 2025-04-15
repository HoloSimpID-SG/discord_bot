# SPDX-License-Identifier: Apache-2.0
import argparse
import sys
import discord_bot

def main_help():
	print('Incomplete command, run \'python run_bot.py -t <token> -n <server_name>\'')
	sys.exit(1)

def main(argc, argv):
	parser = argparse.ArgumentParser(description=None)
	parser.add_argument('-t', '--token', help='discord app token')
	parser.add_argument('-n', '--name',  help='discord server name')

	args = parser.parse_args()

	if ((args.token == None) and (args.name == None)):
		main_help()

	bot = discord_bot.init(args.name)
	bot.run(args.token)


if __name__ == '__main__':
	main(len(sys.argv), sys.argv[1:])