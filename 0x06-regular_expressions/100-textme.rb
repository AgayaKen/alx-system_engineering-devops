#!/usr/bin/env ruby
# This script accepts one argument and extracts sender, receiver, and flags from text messages

input = ARGV[0]
pattern = /\[SENDER:(.*?)\]\s\[RECEIVER:(.*?)\]\s\[FLAGS:(.*?)\]/

matches = input.scan(pattern)
matches.each do |match|
  puts "#{match[0]},#{match[1]},#{match[2]}"
end
