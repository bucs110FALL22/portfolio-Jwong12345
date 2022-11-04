import rectangle
import surface

r = rectangle.rectangle(10, 10, 10, 10)
assert((r.x, r.y, r.height, r.width) == (10,10,10,10))
r = rectangle.rectangle(-1, 1, 1, 1)
assert((r.x, r.y, r.height, r.width) == (0,1,1,1))
r = rectangle.rectangle(1, -1, 1, 1)
assert((r.x, r.y, r.height, r.width) == (1,0,1,1))
r = rectangle.rectangle(1, 1, -1, 1)
assert((r.x, r.y, r.height, r.width) == (1,1,0,1))
r = rectangle.rectangle(1, 1, 1, -1)
assert((r.x, r.y, r.height, r.width) == (1,1,1,0))

s = surface.surface("myimage.png", 10, 10, 10, 10)
assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))
srect = s.getRect()
assert(srect.x,  s.rect.y, srect.height,  srect.width) == (10,10,10,10)
assert s.image 
print("Test Complete!")
