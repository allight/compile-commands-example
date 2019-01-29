#!/usr/bin/python
#
# Copyright 2018 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import json
import os

parser = argparse.ArgumentParser(description='Generate compile_commands.json')
parser.add_argument("--working", action="store_true", default=False,
                help="Generate a compile_commands.json file that causes vscode to act correctly.")

args = parser.parse_args()

curdir = os.getcwd()
compiler_prefix = "" if not args.working else (curdir + "/")
data = [
  {
    "directory": str(curdir),
    "arguments": [
      compiler_prefix + "prebuilts/my-clang",
      "test.cc"
    ],
    "file": "test.cc"
  }
]

with open("compile_commands.json", "w") as commands_json:
  commands_json.write(json.dumps(data, indent=2))
