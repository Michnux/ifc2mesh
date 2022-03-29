import subprocess
import os




def ifc2mesh(input_path, work_dir, offsets, hsrs, vsrs):

	subprocess.run('pwd', shell=True)

	cmd = "/home/script_dir/IfcConvert "+input_path+" "+work_dir+"output.glb"+" --model-rotation '0.7071067811865476;0.0;0.0;0.7071067811865476'"
	print(cmd)

	subprocess.run(cmd, shell=True)




if __name__ == "__main__":

	pass