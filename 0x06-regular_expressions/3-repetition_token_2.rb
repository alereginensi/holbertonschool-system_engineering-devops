#!/usr/bin/env ruby
puts ARGV[0].scan(/\b\w*(\w)\1\w*\b/).join
