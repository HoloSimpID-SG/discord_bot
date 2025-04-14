# SPDX-License-Identifier: Apache-2.0
import argparse
import sys
import discord_bot

def main(argc, argv):
	parser = argparse.ArgumentParser(description=None)
	parser.add_argument('-t', '--token', help='discord app token')

	args = parser.parse_args()

	token = None
	if args.token == None:
		print('No token received, run \'python run_bot.py -t <token>\'')
		sys.exit(1)
	else:
		token = args.token

	print(f"Token is: {token}")

	bot = discord_bot.init()
	bot.run(token)


if __name__ == '__main__':
	main(len(sys.argv), sys.argv[1:])