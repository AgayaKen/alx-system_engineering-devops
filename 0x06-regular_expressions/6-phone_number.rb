#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression matching method

input = ARGV[0]
pattern = /^\d{10}$/

matches = input.scan(pattern)
puts matches.join

