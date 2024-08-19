#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression matching method

input = ARGV[0]
pattern = /hbt{2,5}n/

matches = input.scan(pattern)
puts matches.join
