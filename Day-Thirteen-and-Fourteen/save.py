import csv

def save_to_file(jobs, word):
  file = open(f"{word}.csv", mode='w')
  writer = csv.writer(file)
  for job in jobs:
    writer.writerow(list(job))
  return