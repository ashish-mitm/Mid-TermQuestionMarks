import subprocess

process1 = subprocess.Popen(["python", "Step-1-2-2.py"]) # Create and launch process pop.py using python interpreter
process2 = subprocess.Popen(["python", "Step-2-2-3.py"])
process3 = subprocess.Popen(["python", "Step-3-2-4.py"])
process4 = subprocess.Popen(["python", "FinalOne.py"])
process1.wait() # Wait for process1 to finish (basically wait for script to finish)
process2.wait()
process3.wait()
process4.wait()