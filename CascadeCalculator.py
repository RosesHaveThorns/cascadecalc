y4 = [62,62,62,62,62,62,62,62,62,62,62,62]
y3 = [70,71,53,81,74,74,90,90,90,90,70,70]
y2 = [73,90,81,67,67,64,64,60,81,72,80,80]
band_s = [83] # IY Band
# 9 modules per band

BAND_SIZE = 9
BAND_DELTA = len(y4) - BAND_SIZE

# Extract BAND_SIZE best year 4 modules
y4_sorted = sorted(y4)
band_4 = y4_sorted[-BAND_SIZE:]

#################################

# Init band 3 with remaining year 4 modules
band_3 = y4_sorted[:-BAND_SIZE]

# Populate remaining slots (BAND_DELTA) of band_3
y3_sorted = sorted(y3)
band_3.extend(y3_sorted[-6:])

################################

# Init band_2 with remaining year 3 modules
band_2 = y3_sorted[:6]

# Populate remaining slots (BAND_DELTA) of band_2
y2_sorted = sorted(y2)
band_2.extend(y2_sorted[-BAND_DELTA:])


################################

# band_1 contains whatever is left
band_1 = y2_sorted[:-BAND_DELTA]

################################

# Calculate the average and weighted average for each band
bands = [band_s, band_1, band_2, band_3, band_4]
def handle_band(band, weight):
    avg = float(sum(band)) / len(band)
    wavg = avg * weight
    return avg, wavg

print("Band\tWeight\tAvg.\tW.Avg.")
total = 0
for i, band in enumerate(bands):
    band_no = i


    weight = band_no

    if (i == 0):
        weight = 0.25

    avg, wavg = handle_band(band, weight)
    total += wavg
    print("%d\t%.2f\t%.2f\t%.2f" % (band_no, weight, avg, wavg))

print("Degree Result: %.2f" % (total/10.25))
