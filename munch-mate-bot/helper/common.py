# 
# @Author: Seven Yaoching-Chi 
# @Date: 2024-05-23 20:30:30 
# @Last Modified by:   Seven Yaoching-Chi 
# @Last Modified time: 2024-05-23 20:30:30 
# 

def gen_system_msg(prompt):
    return {'role':'system', 'content': prompt }
    
def gen_assistant_msg(prompt):
    return {'role':'assistant', 'content': prompt }

def gen_user_msg(prompt):
    return {'role':'user', 'content': prompt }