import hashlib

def getFilelines(file_path):
  with open(file_path, 'r') as file:
    lines = file.read().splitlines()
    return lines

def createDigest(decoded_text):
  return hashlib.sha1(decoded_text.encode()).hexdigest()

def crack_sha1_hash(hash, use_salts=False):
  passwords = getFilelines('./top-10000-passwords.txt')
  for password in passwords:
    if use_salts:
      salts = getFilelines('./known-salts.txt')
      for salt in salts:
        test_hash_pre = createDigest(f'{salt}{password}')
        test_hash_app = createDigest(f'{password}{salt}')   
        if hash == test_hash_pre or hash == test_hash_app:
          return password
    else:
      if hash == createDigest(password):
        return password

  return 'PASSWORD NOT IN DATABASE'