

import sys
import nltk

script_file = "res/script.txt"
speech_file = "res/speech.txt"
gpt_file = "res/gpt2.txt"



def GeneratePrompt():
	script_dict = CreateMediaDict(script_file)
	speech_dict = CreateMediaDict(speech_file)
	gpt_dict = CreateMediaDict(gpt_file)

	# get the last 2 lines of output from gpt2	
	prompt = GetBasePrompt()
	'''
	for k in gpt_dict.keys():
		print(k)
		print(gpt_dict[k])
	'''

	insert = None
	# now replace the nouns
	for noun in gpt_dict["NN"]:
		try:
			insert = script_dict["NN"].pop()
			print(insert)
			prompt.replace(noun, insert)
		except (IndexError, KeyError):
			print("exct")
			continue

	for verb in gpt_dict["VB"]:
		try:
			insert = speech_dict["VB"].pop()
			print(insert)
			prompt.replace(verb, insert)
		except (IndexError, KeyError):
			print("exct")
			continue

	print(prompt)#------------------------------------------------------------------------------
	return prompt



def GetBasePrompt():
	f = open(gpt_file)
	lines = f.readlines()
	f.close()
	return lines[-2] + lines[-1]

# returns a dictionary of lists of words. each list is a homogeneous group of a Part-of-Speech tag
# so a list of verbs, a list of nouns, etc.
def CreateMediaDict(filename):

	f = open(filename,"r+")

	if filename == gpt_file:
		media_prompt = GetBasePrompt()
	else:
		media_prompt = f.readline()
	dict = {}

	if media_prompt == "1":
		f.close()
		return dict

	media_toks = nltk.word_tokenize(media_prompt)
	media_tups = nltk.pos_tag(media_toks)

	for k in media_tups:     
		if k[1] in dict:
			dict[k[1]].append(k[0])
		else:
			dict[k[1]] = [k[0]]
	'''
	f.seek(0)
	if filename != gpt_file :
		f.write("1")
		f.truncate()
	'''
	f.close()
	return dict

GeneratePrompt()
