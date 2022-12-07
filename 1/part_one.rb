
max = 0
current = 0
File.readlines('input.txt').each do |line|
    line = line.strip()
    if line != ""
        current += line.to_i
    else
        if current > max
            max = current
        end
        current = 0
    end
end

puts max