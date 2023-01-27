import os
import subprocess

from sty import ef, fg, rs

from src.logger import logger



def pylint_check():
	for root, dirs, files in os.walk(os.getcwd()):
		for file in files:
			if file.endswith(".py"):
				file_path = os.path.join(root, file)
				logger(ef.bold + fg(212,175,55) + 'Pylinting file -> ' + fg.rs + file + rs.bold_dim)
				result = subprocess.run(["pylint", file_path], stdout=subprocess.PIPE, check=False) #stderr=subprocess.PIPE
				stdout = result.stdout.decode().splitlines()
				#stderr = result.stderr.decode()
				for line in [line for line in stdout if (not line=="") and (not "------------------" in line) ]:
					if "**********" in line:
						print(line)
					else:
						print(line)