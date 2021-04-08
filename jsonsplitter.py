#author='vemulasravan6@gmail.com'
import json
import os
import sys

class JsonUtil:

	def __init__(self):
		pass

	def chop_list_to_pieces(self, input_list=[], chop_size=None):
		return [input_list[i * chop_size:(i + 1) * chop_size] for i in range((len(input_list) + chop_size - 1) // chop_size)]

	def split_json_file(self, file_path=None, chunk_size=None, destination_directory=None, debug=False):
		destination_directory = os.getcwd()+'/'+destination_directory
		if not os.path.exists(destination_directory):os.makedirs(destination_directory)
		with open(file_path, "r") as outfile:
			json_object_list = json.load(outfile)
			json_chunk_list = self.chop_list_to_pieces(json_object_list, chunk_size)
			indx = 0
			for tmplis in json_chunk_list:
				file_path = destination_directory+'/'+str(indx)+".json"
				if debug:print('creating..'+file_path)
				with open(file_path, "w") as outfile:
					json.dump(tmplis, outfile, indent=2)
				indx+=1
		return

if __name__ == '__main__':
	try:
		file_path = sys.argv[1]
		chunk_size = int(sys.argv[2])
	except:
		print('\nPls provide input json filepath and chunk size..!\n')
		print('\nUsage : python3 jsonsplitter.py /path/to/your/jsonfile chunk_size_number\n')
		exit(1)
	ju = JsonUtil()
	ju.split_json_file(file_path = file_path, chunk_size=chunk_size, destination_directory='Chunks', debug=False)
	print('\nDone with chopping..Check your files in Chunks Directory\n')
