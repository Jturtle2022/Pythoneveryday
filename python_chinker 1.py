def chunker(seq, size):
 return (seq[pos:pos + size] for pos in range(0, len(seq), size))
for group in chunker(order_items,100):
      for item in group:
# Do something to each group