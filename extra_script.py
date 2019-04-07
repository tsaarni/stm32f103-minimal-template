Import("env")
env.Append(LINKFLAGS=["--specs=nano.specs"])
env.Append(CXXFLAGS=["-Wno-register"])

# for printing floats
#env.Append(LINKFLAGS=["--specs=nano.specs", "-u", "_printf_float"])
