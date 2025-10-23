# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
for name in targets:
	print(name)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
for name, info in targets.items():
	print(name, info["Spectral Type"])
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
for name, info in targets.items():
	if info["Magnitude"] > 0.1:
		print(name)
# 4) Look up another target, add all the necessary information to the targets list.
targets["Altair"] = {
	"RA": "19h 50m 47s",
	"Dec": "+0.8° 52' 06''",
	"Magnitude": 0.76,
	"Spectral Type": "A7V"
}
print(targets)
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
closest_name = None
closest_diff = float('inf')
brightest_mag = float('inf')

for name, info in targets.items():
    dec = info["Dec"]
    try:
        dec_deg = int(dec.split()[0].replace("+", "").replace("-", ""))
        diff = abs(dec_deg - 20)
        if diff < closest_diff or (diff == closest_diff and info["Magnitude"] < brightest_mag):
            closest_diff = diff
            brightest_mag = info["Magnitude"]
            closest_name = name
    except Exception:
        continue

print(closest_name)
# 6) What is your favorite constellation?
# My favorite constellation is the Orion constellation.
