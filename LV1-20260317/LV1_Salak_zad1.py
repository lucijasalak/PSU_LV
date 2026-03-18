

def total_euro (sati, eura_po_h):
    return sati * eura_po_h

sati = float (input("Radni sati: "))
eura_po_h = float(input("eura/h: "))

ukupno = total_euro (sati, eura_po_h)
print ("Ukupno: ", ukupno, "eura.")