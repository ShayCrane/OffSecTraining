#!/usr/bin/python


# based on exercises and labs in offsec.com Get Good at Python learning path


Fact = "When a solution contains more of a solute than can be dissolved, it is known to be supersaturated."

start = "super"
end = "saturated."

#print(Fact.index(start))
#print(Fact.index(end))

slice = Fact[Fact.index(start):Fact.index(end)]

print(slice)

end
