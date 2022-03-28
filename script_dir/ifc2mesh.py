import subprocess
import os




def ifc2mesh(input_path, work_dir, offsets, hsrs, vsrs):

	cmd = "./IfcConvert  "+input_path+" "+work_dir+"output.glb"+" --model-rotation '0.7071067811865476;0.0;0.0;0.7071067811865476'"

	subprocess.run(cmd, shell=True)




if __name__ == "__main__":


	input_path = '../work_dir/input.las'
	ref_path = '../work_dir/input.las'
	work_dir = '../work_dir/'
	mesh2pc(input_path, work_dir)