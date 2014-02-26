#This version handles 4 types: %d, %f, %dl, %fl.
#update item: Make value range limited.

import io, random, re, sys
from obj_types import *
from randomstring import *

def check_rel(l_op, r_op, op_type):  #to check if the comparing relation is established
	if op_type == '<':
		if l_op < r_op:
			return True
		else:
			return False
	elif op_type == '>':
		if l_op > r_op:
			return True
		else:
			return False
	elif op_type == '<=':
		if l_op <= r_op:
			return True
		else:
			return False
	elif op_type == '>=':
		if l_op >= r_op:
			return True
		else:
			return False
	elif op_type == '==':
		if l_op == r_op:
			return True
		else:
			return False
	elif op_type == '!=':
		if l_op != r_op:
			return True
		else:
			return False


while True:
	try:
		ifile_path = sys.argv[1]
		ifile = open(ifile_path, 'r')
		break
	except OSError:  #if open file unsuccessfully
		print('That was not a valid path. Please try again...')
ofile_path = ifile_path[:len(ifile_path) - 4] + '_input.txt'
ofile = open(ofile_path, 'w')

level_num = sys.argv[2]  #easy, medium, hard(1, 2, 3)
part_num = 1  #the number of the handling part
itext = ifile.readline()
ilen, ipos = len(itext), 0  #'ipos' is the start position of unread part of 'itext'
input_num = -1  #-1 is nuset value
orecord = list()  #to record the context which will write to 'ofile'
type_record = []  #to store the type information of elements in 'orecord'
obj_record = []  #to store objects in 'orecord'
rel_record = []  #to store all relations of two vars
end_str_record = list()  #to record the context of end-string
lexical_error, been_match = False, False  #'been_match' checks if there is no match at each iteration of each part
third_part_end, has_end_str = False, False

#--analysis stage--
while itext != '':
	while ipos < ilen:
		if part_num == 1:  #handle the 'number of input' section
			re_result = re.match('%%', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				if input_num == -1:
					input_num = 10  #the default value of 'input_num'
				part_num = 2
				ipos = ipos + 2
			
			re_result = re.match('Yes', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				if input_num == -1:
					input_num = random.randint(1, 10)
					ofile.write(str(input_num) + '\n')
					ipos = ipos + 3
				else:
					lexical_error = True
					break
			
			re_result = re.match('No', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				if input_num == -1:
					input_num = 10
					ipos = ipos + 2
				else:
					lexical_error = True
					break
			
			re_result = re.match('\s+', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				ipos = ipos + len(re_result.group(0))
		elif part_num == 2:  #handle the 1st part of the 'input format' section
			re_result = re.match(r'{', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				part_num = 3
				ipos = ipos + 1
			
			re_result = re.match('%dl', itext[ipos:])  #integer list case
			if not been_match and re_result:
				been_match = True
				orecord.append(VarIntList())
				obj_record.append(orecord[-1])
				type_record.append(orecord[-1]._type)
				ipos = ipos + 3
			
			re_result = re.match('%fl', itext[ipos:])  #float list case(not finish)
			if not been_match and re_result:
				been_match = True
				ipos = ipos + 3
			
			re_result = re.match('%d', itext[ipos:])  #integer case
			if not been_match and re_result:
				been_match = True
				orecord.append(VarInt())
				obj_record.append(orecord[-1])
				type_record.append(orecord[-1]._type)
				ipos = ipos + 2
			
			re_result = re.match('%z' , itext[ipos:])	#string A-Z a-z
			if not been_match and re_result:
				been_match = True
				orecord.append(VarStringDigit())
				obj_record.append(orecord[-1])
				type_record.append(orecord[-1]._type)
				ipos =ipos + 2			
			
			re_result = re.match('%s' , itext[ipos:])	#string A-Z a-z 0-9
			if not been_match and re_result:
				been_match = True
				orecord.append(VarString())
				obj_record.append(orecord[-1])
				type_record.append(orecord[-1]._type)
				ipos = ipos + 2
			
			re_result = re.match('%f', itext[ipos:])  #float case(not finish)
			if not been_match and re_result:
				been_match = True
				ipos = ipos + 2
			
			re_result = re.match('"[^"\n]*"', itext[ipos:])  #string case
			if not been_match and re_result:
				been_match = True
				re_str = re_result.group(0)
				ipos = ipos + len(re_str)
				re_str = re_str[1:len(re_str)-1]
				re_pos = 0
				while re_pos < len(re_str):  #analyze the content of the string
					re_result = re.match(r'\\n', re_str[re_pos:])
					if re_result:
						orecord.append('\n')
						type_record.append(None)
						re_pos = re_pos + 2
					
					re_result = re.match(r'\\t', re_str[re_pos:])
					if re_result:
						orecord.append('\t')
						type_record.append(None)
						re_pos = re_pos + 2
					
					re_result = re.match('[ ]+', re_str[re_pos:])
					if re_result:
						orecord.append(re_result.group(0))
						type_record.append(None)
						re_pos = re_pos + len(re_result.group(0))
					
					re_result = re.match('[^\\\\]+', re_str[re_pos:])
					if re_result:
						orecord.append(re_result.group(0))
						type_record.append(None)
						re_pos = re_pos + len(re_result.group(0))
			
			re_result = re.match('\s+', itext[ipos:])  #space characters case
			if not been_match and re_result:
				been_match = True
				ipos = ipos + len(re_result.group(0))
		elif part_num == 3:  #handle the 2nd part of the 'input format' section(not finish)
			re_result = re.match('%%', itext[ipos:])
			if not been_match and re_result:
				if third_part_end:
					been_match = True
					part_num = 4
					ipos = ipos + 2
				else:
					lexical_error = True
					break
			
			re_result = re.match(r'}', itext[ipos:])
			if not been_match and re_result:
				been_match, third_part_end = True, True
				ipos = ipos + 1
			
			#case of '='
			re_result = re.match('\$([0-9]+)[ ]*=[ ]*(-?[0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				obj_index = int(re_result.group(1)) - 1
				r_op = int(re_result.group(2))
				obj_record[obj_index].set_max(r_op)
				obj_record[obj_index].set_min(r_op)
				ipos = ipos + len(re_result.group(0))
			
			#case of '<'
			re_result = re.match('\$([0-9]+)[ ]*<[ ]*(-?[0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				obj_index = int(re_result.group(1)) - 1
				r_op = int(re_result.group(2))
				obj_record[obj_index].set_max(r_op - 1)
				ipos = ipos + len(re_result.group(0))
			
			re_result = re.match('(-?[0-9]+)[ ]*<[ ]*\$([0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				obj_index = int(re_result.group(2)) - 1
				l_op = int(re_result.group(1))
				obj_record[obj_index].set_min(l_op + 1)
				ipos = ipos + len(re_result.group(0))
			
			re_result = re.match('\$([0-9]+)[ ]*(<)[ ]*\$([0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				rel_stmt = RelStmt()
				rel_stmt.l_operand = int(re_result.group(1))
				rel_stmt.r_operand = int(re_result.group(3))
				rel_stmt.operator = re_result.group(2)
				rel_record.append(rel_stmt)
				ipos = ipos + len(re_result.group(0))
			
			#case of '>'
			re_result = re.match('\$([0-9]+)[ ]*>[ ]*(-?[0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				obj_index = int(re_result.group(1)) - 1
				r_op = int(re_result.group(2))
				obj_record[obj_index].set_min(r_op + 1)
				ipos = ipos + len(re_result.group(0))
			
			re_result = re.match('(-?[0-9]+)[ ]*>[ ]*\$([0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				obj_index = int(re_result.group(2)) - 1
				l_op = int(re_result.group(1))
				obj_record[obj_index].set_max(l_op - 1)
				ipos = ipos + len(re_result.group(0))
			
			re_result = re.match('\$([0-9]+)[ ]*(>)[ ]*\$([0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				rel_stmt = RelStmt()
				rel_stmt.l_operand = int(re_result.group(1))
				rel_stmt.r_operand = int(re_result.group(3))
				rel_stmt.operator = re_result.group(2)
				rel_record.append(rel_stmt)
				ipos = ipos + len(re_result.group(0))
			
			#case of '<='
			re_result = re.match('\$([0-9]+)[ ]*<=[ ]*(-?[0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				obj_index = int(re_result.group(1)) - 1
				r_op = int(re_result.group(2))
				obj_record[obj_index].set_max(r_op)
				ipos = ipos + len(re_result.group(0))
			
			re_result = re.match('(-?[0-9]+)[ ]*<=[ ]*\$([0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				obj_index = int(re_result.group(2)) - 1
				l_op = int(re_result.group(1))
				obj_record[obj_index].set_min(l_op)
				ipos = ipos + len(re_result.group(0))
			
			re_result = re.match('\$([0-9]+)[ ]*(<=)[ ]*\$([0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				rel_stmt = RelStmt()
				rel_stmt.l_operand = int(re_result.group(1))
				rel_stmt.r_operand = int(re_result.group(3))
				rel_stmt.operator = re_result.group(2)
				rel_record.append(rel_stmt)
				ipos = ipos + len(re_result.group(0))
			
			#case of '>='
			re_result = re.match('\$([0-9]+)[ ]*>=[ ]*(-?[0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				obj_index = int(re_result.group(1)) - 1
				r_op = int(re_result.group(2))
				obj_record[obj_index].set_min(r_op)
				ipos = ipos + len(re_result.group(0))
			
			re_result = re.match('(-?[0-9]+)[ ]*>=[ ]*\$([0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				obj_index = int(re_result.group(2)) - 1
				l_op = int(re_result.group(1))
				obj_record[obj_index].set_max(l_op)
				ipos = ipos + len(re_result.group(0))
			
			re_result = re.match('\$([0-9]+)[ ]*(>=)[ ]*\$([0-9]+)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				rel_stmt = RelStmt()
				rel_stmt.l_operand = int(re_result.group(1))
				rel_stmt.r_operand = int(re_result.group(3))
				rel_stmt.operator = re_result.group(2)
				rel_record.append(rel_stmt)
				ipos = ipos + len(re_result.group(0))
			
			#case of method 'range'
			re_result = re.match('\$([0-9]+)\.range\([ ]*(-?[0-9]+)[ ]*,[ ]*(-?[0-9]+)[ ]*\)[ ]*;', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				obj_index = int(re_result.group(1)) - 1
				para1 = int(re_result.group(2))
				para2 = int(re_result.group(3))
				if obj_record[obj_index]._type == 'int':
					obj_record[obj_index].set_min(para1)
					obj_record[obj_index].set_max(para2)
				elif obj_record[obj_index]._type == 'intlist':
					obj_record[obj_index].range(para1, para2)
				ipos = ipos + len(re_result.group(0))
			
			#case of method 'set_del'
			re_result = re.match('\$([0-9]+)\.set_del\([ ]*("[^"\n]*")[ ]*\);', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				ipos = ipos + len(re_result.group(0))
				obj_index = int(re_result.group(1)) - 1
				re_str = re_result.group(2)
				re_str = re_str[1:len(re_str)-1]
				re_pos, para1 = 0, ''
				while re_pos < len(re_str):
					re_result = re.match(r'\\n', re_str[re_pos:])
					if re_result:
						para1 += '\n'
						re_pos = re_pos + 2
					
					re_result = re.match(r'\\t', re_str[re_pos:])
					if re_result:
						para1 += '\t'
						re_pos = re_pos + 2
					
					re_result = re.match('[ ]+', re_str[re_pos:])
					if re_result:
						para1 += re_result.group(0)
						re_pos = re_pos + len(re_result.group(0))
					
					re_result = re.match('[^\\\\]+', re_str[re_pos:])
					if re_result:
						para1 += re_result.group(0)
						re_pos = re_pos + len(re_result.group(0))
				obj_record[obj_index].set_del(para1)
				
			#case of method 'set_len'
			re_result = re.match('\$([0-9]+)\.set_len\([ ]*([0-9]+)[ ]*\);', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				obj_index = int(re_result.group(1)) - 1
				para1 = int(re_result.group(2))
				obj_record[obj_index].set_len(para1)
				ipos += len(re_result.group(0))
			
			re_result = re.match('\s+', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				ipos = ipos + len(re_result.group(0))
		elif part_num == 4:  #handle the 'end-format' section
			re_result = re.match('"[^"\n]*"', itext[ipos:])  #end-string case
			if not been_match and re_result:
				if has_end_str:  #There were one more end-strings.
					lexical_error = True
					break
				else:
					been_match, has_end_str = True, True
					end_str = re_result.group(0)
					ipos = ipos + len(end_str)
					end_str = end_str[1:len(end_str)-1]
					end_pos = 0
					while end_pos < len(end_str):  #analyze the content of the end-string
						re_result = re.match(r'\\n', end_str[end_pos:])
						if re_result:
							end_str_record.append('\n')
							end_pos = end_pos + 2
						
						re_result = re.match(r'\\t', end_str[end_pos:])
						if re_result:
							end_str_record.append('\t')
							end_pos = end_pos + 2
						
						re_result = re.match('[ ]+', end_str[end_pos:])
						if re_result:
							end_str_record.append(re_result.group(0))
							end_pos = end_pos + len(re_result.group(0))
						
						re_result = re.match('[^\\\\]+', end_str[end_pos:])
						if re_result:
							end_str_record.append(re_result.group(0))
							end_pos = end_pos + len(re_result.group(0))
			
			re_result = re.match('\s+', itext[ipos:])
			if not been_match and re_result:
				been_match = True
				ipos = ipos + len(re_result.group(0))
		
		if been_match:
			been_match = False
		else:
			lexical_error = True
			break
	if lexical_error:
		break
	itext = ifile.readline()
	ilen, ipos = len(itext), 0
#--analysis stage end--

if lexical_error:
	print('There was lexical error!', ipos)
else:
#--output stage--
	while input_num > 0:
		input_num = input_num - 1
#--generation stage--
		generation_loop = True
		while generation_loop:
			for obj in obj_record:
				if obj._type == 'int':
					obj.gen_val(level_num)
				elif obj._type == 'intlist':
					obj.gen_ints()
			for rel in rel_record:
				if check_rel(obj_record[rel.l_operand - 1].get_val(), obj_record[rel.r_operand - 1].get_val(), rel.operator):
					continue
				else:
					break
			else:
				generation_loop = False
#--generation stage end--
		index = 0
		while index < len(orecord):
			if type_record[index] == 'int':
				ofile.write(str(orecord[index].get_val()))
			elif type_record[index] == 'intlist':
				for element in orecord[index].get_ints():
					ofile.write(str(element))
			elif type_record[index] == 'string':
				ofile.write(orecord[index].get_str())
			elif type_record[index] == 'stringdigit':
				ofile.write(orecord[index].get_str())
			else:
				ofile.write(orecord[index])
			index = index + 1
		ofile.write('\n')
	if len(end_str_record) != 0:
		for word in end_str_record:
			ofile.write(word)
#--output stage end--
	print('Generate output successfully.')

ifile.close()
ofile.close()	
