#!/usr/bin/env ruby
puts ARGV[0].scan(/^[a-z]*([a-z])\1[a-z]*$/).join
