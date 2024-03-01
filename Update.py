import os

os.chdir("offsets/")
fin = open("csgo.hpp", "rt")

data = fin.read()
data = data.replace('#pragma once', '').replace("#include <cstdint>", '').replace('//' , '#').replace('namespace hazedumper {' , '')
data = data.replace("constexpr ::std::int64_t ",'')
data = data.replace("namespace netvars {" , '').replace("constexpr ::std::ptrdiff_t ", "").replace(';', '')
data = data.replace("} # namespace netvars\nnamespace signatures {", '').replace("} # namespace signatures", '')
data = data.replace('} # namespace hazedumper', '')
fin.close()

fout = open("csgo.py", "w")
fout.write(data)
fout.close()
print("Updated")