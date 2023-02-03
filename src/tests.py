"""Tests for the project, to see if nothing broke"""
import os
import subprocess

from sty import ef, fg, rs

from src.logger import logger



def pylint_check():
	"""Check the code quality of the project with PyLint"""
	project_path = os.getcwd()
	errors = 0
	for root, _ , files in os.walk(project_path):
		for file in files:
			if file.endswith(".py"):
				file_path = os.path.join(root, file)
				logger(ef.bold + fg(212,175,55) + 'Pylinting file -> ' + fg.rs + rs.bold_dim + os.path.relpath(file_path, project_path))
				result = subprocess.run(["pylint", file_path], stdout=subprocess.PIPE, check=False) #stderr=subprocess.PIPE
				stdout = result.stdout.decode().splitlines()
				#stderr = result.stderr.decode()
				for line in [line for line in stdout if (not line=="") and (not "------------------" in line) ]:
					if "**********" in line:
						pass
					elif "Your code has been rated at" in line:
						logger(line.split(" (previous run: ")[0])
					else:
						lline = line.split(":")
						logger(ef.bold + fg(255,0,0) + "Error : " + fg.rs + rs.bold_dim + fg(50,111,168) + lline[1] + fg.rs + ":" + fg(50,111,168) + lline[2] + fg.rs + lline[3] + lline[4])
						errors += 1
				print(" ")
	if errors == 0:
		logger(ef.bold + fg(0,255,0) + "No errors found" + fg.rs + rs.bold_dim)
	else:
		logger(ef.bold + fg(255,0,0) + f"{errors} errors found" + fg.rs + rs.bold_dim)
