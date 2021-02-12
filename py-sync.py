#!/usr/bin/env python3

import os
import sys
import shutil
import configparser

from sh import rsync
from time import sleep
from datetime import date

configPath = 'py-sync.conf'

#func: check if directory exists
def pathExist(path):
    if not os.path.exists(path):
        sys.exit(path + " does not exist. Verify path and retry.")

#check if config file exists
if not os.path.isfile(configPath): 
	sys.exit("Error: Config file " + configPath + "is missing. Please create it.")

#parse config file
config = configparser.ConfigParser()
config.read(configPath)
inputPaths = config['input_paths']['input_paths'].split(',')
inputPath = None
numPaths = len(inputPaths)
outputPath = config['output_path']['output_path']
backupDir = config['backup_path']['backup_path']
excludePaths = config['exclude_paths']['exclude_paths'].split(',')
deleteToggle = config['arguments']['delete_from_dest']
relativeToggle = config['arguments']['use_relative_path']
backupToggle = config['arguments']['backup_deleted_dest']

args = [
	"--archive", "--human-readable", "--stats",
	"--out-format='%i | %n'", "--itemize-changes",
	inputPath, outputPath,
	]

#toggle args - relative, delete, backup
if deleteToggle == "1":
	args.insert(len(args)-2, "--delete")
if relativeToggle == "1":
	args.insert(len(args)-2, "--relative")
if backupToggle == "1":
	args.insert(len(args)-2, "--backup")
	args.insert(len(args)-2, "--backup-dir=" + backupDir)

#add exclude arguments
for excludePath in excludePaths: 
	args.insert(len(args)-2, "--exclude=" + excludePath)

#check if output path exists (HOW TO MAKE THIS WORK WITH NETWORKED STORAGE???)
#pathExist(outputPath)
#if it doesn't, ask if you want to create it

#check if input paths exist
for inputPath in inputPaths:
	pathExist(inputPath)

#check if logs dir exists, if not then create
logsDir = os.getcwd() + "/logs"
if not os.path.exists(logsDir):
	os.makedirs(logsDir)
	print("Creating logs folder in " + os.getcwd() + "\n")
	sleep(1)

backupTime = date.today()
log = open("logs/" + str(backupTime) + "-log.txt", "a")

#for each input path, rsync to output path
for inputPath in inputPaths:
	print("Backing up " + inputPath + "...\n")
	sleep(1)
	args[len(args)-2] = inputPath
	rsync(args, _out=log)

log.close

print("Backup complete")
