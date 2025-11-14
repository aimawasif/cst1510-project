import bcrypt

def hash_password(plain_text_pass):
    pass_bytes = plain_text_pass.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(pass_bytes, salt)
    return hashed_pass

simple_pass = 'simple_password'

simple_hash = hash_password(simple_pass)
print(f"Original1: {simple_pass} | Hashed: {simple_hash}")

simple_hash = hash_password(simple_pass)
print(f"Original2: {simple_pass} | Hashed: {simple_hash}")

simple_hash = hash_password(simple_pass)
print(f"Original3: {simple_pass} | Hashed: {simple_hash}")

  


      
      

