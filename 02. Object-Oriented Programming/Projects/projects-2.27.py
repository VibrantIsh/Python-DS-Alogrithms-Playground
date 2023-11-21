# P-2.27 Write a Python program that inputs a document and then outputs a barchart plot of the fre- quencies of each alphabet character that appears in that document.
import matplotlib.pyplot as plt

def freq(doc):
    freqs = {}
    for c in doc:
        if c.isalpha():
            c = c.lower()
            freqs[c] = freqs.get(c, 0) + 1
    return freqs

def plot(freqs):
    plt.bar(*zip(*freqs.items()))
    plt.show()

def main():
    d = input()
    p = freq(d)
    plot(p)

if __name__ == "__main__":
    main()

