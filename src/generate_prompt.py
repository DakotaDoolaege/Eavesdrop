#
# Produce a string to prompt the gpt-2 algorithm.
# The prompt is generated by sewing reference material from
# converstations and previous gpt-2 outputs into sentences
# pulled from movie scripts.
#
import sys
import nltk
import parseparse

speech_file = "res/eavesdrop.txt"
gpt_file = "res/gpt2.txt"

def GeneratePrompt():
	
	prompt = parseparse.Sliced()
	script_dict = PopulateDict(prompt)
	speech_dict = CreateMediaDict(speech_file)
	gpt_dict = CreateMediaDict(gpt_file)
	
	print("\n---------------------\ninserts:")
	insert = None
	if "NN" in script_dict.keys():
		for noun in script_dict["NN"]:
			try:
				insert = gpt_dict["NN"].pop()
				prompt = prompt.replace(noun, insert)
				print(insert)
			except IndexError:
				continue
			except  KeyError:
				continue

	if "VB" in script_dict.keys():
		for verb in script_dict["VB"]:
			try:
				insert = speech_dict["VB"].pop()
				prompt = prompt.replace(verb, insert)
				print(insert)
			except IndexError:
				continue
			except  KeyError:
				continue
	print("---------------------")
	return prompt


def PopulateDict(media_prompt):

	media_dict = {}
	media_toks = nltk.word_tokenize(media_prompt)
	media_tups = nltk.pos_tag(media_toks)

	for k in media_tups:
		if k[1] in media_dict:
			media_dict[k[1]].append(k[0])
		else:
			media_dict[k[1]] = [k[0]]

	return media_dict


# returns a dictionary of lists of words. each list is a homogeneous group of a Part-of-Speech tag
# so a list of verbs, a list of nouns, etc.
def CreateMediaDict(filename):

	f = open(filename,"r+")
	media_dict = {}

	if (filename == gpt_file):
		lines = f.readlines()
		
		if len(lines) > 1:
			media_prompt =  lines[-2] + lines[-1]
		elif len(lines) > 0:
			media_prompt = lines[-1]
		else:
			media_prompt = f.readlines()[-2] + f.readlines[-1]
	else:
		media_prompt = f.readline()

	if media_prompt == "1":
		f.close()
		return media_dict

	media_dict = PopulateDict(media_prompt)

	
	if filename == speech_file :
		f.seek(0)
		f.write("1")
		f.truncate()

	f.close()
	return media_dict

GeneratePrompt()
