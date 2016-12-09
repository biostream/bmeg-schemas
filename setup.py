
import os
import sys
from glob import glob
from distutils.core import setup
import subprocess
from distutils.spawn import find_executable


# Find the Protocol Compiler.
if 'PROTOC' in os.environ and os.path.exists(os.environ['PROTOC']):
  protoc = os.environ['PROTOC']
elif os.path.exists("../src/protoc"):
  protoc = "../src/protoc"
elif os.path.exists("../src/protoc.exe"):
  protoc = "../src/protoc.exe"
elif os.path.exists("../vsprojects/Debug/protoc.exe"):
  protoc = "../vsprojects/Debug/protoc.exe"
elif os.path.exists("../vsprojects/Release/protoc.exe"):
  protoc = "../vsprojects/Release/protoc.exe"
else:
  protoc = find_executable("protoc")


def generate_proto(source, dest, include=".", require = True):
  """Invokes the Protocol Compiler to generate a _pb2.py from the given
  .proto file.  Does nothing if the output already exists and is newer than
  the input."""

  if not require and not os.path.exists(source):
    return

  output = source.replace(".proto", "_pb2.py")

  if (not os.path.exists(output) or
      (os.path.exists(source) and
       os.path.getmtime(source) > os.path.getmtime(output))):
    print("Generating %s..." % output)

    if not os.path.exists(source):
      sys.stderr.write("Can't find required file: %s\n" % source)
      sys.exit(-1)

    if protoc is None:
      sys.stderr.write(
          "protoc is not installed nor found in ../src.  Please compile it "
          "or install the binary package.\n")
      sys.exit(-1)

    protoc_command = [ protoc, "-I.", "-I%s" % (include), "--python_out=%s" % (os.path.abspath(dest))  , os.path.basename(source) ]
    if subprocess.call(protoc_command, cwd=os.path.dirname(source)) != 0:
      sys.exit(-1)


for a in glob("schema/*.proto"):
    generate_proto(a, "bmeg")

generate_proto("ga4gh/src/main/proto/ga4gh/bio_metadata.proto", "bmeg/ga4gh", include="../")

setup(name='bmeg-schemas',
      version='0.1',
      description='BMEG Schema Build',
      url='https://github.com/bmeg/bmeg-schemas',
      packages=['bmeg', 'bmeg.ga4gh'],
     )